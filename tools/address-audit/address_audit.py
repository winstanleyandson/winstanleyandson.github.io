#!/usr/bin/env python3
"""
Address completeness audit for the VisionPMS recall export.

Usage:
    python3 address_audit.py export.csv [--as-of 2026-09-07] [--out report.csv]

Reads the weekly VisionPMS export (CSV or XLSX), assigns each record to a
recall band, checks the postcode against the UK format, and prints a table of
completeness by band. Column names are auto-detected but can be overridden
with --postcode / --address / --recall-date / --band.

No data leaves the machine. Stdlib only, except openpyxl for .xlsx input.
"""
import argparse
import csv
import re
import sys
from collections import OrderedDict
from datetime import date, datetime

# Full UK postcode format (GOV.UK / BS 7666 pattern), case- and space-tolerant.
UK_POSTCODE = re.compile(
    r"^(GIR ?0AA|(?:[A-PR-UWYZ][0-9]{1,2}|[A-PR-UWYZ][A-HK-Y][0-9]{1,2}|"
    r"[A-PR-UWYZ][0-9][A-HJKPSTUW]|[A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY]) ?"
    r"[0-9][ABD-HJLNP-UW-Z]{2})$",
    re.IGNORECASE,
)

# Bands in months since/until the recall due date. Order matters.
BANDS = OrderedDict([
    ("due30",  lambda d: -1 <= d <= 30),         # due within the next 30 days (or last day)
    ("0-6m",   lambda d: -183 <= d < -1),        # overdue by up to 6 months
    ("6-12m",  lambda d: -365 <= d < -183),
    ("12-24m", lambda d: -730 <= d < -365),
    ("24-36m", lambda d: -1095 <= d < -730),
    ("36m+",   lambda d: d < -1095),
    ("future", lambda d: d > 30),
])

DATE_FORMATS = ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y", "%d/%m/%y", "%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M")


def guess(columns, *needles):
    low = {c.lower().replace("_", " ").strip(): c for c in columns}
    for n in needles:
        for k, orig in low.items():
            if n in k:
                return orig
    return None


def parse_date(s):
    s = (s or "").strip()
    for f in DATE_FORMATS:
        try:
            return datetime.strptime(s, f).date()
        except ValueError:
            pass
    return None


def load_rows(path):
    if path.lower().endswith(".xlsx"):
        try:
            import openpyxl
        except ImportError:
            sys.exit("pip install openpyxl to read .xlsx, or export as CSV")
        ws = openpyxl.load_workbook(path, read_only=True).active
        it = ws.iter_rows(values_only=True)
        header = [str(h or "").strip() for h in next(it)]
        return header, [dict(zip(header, ["" if v is None else str(v) for v in r])) for r in it]
    with open(path, newline="", encoding="utf-8-sig") as fh:
        r = csv.DictReader(fh)
        return r.fieldnames, list(r)


def normalise_postcode(pc):
    pc = re.sub(r"\s+", "", (pc or "").upper())
    return pc[:-3] + " " + pc[-3:] if len(pc) > 3 else pc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--as-of", default=date.today().isoformat())
    ap.add_argument("--postcode")
    ap.add_argument("--address", help="first address line column")
    ap.add_argument("--recall-date")
    ap.add_argument("--band", help="use an existing band column instead of computing one")
    ap.add_argument("--out", help="write per-record flags to this CSV")
    a = ap.parse_args()

    header, rows = load_rows(a.path)
    as_of = date.fromisoformat(a.as_of)

    pc_col = a.postcode or guess(header, "postcode", "post code", "postal")
    ad_col = a.address or guess(header, "address1", "address 1", "addr1", "address line 1", "address")
    rd_col = a.recall_date or guess(header, "recall due", "recall date", "next recall", "recall", "due")
    band_col = a.band or guess(header, "band")

    print(f"records: {len(rows)}")
    print(f"columns: postcode={pc_col!r} address={ad_col!r} recall_date={rd_col!r} band={band_col!r}\n")
    if not pc_col:
        sys.exit("could not find a postcode column; pass --postcode")

    stats = OrderedDict((b, dict(n=0, has_pc=0, valid_pc=0, addr_no_pc=0, no_addr=0)) for b in list(BANDS) + ["unknown"])
    flagged = []

    for r in rows:
        if band_col:
            band = (r.get(band_col) or "").strip() or "unknown"
            stats.setdefault(band, dict(n=0, has_pc=0, valid_pc=0, addr_no_pc=0, no_addr=0))
        else:
            d = parse_date(r.get(rd_col)) if rd_col else None
            band = "unknown"
            if d:
                delta = (d - as_of).days
                band = next((b for b, f in BANDS.items() if f(delta)), "unknown")

        pc_raw = (r.get(pc_col) or "").strip()
        addr = (r.get(ad_col) or "").strip() if ad_col else ""
        valid = bool(pc_raw) and bool(UK_POSTCODE.match(pc_raw))

        s = stats[band]
        s["n"] += 1
        if pc_raw:
            s["has_pc"] += 1
        if valid:
            s["valid_pc"] += 1
        if addr and not pc_raw:
            s["addr_no_pc"] += 1
        if not addr and not pc_raw:
            s["no_addr"] += 1

        flagged.append({
            **r,
            "band": band,
            "postcode_present": int(bool(pc_raw)),
            "postcode_valid_format": int(valid),
            "postcode_normalised": normalise_postcode(pc_raw) if valid else "",
            "address_status": "ok" if valid else ("repairable" if addr else "no_address"),
        })

    def pct(x, n):
        return f"{100 * x / n:5.1f}%" if n else "   - "

    print(f"{'band':8} {'records':>8} {'postcode':>9} {'valid fmt':>10} {'addr,no pc':>11} {'no address':>11}")
    tot = dict(n=0, has_pc=0, valid_pc=0, addr_no_pc=0, no_addr=0)
    for b, s in stats.items():
        if not s["n"]:
            continue
        for k in tot:
            tot[k] += s[k]
        print(f"{b:8} {s['n']:8} {pct(s['has_pc'], s['n']):>9} {pct(s['valid_pc'], s['n']):>10} "
              f"{pct(s['addr_no_pc'], s['n']):>11} {pct(s['no_addr'], s['n']):>11}")
    s = tot
    print(f"{'ALL':8} {s['n']:8} {pct(s['has_pc'], s['n']):>9} {pct(s['valid_pc'], s['n']):>10} "
          f"{pct(s['addr_no_pc'], s['n']):>11} {pct(s['no_addr'], s['n']):>11}")

    if a.out and flagged:
        with open(a.out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(flagged[0].keys()))
            w.writeheader()
            w.writerows(flagged)
        print(f"\nper-record flags written to {a.out}")


if __name__ == "__main__":
    main()

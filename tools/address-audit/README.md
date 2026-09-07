# Address audit and GHL postal field mapping

Tooling and spec for adding postal address to the weekly VisionPMS → GoHighLevel (GHL) feed.
The patient export itself is **never** committed to this repository.

## 1. Run the completeness audit

```
python3 tools/address-audit/address_audit.py /path/to/visionpms-export.csv --as-of 2026-09-07 --out flags.csv
```

Output is one row per recall band: record count, % with any postcode, % with a
postcode that passes the UK format check, % with an address line but no postcode
(repairable via PAF lookup), and % with no address at all.

Columns are auto-detected. Override if the guess is wrong:
`--postcode`, `--address`, `--recall-date`, or `--band` (to use a precomputed band column).

Bands are computed from the recall due date relative to `--as-of`:
due30, 0-6m, 6-12m, 12-24m, 24-36m, 36m+ overdue, future.

`flags.csv` adds `band`, `postcode_present`, `postcode_valid_format`,
`postcode_normalised` and `address_status` (`ok` / `repairable` / `no_address`)
to every record. Only the `ok` and `repairable` rows go to the PAF cleanse;
`no_address` rows are excluded from postal until reception captures an address.

## 2. Field mapping (VisionPMS → GHL native fields)

| VisionPMS column (adjust to export) | GHL field      | Transform                                |
|-------------------------------------|----------------|------------------------------------------|
| Address line 1                      | `address1`     | trim; append line 2 with ", " if present |
| Town / City                         | `city`         | trim, title case                         |
| County                              | `state`        | trim (optional, may be blank)            |
| Postcode                            | `postal_code`  | upper case, single space before inward code |
| (constant)                          | `country`      | `GB`                                     |

Do **not** map to custom fields. Stannp, Scribeless and GHL smart-list filters read the native fields only.

## 3. Sync rules for the Make scenario

1. VisionPMS is the address source of truth. Sync is one-way, VisionPMS → GHL.
2. **Skip the address update** for any contact carrying tag `ADDRESS_BAD` or `ADDRESS_CORRECTED`.
   Instead raise a GHL task for reception to update VisionPMS. Once reception has updated
   VisionPMS, they remove the tag and the next weekly run resyncs normally.
3. Only write `postal_code` when it passes the UK format check; otherwise leave existing GHL
   values untouched and tag `ADDRESS_INCOMPLETE`.
4. Returned mail workflow: staff add `ADDRESS_BAD` + note. This tag also excludes the contact
   from every postal campaign automatically.

## 4. Pre-send checklist for cold recall postal (12-36m)

- [ ] One-off PAF cleanse of the full file (getAddress.io / Ideal Postcodes / Loqate). Store the result as `address_validated` date on the contact.
- [ ] Deceased screening against Mortascreen or The Bereavement Register. Tag matches `DECEASED_SUSPECTED`, exclude from all channels, route to reception to confirm.
- [ ] Re-screen the 12-36m bands before each postal campaign, not only once.
- [ ] Thank-you cards (address confirmed at collection) can bypass the cleanse but not the `ADDRESS_BAD` exclusion.

# Handoff: postal address in the recall feed

Merged to `main` on winstanleyandson/winstanleyandson.github.io on 7 September 2026.
Status: built and published in the repo, not yet wired to live systems. Nothing here has touched GHL, Make or Stannp.
The `/book/` redirect is live on the website via GitHub Pages; verify it resolves before any letter is printed.

## What exists

| File | What it is |
|------|------------|
| `address_audit.py` | Run against the VisionPMS export to get postcode completeness by recall band. Tested on synthetic data only. |
| `README.md` | Field mapping (VisionPMS -> GHL native address fields), sync rules, dialer letter fallback, pre-send checklist, house style. |
| `letters/recall-letter.html` | Branded A4 letter for due30 / 0-6m / 6-12m. Plain, local voice. |
| `letters/cold-reactivation-letter.html` | Branded A4 letter for 12-24m / 24-36m. |
| `letters/*.md`, `letters/*-preview.png` | Plain copy and rendered previews of the two letters. |
| `automation/make-visionpms-ghl-sync.blueprint.json` | Importable Make scenario: parse export, validate postcode, band, look up GHL contact, skip address overwrite when `address_bad` / `address_corrected`, upsert otherwise. |
| `automation/ghl-workflows.md` | Build sheet for three GHL workflows, custom fields, tags, custom values, and a test plan. |
| `automation/stannp-send-letter.json` | Webhook body GHL sends to Stannp. |
| `/book/index.html` (site root) | Redirect to the GHL booking widget with UTM tags. Both letters print this URL. Goes live on merge to main. |

## Decisions already made

- Native GHL address fields, not custom fields.
- VisionPMS is address truth, one-way sync, except records tagged `address_bad` or `address_corrected` which are skipped and raised as a task.
- Failed phone call in the Power Dialer triggers a letter automatically if the address is usable.
- No letter to any contact tagged `deceased_suspected`, `dnc_post`, `address_incomplete`, or with a letter in the last 90 days.
- Cold bands (12-36m) get a PAF cleanse and deceased screening before any postal send.
- Gavin Winstanley is described as "Frame maker", never optician.

## Still needed from the practice (nothing below depends on anything else)

1. The VisionPMS export, or a header-only sample. Unblocks the audit and the column names in the Make blueprint (modules 2, 3, 7, 8).
2. GHL private integration API key + location ID, set as Make scenario variables `GHL_API_KEY`, `GHL_LOCATION_ID`.
3. Stannp account on the EU platform (see chat instructions), API key stored as GHL custom value `stannp_api_key`, and the two template IDs after uploading the HTML letters.
4. Where the weekly export lands (email / Drive / manual). Decides the trigger module in the blueprint; currently a webhook.
5. Power Dialer disposition names, to map to `phone_bad`, `phone_unreached`, `dnc_phone`, `letter_requested`.
6. Signatory name and role for each letter (custom values `letter_signatory_name`, `letter_signatory_role`).
7. Check winstanleyandson.co.uk/book redirects to the GHL calendar (already deployed).

## Order of work once inputs arrive

1. Run `address_audit.py` on the export. If cold bands are under ~70% valid postcode, cleanse before building the cold campaign.
2. Fix column names in the blueprint, import into Make, run once in test against a handful of test contacts.
3. Create custom fields, tags and custom values in GHL per `ghl-workflows.md` section 0.
4. Upload letters to Stannp; if Stannp rejects `{{contact.x}}` tags, rename to Stannp's `{{firstname}}` style in both HTML files.
5. Build workflow 1 (dialer -> letter) with Stannp `test=1`. Proof both letters on paper.
6. Build workflow 2 (returned mail). Run the test plan in `ghl-workflows.md`.
7. Deceased screening + PAF cleanse of the full file. Then workflow 3 (cold campaign).
8. Flip Stannp `test` to `0`. Go live.

## Known gaps

- The blueprint's postcode check is a length/first-letter test because Make lacks regex in filters. The Python script has the full UK pattern; run the audit for the real numbers.
- Make's HTTP modules call GHL API v2 directly. If the practice prefers Make's native GHL app, swap modules 4, 6, 7, 8.
- Template previews render in Georgia; live templates load Cinzel and Cormorant Garamond from Google Fonts. Check Stannp's renderer allows external fonts, otherwise embed them.

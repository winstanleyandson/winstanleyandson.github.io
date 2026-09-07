# Handoff: postal address in the recall feed

Merged to `main` on winstanleyandson/winstanleyandson.github.io. Last updated 7 September 2026.
Status: letters are now direct-response copy with a real offer, built and pushed. A Stannp account
exists (EU platform) and is mid-setup. Nothing has touched GHL or Make yet.
The `/book/` redirect is live on the website via GitHub Pages; verify it resolves before any letter is printed.

## Since the last handoff

- Both letters were rewritten from a plain reminder notice into direct-response copy
  (Hormozi/Kennedy style, at the user's request): a headline, a reason it matters, a
  concrete offer with a real dated deadline (`{{contact.letter_expiry_date}}`, set by the
  sending workflow to send-date + 14 days, never typed by hand), three ways to book, and a
  P.S. restating the offer.
- **Offer, both letters (finalised, matches):** free 1.6 high-index lenses (25% thinner,
  normally £65) + premium anti-glare coating (normally £45), worth over £110 together, on
  any pair ordered before the deadline. The cold letter adds one more line: 50% off the
  eye test when ordering glasses, worth £22.50. Deliberately kept to two or three items,
  not a long stack, first draft, and the user pulled it back, "the stack is crazy, just do
  the 1.6 and HMC". No cash discount anywhere, the user's steer was explicit: a stack of
  real product costs less to deliver than its price tag and doesn't train people to wait
  for a discount the way cash off does.
- **All £ values in the offer are still placeholders I chose to sound plausible.** They
  have not been confirmed against real pricing. This must be signed off by whoever prices
  jobs before the first live send, flagged in `letters/README.md`.
- Layout bug found and fixed: both letters were quietly spilling onto a mostly-blank
  second page. The screenshots used for review were rendered at a tall, non-A4 window and
  looked fine, but the actual print output was 2 pages. Fixed by tightening line-height,
  margins and the offer box CSS, and re-verified against true PDF page-object counts, not
  screenshots, both are confirmed single A4 pages now. If you touch the copy again, check
  page count with a real print render, not a screenshot at an arbitrary window height.
- Gavin is never described as "optician", only "Frame maker". Confirmed nowhere in the
  templates, previews or custom-value docs.

## Stannp account status (as of this handoff)

- Account created on the **EU platform** (`app-eu1.stannp.com`), correct for UK postage.
- Subscribed to a plan (Starter, £12/mo, discussed) to unlock API access.
- **An API key was generated and pasted into this chat.** I could not use it, my sandboxed
  environment blocks outbound calls to arbitrary hosts and Stannp is not on the allowlist,
  so the key was never sent anywhere by me. But it is sitting in this conversation's
  history in plain text. **Treat it as compromised: go to Settings -> API in Stannp and
  regenerate it before using it for anything real.** Only use API keys in a local terminal
  or a secrets manager from here on, never paste them into chat.
- Templates have **not** been uploaded yet. That step could not be done via API with
  confidence (template creation isn't a documented flow I could verify), so it still needs
  the UI: Campaigns -> (new campaign) -> Design step -> upload HTML, or a dedicated
  Templates area if the account has one. Two templates needed, one per letter file.
- Once template IDs exist, a single letter can be tested via
  `POST https://api-eu1.stannp.com/v1/letters/create` with `-u "<key>:"`, `template=<id>`,
  `test=1`, and the `recipient[...]` fields, run from the user's own machine. `test=1`
  returns a proof without posting anything, flip to `test=0` only once both letters are
  proofed on paper.

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
3. **Regenerate the Stannp API key** (see above), then upload the two letter templates via the Stannp UI and send back the two template IDs. Store the new key as GHL custom value `stannp_api_key`, never in chat.
4. Where the weekly export lands (email / Drive / manual). Decides the trigger module in the blueprint; currently a webhook.
5. Power Dialer disposition names, to map to `phone_bad`, `phone_unreached`, `dnc_phone`, `letter_requested`.
6. Signatory name and role for each letter (custom values `letter_signatory_name`, `letter_signatory_role`). Never "optician" for Gavin.
7. Check winstanleyandson.co.uk/book redirects to the GHL calendar (already deployed).
8. **Sign-off on the offer values**: £65 lenses, £45 coating, £22.50 half-price eye test. Placeholders, not real pricing, confirm with whoever prices jobs before anything goes to print.

## Order of work once inputs arrive

1. Run `address_audit.py` on the export. If cold bands are under ~70% valid postcode, cleanse before building the cold campaign.
2. Fix column names in the blueprint, import into Make, run once in test against a handful of test contacts.
3. Create custom fields, tags and custom values in GHL per `ghl-workflows.md` section 0, including `letter_expiry_date` (date, set by the send step to today + 14 days on every send, see section 0 note added this round).
4. Regenerate the Stannp key, upload both letters via the UI, note the two template IDs. If Stannp rejects `{{contact.x}}` tags on upload, rename to Stannp's own merge syntax in both HTML files, then regenerate the `.md` copies from the HTML (see the inline python approach used in this session, `re.sub` on the `.ways` blocks) rather than hand-editing them out of sync.
5. Test-send both letters with `test=1` from a local terminal (command in this doc's Stannp section above), confirm merge fields and layout are correct, then proof on paper before flipping to `test=0`.
6. Build workflow 1 (dialer -> letter) in GHL per `automation/ghl-workflows.md`.
7. Build workflow 2 (returned mail). Run the test plan in `ghl-workflows.md`.
8. Deceased screening + PAF cleanse of the full file. Then workflow 3 (cold campaign).
9. Flip Stannp `test` to `0` in the live GHL webhook. Go live.

## Known gaps

- The blueprint's postcode check is a length/first-letter test because Make lacks regex in filters. The Python script has the full UK pattern; run the audit for the real numbers.
- Make's HTTP modules call GHL API v2 directly. If the practice prefers Make's native GHL app, swap modules 4, 6, 7, 8.
- Template previews render in Georgia; live templates load Cinzel and Cormorant Garamond from Google Fonts. Check Stannp's renderer allows external fonts, otherwise embed them.

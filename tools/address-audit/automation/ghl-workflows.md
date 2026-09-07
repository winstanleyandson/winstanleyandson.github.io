# GHL build sheet: letter automation

Three workflows plus the custom fields and tags they rely on. Build in this order.

## 0. Custom fields, tags, custom values

Custom fields (Contact): `visionpms_id` (text), `last_exam_date` (date), `months_since_exam` (number),
`recall_band` (text), `address_synced` (date), `last_dialer_outcome` (text), `last_dialer_date` (date),
`address_validated` (date).

Tags: `address_bad`, `address_corrected`, `address_incomplete`, `deceased_suspected`, `dnc_post`,
`dnc_phone`, `phone_bad`, `phone_unreached`, `letter_requested`, `letter_sent`.
GHL lower-cases tags; the docs elsewhere in this folder use upper case for readability only.

Custom values (Settings > Custom Values): `stannp_template_recall`, `stannp_template_cold`,
`letter_signatory_name`, `letter_signatory_role`.

## 1. "Dialer outcome → letter"

Trigger: **Contact Tag Added**, any of `phone_bad`, `phone_unreached`, `dnc_phone`, `letter_requested`.
Attach the same tags to Power Dialer dispositions: Number not in service → `phone_bad`;
Wrong number → `phone_bad`; No answer (3rd attempt) → `phone_unreached`; Do not call → `dnc_phone`;
Send letter → `letter_requested`.

Steps:
1. Update contact field `last_dialer_outcome` = trigger tag, `last_dialer_date` = now.
2. If tag is `phone_bad`: create task "Phone number not working - check with patient" assigned to reception.
3. If/Else **"Can we post?"**: `postal_code` is not empty AND does not have tag `address_bad`
   AND not `deceased_suspected` AND not `dnc_post` AND not `address_incomplete`.
   - No → create task "Phone failed and no usable address - unreachable, check record". End.
4. If/Else **"Sent recently?"**: has tag `letter_sent` AND `letter_sent_date` within last 90 days → End.
5. If/Else on `recall_band`:
   - `due30`, `0-6m`, `6-12m` → Webhook (stannp-send-letter.json, template = `stannp_template_recall`).
   - `12-24m`, `24-36m` → Webhook (template = `stannp_template_cold`).
   - anything else → task "Band unknown, decide manually".
6. Add tag `letter_sent`, set `letter_sent_date` = now, add note "Letter sent: <template name>".

## 2. "Returned mail"

Trigger: **Contact Tag Added** `address_bad`.
1. Remove from any active postal campaign (Remove from workflow: "Cold recall postal").
2. Create task "Letter returned - confirm address with patient, update VisionPMS, then remove address_bad".
3. Nothing else. The Make sync sees the tag and skips the address overwrite.

## 3. "Cold recall postal" (scheduled campaign, run after PAF cleanse + deceased screening)

Trigger: manual / bulk action from a smart list.
Smart list: `recall_band` in (12-24m, 24-36m) AND `address_validated` within last 180 days AND
no tags `address_bad`, `deceased_suspected`, `dnc_post`, `address_incomplete`, and `letter_sent`
older than 90 days or absent.
Steps: Webhook with `stannp_template_cold`, then tag `letter_sent` and set `letter_sent_date`.
Add a 5-minute wait between batches of 50 so Stannp rate limits are not hit.

## Stannp webhook (for step 1.5 and workflow 3)

Method POST, URL `https://api-eu1.stannp.com/v1/letters/create?api_key=<KEY>`, body from
`stannp-send-letter.json` as form fields. Stannp will merge `recipient[...]` values into the
uploaded HTML template; rename the template merge tags to match (`{{firstname}}`,
`{{last_exam_date}}` etc.) when uploading, since Stannp does not read GHL's `{{contact.x}}` syntax.
For Scribeless (handwritten), the same fields go to their `/v1/letters` endpoint.

## Test plan before going live

1. Create a test contact with your own address, band `0-6m`, tag `phone_bad`. Expect a task and,
   with `test=1` in the Stannp body, a proof PDF but no post.
2. Add `address_bad` to that contact, re-run the Make sync. Expect a reception task and no address change.
3. Remove `address_bad`, re-run the sync. Expect the VisionPMS address to come back.
4. Flip `test` to `0` only after both letters have been proofed on paper.

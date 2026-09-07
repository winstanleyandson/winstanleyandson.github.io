# Letter templates

Print-ready A4 templates in the current brand (green/gold crest, Cinzel wordmark,
Cormorant Garamond body, parchment call-out): `recall-letter.html` and
`cold-reactivation-letter.html`. The `.md` files hold the plain copy; the `.png` files
are rendered previews with sample data. Paste the HTML into the Stannp or Scribeless
template editor; the fonts load from Google Fonts and fall back to Georgia. The address
block sits at 20mm left / ~46mm top to suit a standard C5 window envelope.

Merge fields used: contact.first_name, last_name, address1, city, postal_code, phone,
last_exam_date, months_since_exam; right_now.date; practice.signatory_name,
practice.signatory_role.

| File | Bands | Trigger |
|------|-------|---------|
| recall-letter.md | due30, 0-6m | weekly recall postal, or dialer fallback |
| cold-reactivation-letter.md | 12-24m, 24-36m | dialer fallback, or scheduled cold campaign after PAF cleanse and deceased screening |

Both letters:
- Use GHL native merge fields for name and phone; `last_exam_date` and `months_since_exam`
  need to exist as custom fields populated by the weekly sync.
- Reference the phone failure ("we tried to call") so patients understand why a letter
  arrived. For a scheduled send with no dial attempt, delete that sentence.
- Carry an opt-out line. Returned letters or "no further contact" replies go to reception,
  who tag `ADDRESS_BAD` or `DNC_POST` as appropriate.
- Reference `winstanleyandson.co.uk/book`; this path needs to redirect to the GHL booking
  widget before the first send. Check that exists.

6-12m has no dedicated letter: use the recall letter with the "now due" line softened to
"is overdue".

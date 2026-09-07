# Letter templates

Print-ready A4 templates in the current brand (green/gold crest, Cinzel wordmark,
Cormorant Garamond body, parchment call-out): `recall-letter.html` and
`cold-reactivation-letter.html`. The `.md` files hold the plain copy; the `.png` files
are rendered previews with sample data. Paste the HTML into the Stannp or Scribeless
template editor; the fonts load from Google Fonts and fall back to Georgia. The address
block sits at 20mm left / ~46mm top to suit a standard C5 window envelope.

Merge fields used: contact.first_name, last_name, address1, city, postal_code, phone,
last_exam_date, months_since_exam, letter_expiry_date; right_now.date;
practice.signatory_name, practice.signatory_role.

## Style: direct response, not a reminder note

Both letters lead with the offer, not the appointment. Headline, a short reason it matters,
the offer as a bulleted stack with a deadline, three ways to book, then a P.S. that repeats
the deadline. This is deliberate: a plain recall notice gets filed, an offer with a real
expiry date gets acted on.

**The offer must be real.** `letter_expiry_date` is set by the sending workflow, not typed
by hand, so it's always send date + 14 days and never stale. Don't shorten the window for
effect, and don't send the same offer twice to someone who let the first one lapse without
checking with reception first, repeated "deadlines" that aren't real is what turns a good
letter into junk mail.

- Recall letter offer: free anti-glare/anti-scratch upgrade (normally £89) on any pair
  ordered before the deadline.
- Reactivation letter offer: £40 off the next pair, any frame, any lens.

Both are placeholder amounts. Confirm the real margin on these before the first live send,
lens upgrades and frame discounts need sign-off from whoever prices jobs, not a copywriter.


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

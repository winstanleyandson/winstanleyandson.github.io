# Business context: Winstanley & Son Opticians (for AI-account design)

Independent optician and bespoke frame maker at 252 Park Road, Dingle, Liverpool L8 4UE, trading since 1998.
Owner-operator is Gavin Winstanley. House rule: Gavin is never described as "optician", only "Frame maker".
Phone 0151 726 0622. Email help@winstanleyandson.co.uk. Open Mon-Fri 9-5, closed weekends.
5.0 stars from 213 Google reviews. Serves Dingle, Toxteth, Aigburth and south Liverpool.

## What they sell
- Varifocals (the flagship): Essilor Varilux, Nikon, Zeiss, Hoya. Measured on the Essilor Visioffice X, "never a felt-tip pen". Lenses from £205. Usually ready within 48 hours.
- Private and NHS eye examinations (free NHS tests for those who qualify, including children). Stellest myopia-control lenses for children.
- Same-day single-vision glasses from stock lenses. Reglazes into the customer's own frames.
- Bespoke handmade frames cut from Italian Mazzucchelli acetate, about four weeks, three-year guarantee. "The only bespoke frame makers in Merseyside."
- Repairs, prescription sunglasses, Transitions, computer/office glasses, 0% finance over six months.
- Frames: Tom Ford, Giorgio Armani, Ray-Ban and their own handmade range.

## Existing tech and systems (what AI accounts would plug into)
- Website: static HTML on GitHub Pages (this repo), ~45 landing pages + a /guides/ section of long-form SEO articles, llms.txt, sitemap.xml. Pages are hand-maintained HTML with a shared style.css. Commits are small and frequent ("Quick facts + wording").
- GoHighLevel (GHL): CRM, booking widget (api.leadconnectorhq.com), power dialer for recall calls, workflows, tags, custom fields.
- VisionPMS: practice management system, source of truth for patient records and recall dates. Weekly export -> GHL via a Make scenario (one-way sync).
- Make (make.com): automation scenarios (VisionPMS -> GHL sync blueprint exists in tools/address-audit/automation).
- Stannp (EU platform): direct-mail letters. Two direct-response recall letters exist (recall-letter.md, cold-reactivation-letter.md) with a real dated offer. API key was previously leaked into a chat and must be regenerated.
- Social: /social/2026-09 and /social/2026-10 hold ~90 generated "card" PNGs, product/workshop photos and short vertical videos (same-day Italy video etc.). Content is produced in monthly batches.
- Reviews page, Glasses Club (membership/offer page), varifocal offer landing pages with calendar booking.
- Python tooling: tools/address-audit/address_audit.py (postcode completeness by recall band).

## Existing documented workflows (from tools/address-audit)
- Recall: dialer disposition -> tag -> letter workflow (gate on postal quality; exclusions address_bad, deceased_suspected, dnc_post).
- Pre-send checklist: PAF cleanse, deceased screening, re-screen before each campaign.
- House style for letters: direct-response (Hormozi/Kennedy), a real offer with a dated deadline, product value not cash discounts, "the stack is crazy, just do the 1.6 and HMC".
- Secrets never pasted into chat; API keys only in a local terminal or secrets manager.

## Recurring jobs an AI team could own
1. Patient recall and reactivation (phone, SMS/email via GHL, letters via Stannp), respecting tags and exclusions.
2. Website content: new landing pages and guides, quick-facts wording updates, FAQ schema, sitemap and llms.txt upkeep, internal links.
3. Social content: monthly batches of cards, reels and captions from workshop photos and customer videos; posting schedule.
4. Reviews: requesting, monitoring and replying to Google reviews; turning reviews into site and social content.
5. Bookings and front-desk: answering common questions (prices, NHS eligibility, parking, same-day), routing to the booking widget, reminders and no-show follow-up.
6. Supplier and lab ordering: Essilor/Nikon/Zeiss/Hoya orders, bespoke frame job tracking (four-week pipeline).
7. Data hygiene: VisionPMS export audit, address/postcode repair, GHL field mapping, weekly sync checks.
8. Owner's advisory: pricing offers, campaign decisions, "roast my plan" style pressure-testing before spending money.

## Constraints and tone
- Plain English, Liverpool-local, honest comparison style (see "Independent opticians vs the big chains" guide). No hype.
- UK spelling. NHS rules must be stated accurately (free tests for under-16s, 16-18 in full-time education, over-60s, diabetics, glaucoma risk, certain benefits/HC2).
- Patient data is sensitive (UK GDPR). Exports are never committed to the repo. AI accounts must never see or store full patient lists in chat.

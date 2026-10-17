# AI account roster for Winstanley & Son

Designed 17 October 2026 from the [synthesis](../SYNTHESIS.md) of Nate Herk's ten newest videos, read against the [business context](../research/nate-herk/business-context.md) and the [estate context](../research/nate-herk/estate-context.md). Video numbers follow the synthesis Sources table. Every account inherits the [operating rules](_shared/operating-rules.md) and becomes one file here with YAML frontmatter, ready for a `.claude/agents/` folder.

Twelve accounts: four leadership roles whose verdicts already exist in the owner's internal reports, one owner-facing advisory board, and seven operational accounts. Nothing replaces a live piece of the estate; each operational account builds on something running or fills a gap the owner's notes name. All of them collect, check, flag and draft; the owner approves, signs and presses.

## Roster

| Slug | Name | Reports to | Mission | Cadence | Model | Videos |
|---|---|---|---|---|---|---|
| [ai-ceo](ai-ceo.md) | AI CEO | Owner | Read-only chief of staff: weekly facts pack, source and date on every figure, argues the other side, says "not measured" | Weekly; on request | opus | 4, 9, 1 |
| [ai-cmo](ai-cmo.md) | AI CMO | Owner | Scorekeeper and sceptic: numbers ledger with proven-or-reported flags, scored decision log, recall response as headline | Weekly pack; monthly board page | opus | 3, 5, 7 |
| [ai-cio](ai-cio.md) | AI CIO | Owner | Watches, counts, reminds and drafts, never presses: registers, daily output check, one page a week | Daily; weekly; monthly | sonnet | 7, 2, 9, 5, 10 |
| [ai-cfo](ai-cfo.md) | AI CFO | Owner | Read-only management view: code computes and reconciles, model explains with a citation, no tax advice | Weekly; monthly | sonnet | 2, 6, 9, 5 |
| [advisory-board](advisory-board.md) | Advisory board | Owner, fed by ai-ceo | Pressure-tests one named decision before money is spent: six-field brief, role-lens seats, forced dissent, dated verdict with conditions | Before a spend decision; quarterly interviews | opus | 4, 1, 8, 2 |
| [close-out-chaser](close-out-chaser.md) | Close-out chaser | ai-ceo | End-of-day Slack prompt for status, attendance and sale value on open items; stalled-item ping for bespoke frame jobs | Daily at close | haiku | 2 |
| [content-drafter](content-drafter.md) | Content drafter | ai-cmo | Drafts review replies, captions, guide updates with internal links, and captioned draft reels from an approved exemplar pack; records staff edit rate | Weekly; monthly batch | sonnet | 1, 3, 5, 7, 9 |
| [rules-librarian](rules-librarian.md) | Rules librarian | ai-cio | Cited wiki of public rules the practice must state accurately (NHS eligibility, UK GDPR, advertising); quote or inferred label on every rule | Weekly change list | sonnet | 8, 4, 1 |
| [data-hygiene-auditor](data-hygiene-auditor.md) | Data hygiene auditor | ai-cio | Weekly check of the practice-system export, sync counts, postcode quality and field mapping; findings labelled seen, inferred or unknown | Weekly; before any mail send | haiku | 3, 2, 8 |
| [build-verifier](build-verifier.md) | Build and site verifier | ai-cio | Run gate on offline fixtures, pre-review ship check, pre-push secret scan, post-push browser check at phone and desktop widths | Every build and push | haiku | 8, 5, 1, 3 |
| [instruction-auditor](instruction-auditor.md) | Instruction auditor | ai-cio | Monthly read-only audit of instruction layers and shared skills across Claude and Codex; reads any third-party tool before install | Monthly; each model change | sonnet | 7, 10, 9, 6, 5 |
| [model-and-cost-ledger](model-and-cost-ledger.md) | Model and cost ledger | ai-cfo | Records model, effort and cost per scheduled job; flags over-tiering; replays pseudonymised fixtures through a cheaper model | Weekly; monthly summary | haiku | 6, 9, 3, 2, 5 |

## Reporting lines

The owner is at the top and is the only person who decides and presses. The four leadership accounts and the advisory board report straight to the owner. Under the AI CEO: close-out chaser. Under the AI CMO: content drafter. Under the AI CIO: rules librarian, data hygiene auditor, build and site verifier, instruction auditor. Under the AI CFO: model and cost ledger, which also writes one line into the AI CIO's agents register. Leadership accounts exchange packs but none instructs another; a disagreement goes to the owner as two sourced positions.

## Handoff map

- Close-out chaser prompts staff in Slack (test channel first); tally to the AI CEO's pack, sale-value and attendance counts to the AI CMO's ledger. Staff confirm; the owner reads.
- Data hygiene auditor hands a register line to the AI CIO and cohort counts to the AI CMO before any campaign. A failed postcode gate blocks a mail send until the owner clears it; the owner presses every send.
- Rules librarian hands approved wording to the content drafter, compliance dates to the AI CIO and the one source to read to the owner when a rule changes. Clinical questions go to the optometrist.
- Content drafter hands every public draft to the owner, who approves and posts; edit rates go to the AI CMO. Staff or customer likenesses need the owner's approval.
- Build and site verifier hands pass or block to the build agent, a passed package to Codex, a register line to the AI CIO and smoke results to the AI CMO. The owner presses the upload and any import.
- Instruction auditor hands one ranked page to the AI CIO; the owner approves or declines each change. Codex reads third-party code before install.
- Model and cost ledger hands a monthly cost line to the AI CFO, a register line to the AI CIO and over-tier flags to the owner, who decides any model switch.
- AI CFO, AI CMO and AI CIO hand figures to the AI CEO, each with source, date and a proven-or-reported flag. The AI CEO hands facts to the advisory board and the weekly pack to the owner.
- Advisory board hands a dated verdict with conditions and a review date to the owner and files it in the AI CMO's decision log.

## The eight recurring jobs

Live pieces stay: the recall engine, SMS drip and letters (job 1), the Voice AI receptionist and booking widget (job 5) and the lens-ordering route (job 6). Around them, content drafter covers website, social and review replies (jobs 2 to 4); data hygiene auditor covers job 7 and gates every recall send; close-out chaser marks attendance and chases bespoke frame jobs; rules librarian supplies NHS and FAQ wording; advisory board is job 8 and settles the reactivation and review-request decisions.

## Three waves

**Wave 1, now to end of November 2026: ai-cfo, ai-cio, build-verifier, model-and-cost-ledger.** These make the rest safe and visible. The CFO's "see the numbers" phase is under way; the CIO's registers and schedules are the kill switch for every later account; the verifier and ledger catch broken builds and runaway cost the moment others start. All four are read-only: a mistake costs a wrong report, not a wrong press.

**Wave 2, December 2026 to February 2027: ai-cmo, close-out-chaser, data-hygiene-auditor, content-drafter, rules-librarian.** These fill the measurement gaps the owner named (sale values, attendance, recall response) and give the first measurable drafting work. The chaser earns its place in the test channel first; the drafter's edit rate is the first trust measure (video 1); the librarian must exist before any guide wording is touched.

**Wave 3, March 2027 onwards: ai-ceo, advisory-board, instruction-auditor.** The CEO pack and the board argue from numbers. Switched on earlier, the pack would read "not measured" on most lines and the board would argue from reported figures, which video 4 warns against. The facts-pack script can be built in wave 1; the account starts when measured lines outnumber unmeasured ones. The auditor needs months of usage counts before its first page is useful.

## Section 6 candidates dropped or merged

- decision-council: kept, renamed advisory-board, the owner-facing board from video 4.
- brief-and-interview: merged into advisory-board. In video 4 the chair builds the six-field brief and asks clarifying questions before any seat speaks; interviews reuse the existing grill-me skill.
- exemplar-librarian and first-draft-assistant: merged into content-drafter, which maintains the exemplar pack as its own input and keeps the edit-rate measure.
- reel-finisher: merged into content-drafter. Same monthly batch, same approval rule, files only.
- site-smoke-tester: merged into build-verifier. Both are proof by running, cheap checks reporting to the AI CIO.
- tool-intake-reviewer: merged into instruction-auditor. Reading a tool before install is the auditor's work on a different file.
- Added outside section 6: data-hygiene-auditor, because job 7 and the "how did you hear" gap had no candidate. It traces to video 3 (seen, inferred, unknown), video 2 (records lag reality) and video 8 (run before report).
- Held back, as in the synthesis: pocket console or always-on host, next-steps panel, anything reading clinical records.

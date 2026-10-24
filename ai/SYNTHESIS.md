# Synthesis: Nate Herk's seventeen newest videos, read for Winstanley & Son

Written 17 October 2026 from the ten verified summaries in `ai/videos/` (videos published 2 to 16 October 2026), with an addendum the same day for videos 11 to 15 (28 September to 2 October 2026) in section 8 and a second addendum on 24 October 2026 for videos 16 and 17 (19 and 22 October 2026) in section 9, with `research/nate-herk/business-context.md` and `estate-context.md` as the yardstick. A citation such as [V7 7:04] means video 7 in the Sources list, at the timestamp the summary gives; timestamps are caption-block starts and can sit up to a minute off. This is raw material for the roster designers, not the roster. Nothing here was checked against the videos themselves, only against the summaries.

## 1. What the first ten videos add up to

Across one fortnight the channel describes a single working method from several angles. An agent is a folder of plain files: a short routing file, skills that are recipes corrected after each run, and a knowledge folder. Quality comes from showing the agent a finished example or a countable finish line, from keeping instructions to what the model cannot infer, and from forcing proof before the agent may say it is done: a run, a screenshot, a real browser click. Around that core sit three experiments: a panel of sub-agents that argue a decision, an expert clone compiled from public material into a cited wiki, and small interface mods that surface hidden state. Two videos are sponsored or partnered tours of hosted products and one covers a Grok Bot update; in each Nate concedes that the product removes plumbing rather than adding a capability he could not get before [V2 20:39].

For Winstanley & Son most of the method is already live: the router CLAUDE.md, shared skills, grill-me, the five-stage change gate, the isolated test channel and the rule that agents draft while the owner presses. What the videos sharpen is specific: a propose-first audit on a schedule, a six-field decision brief with forced dissent, a quote-or-inferred rule for any knowledge base, a run gate for build agents, a browser check after every site push, and a written record of which model ran which job at what cost. What they do not supply is any reason to move work onto a hosted third-party platform or to loosen the owner-presses rule.

## 2. Cross-video themes

### 2.1 A finished example beats a description

Claim: an agent does its best work when pointed at a concrete example or finish line, and generic work when handed a vague goal.

Support: V3 Reverse Engineer Anything [2:25]: an existing app is a more specific requirements document than one you would type, and a Friday report skill should study five good Friday reports; thirty top reels became an editing skill [0:48]. V1 Matt Pocock [4:24]: tell the agent what you care about; his largest gain came from letting it click through and screenshot its own output [32:52]. V7 Context engineering [1:34]: define done by outcome, reason and constraints. V4 Roast Room [11:02]: the brief needs real numbers, limits and a definition of success. V9 Codex [7:10]: countable finish lines beat subjective ones.

Hedge: V3's with-and-without comparison is one anecdote with no timings [12:45], and V3 itself calls REA a framework, not a new technique [4:48].

Evidence: practitioner opinion throughout; nothing is measured.

### 2.2 Smallest sufficient context, routed rather than piled

Claim: instructions should hold only what the model cannot infer, in a short routing file that points to deeper material loaded on demand.

Support: V7 Context engineering: Anthropic cut over 80% of Claude Code's own system prompt [0:00]; keep voice, goals, audience and intent, drop what can be looked up [5:35, 6:22]; CLAUDE.md as a starting point with pointers [6:22]. V9 Codex [2:23, 3:10]: AGENTS.md as a routing map. V5 Six repos [4:45]: context rot, so the plan lives in files and a fresh session resumes. V10 Mods [3:57]: hand off before the cache lapses. V4 Roast Room [7:52]: a thin agent file routes to a knowledge folder only when needed.

Disagree: V5 praises a spec step that surfaces edge cases and doubles as a client document [5:33]; V1's Pocock says keeping specs as the main artefact made his code and agent output worse over months [27:17]. V8 builds a 700,000-word corpus [3:10] in the same fortnight V7 says to cut.

Evidence: the 80% figure and the tool-loading figures are Anthropic reporting on its own product [V7 0:00, 2:22]; the 2025 paper is real but ran on older models, as Nate cautions [V7 2:22]; his own comparison is one run judged by him [V7 4:13].

### 2.3 Proof by running, not by the agent's word

Claim: an agent saying something works is not evidence; a run, a screenshot, a real browser click or a labelled finding is.

Support: V8 Expert clone [7:08]: a hook blocks the final answer until written code has run; predict, run, compare, show the broken version [7:56]; a script that worked in one terminal only [8:43]. V5 Six repos [7:54]: Claude reporting that a feature works is not proof, so Playwright CLI clicks like a customer. V1 Pocock [4:48]: tests raise the floor more than a model change. V3 REA [9:34, 10:21]: tag findings seen, inferred or unknown, then rebuild and test. V6 Grok Bot [3:58]: a bot does not always know how it works. V10 Mods [8:40]: Goal Meter shows Claude's own task list, which is not proof.

Hedge: V8 shows no side-by-side against ordinary Claude; V1's claim is one developer's experience.

Evidence: demonstration and opinion; V5's point that a command-line tool costs fewer tokens than an MCP is echoed by the Playwright README [7:54].

### 2.4 Match model and effort to the step, and see the cost

Claim: model and effort are cost dials to set per step, record and keep visible, not leave to a hidden router.

Support: V9 Codex [16:41, 19:04]: the top model at high effort is overkill for an email; middle tier at medium for knowledge work; cheaper subagents in parallel [28:34]. V1 Pocock [32:05]: Opus 5.5 at medium, maybe lower, once tests exist. V6 Grok Bot [4:35, 6:20]: split a seven-job skill by the model each step needs, and pin and see the model per skill, which routing hides [0:47]. V3 REA [11:58]: saved evidence may let a cheaper model do the build. V2 Kylon [15:52]: usage by person, room and agent. V5 Six repos [8:41]: token-saver add-ons delivered far less than claimed, and a spend tracker flags an unused MCP loading on every message. V4 Roast Room [7:04]: sub-agents cheaper than agent teams. V10 Mods [3:10]: cache age and API-equivalent cost on screen.

Disagree: V6 complains that routing is opaque yet prefers Grok Bot and uses it daily [8:41]; V2 recommends hosted tiers that also route [12:55].

Evidence: V9's cost figures are self-reported [17:28]; V5's savings come from a JetBrains test Nate cites [8:41]; V2's tier ratios are relayed from the sponsor; V4's cost comparison is unmeasured.

### 2.5 Interview first, then write the brief

Claim: nobody knows their requirements in full, so the agent should question the human before building or deciding, and the result should be a written brief.

Support: V1 Pocock [15:59]: grill me surfaces unknown unknowns such as security and deployment; one shared vocabulary across code, product and client [22:27]. V4 Roast Room [11:02, 11:50]: a six-field brief of decision, options, numbers, limits, success and current lean, with the chair asking clarifying questions first. V2 Kylon [10:21, 19:04]: onboard an agent with a Markdown brief from your existing setup, and tell it your tools, pain points and roles. V5 Six repos [5:33]: the spec step surfaces double bookings, refunds and time zones.

Hedge: V6's AI OS kit also interviews you, but it is Nate's own lead magnet [4:08].

Evidence: practitioner opinion; V1 cites The Pragmatic Programmer without the summary checking the book [15:59].

### 2.6 Cited knowledge: a quote or a label on every rule

Claim: compiled knowledge is safe to lean on only when each rule carries an exact quote and source, or is marked as inferred.

Support: V8 Expert clone [5:33, 6:20]: every rule needs an exact quote and origin, or an inferred label; raw files stay untouched and a wiki with index and log is compiled over them [3:58]; one new link updates the affected pages and promotes a one-source rule only on a second source [9:31]. V4 Roast Room [7:52, 10:15]: adviser brains with a decision-rules sheet and a source list, built by research agents from public material. V1 Pocock [7:15]: his teach skill fetches primary sources with quotes and links, then he reads the source himself. V3 REA [9:34]: seen, inferred, unknown. V7 Context engineering [10:17]: only three of 25 script folders had a sources file, so the next step re-verified everything.

Disagree: V7 argues for less context while V4 and V8 compile corpora of over a million words [V4 7:52]; both reconcile through thin routing files, but neither measures the trade-off.

Evidence: the wiki pattern is Karpathy's, dated to April 2026 by secondary write-ups only [V8 3:58]; the closing line on outsourcing thinking has no primary source [V8 10:20]. Neither V4 nor V8 discusses copyright or terms for compiling a named person's material.

### 2.7 Structured dissent, judgement kept

Claim: one model agreeing with itself is a warning sign, so dissent must be designed in and the human must still understand the answer.

Support: V4 Roast Room [2:20]: unanimity in round one is treated as a warning and two seats are told to argue the other option; three rounds with scores [6:17]; outsource the thinking but not the understanding [12:37]. V8 Expert clone [10:20]: the same line attributed to Karpathy. V1 Pocock [7:15]: do not trust what agents teach you; he is also excited by agents that argue for doing things properly [41:31].

Hedge: whether the advisers really disagree is open, and the demo verdict backed the unanimous option anyway [V4 2:20, 3:55]; the preference for sub-agents over agent teams is unmeasured [V4 7:04]; a viewer argues seven seats on one model are one training echoing itself.

Evidence: demonstration and opinion.

### 2.8 Shared, always-on and remotely steered agents

Claim: the step after a personal setup is agents that colleagues can reach, that keep running when a laptop is shut, and that can be steered from a phone.

Support: V2 Kylon [0:00, 16:39]: humans and agents in shared rooms, teammates messaging each other's Claude Code; local agents go quiet when the machine is off [14:17]; an end-of-day check-in to correct status drift [17:28]. V6 Grok Bot [6:39, 7:07]: Claude Code installed in a hosted bot's terminal, reachable from a phone. V9 Codex [12:42, 30:08, 31:44]: phone remote, scheduled tasks, voice across threads. V7 Context engineering [10:51, 11:53]: scheduled audits with approve-or-decline output, and team sync named as the next problem. V10 Mods [8:40]: one view of goals across sessions.

Disagree: V2 is sponsored and Nate says nothing shown was impossible before [20:39]; V9 says he rarely uses the cloud because an always-on machine feels the same [11:06]; the V6 summary checked Anthropic's legal page and found that third parties may not broker subscription sign-in, so whether Grok Bot's route is allowed is unverified.

Evidence: product claims second-hand; the six-hourly publishing loop and the media pilot report no results [V2 7:10, 4:48].

### 2.9 The trust ladder: narrow, watched, one tool at a time

Claim: start agents on small checkable work under tight permissions and widen trust only on evidence.

Support: V1 Pocock [36:05, 40:04]: brake before accelerator; menial, measurable work first, such as draft replies. V9 Codex [20:37, 21:25]: start on ask for approval; hard blocks in config. V5 Six repos [9:28, 7:06]: one tool at a time so a breakage has one cause; install narrowly, connectors read-only. V2 Kylon [4:48, 19:04]: one work stream, quick wins, then the next room. V7 Context engineering [10:51]: scheduled recommendations wait for approval. V10 Mods: Anthropic's page says mods are not sandboxed, and the viewer who read every line before installing is the standard.

Disagree: Herk relays, without a source, that well-known figures say to give models the most ambitious task, and Pocock disagrees [V1 40:04]. Nate's own scheduled trading tasks run unattended with real money [V9 30:56], and his Instagram room publishes every six hours [V2 7:10].

Evidence: opinion, consistent between host and guest.

## 3. Nate's current playbook

Corrected to what the summaries say. Where the summaries are silent, that is stated.

1. **A folder of plain files is the operating system.** A project is a folder; a short rules file (CLAUDE.md or AGENTS.md) is read before every message and works best as a routing map, not a store of everything [V9 0:48, 2:23, 3:10; V7 6:22]. His four labels are context, connections, capabilities and cadence [V6 4:08; V7 6:01].
2. **Skills are recipes, built from examples and corrected after each run.** The videos do not frame this as skills versus prompts. A skill is a Markdown file with a name, a when-to-use line and instructions; do the task well once, then fix the recipe when a result is off [V9 21:38, 22:12]. Build it by studying finished output, not by describing the style [V3 0:48, 2:25]. Keep presentation in a skill and let the model structure content [V7 4:47]. Ask the agent which skills it used [V9 23:01].
3. **Context hygiene on a schedule.** Define done by outcome, reason and constraints [V7 1:34]; keep what the model cannot infer [V7 5:35]; run /doctor for usage counts, token cost per listing, duplicates, stray files and broken skills, reviewing before deleting [V7 7:08, 7:55]; use a propose-first audit prompt that names the smallest change, cites files and edits nothing [V7 9:43]; repeat monthly or quarterly and at each new model, eventually scheduled with approve-or-decline output [V7 10:51].
4. **Hooks block, mods ask or display.** A hook stops an agent finishing until its code has run [V8 7:08]. Mods are plugin code that changes the desktop app: cache countdown and two-click handoff, display masking, a goal meter, and a collision check that asks rather than blocks [V10 2:53, 5:30, 7:23, 9:11]. He picked his mods by having Claude mine his session logs [V10 1:55]. The summary notes he never explains why a hook could not also ask.
5. **Multiplayer workspaces, sponsored.** Rooms with humans and agents, bring-your-own Claude Code and Codex, one work stream first, an end-of-day check-in and stalled-item pings [V2 0:00, 12:55, 17:28, 18:16, 19:04]. He concedes it adds no new capability [V2 20:39].
6. **Expert clones from a public corpus.** Crawl with one agent per source, compile a wiki over untouched raw files, extract rules with a quote or an inferred label, package as a sub-agent plus a grading skill, gate on a run, test on real work, then ingest new links [V8 3:10 to 9:31]. The same thin-file-plus-brain pattern builds his advisers [V4 7:52].
7. **Advisory councils that argue.** Chair plus single-question sub-agent seats, three rounds, forced dissent on unanimity, a subset of seats when the question is narrow, a PDF verdict with conditions, and a six-field brief in [V4 0:46, 2:20, 5:29, 6:17, 7:04, 11:02].
8. **Codex and Claude Code: he uses both, and states no rule for choosing.** V9 shows Codex as his general work assistant over the same folder, with CLAUDE.md copied to AGENTS.md and skills copied across [V9 8:45]; V4, V7, V8 and V10 show Claude Code for sub-agents, hooks, /doctor and mods; V2 and V6 plug both into hosted products [V2 12:55; V6 6:39]. The V9 description carries a ChatGPT partner tag, so treat that tour as possibly promotional. On effort he uses the middle tier at medium for knowledge work [V9 19:18]; Pocock runs Opus 5.5 at medium [V1 32:05].
9. **Goals, subagents, schedules and voice.** Goals with countable finish lines, stepping back on low-risk work; a strong main thread delegating to cheaper subagents; scheduled prompts on a timer; voice steering several threads, including from a phone [V9 6:21, 7:57, 28:34, 30:08, 31:44].
10. **The tool and repo landscape.** His current list: HyperFrames, Google Workspace CLI, Apify MCP, Scrollcraft (his own), Humanizer, Addy Osmani's Agent Skills, Expo, Supabase and Stripe skills, Playwright CLI, Claude Security, OpenSEO and a Codeburn spend tracker; he withdrew Claude Mem and Context Mode, which he recommended in May, and says to install one tool at a time [V5 0:24 to 9:46]. Hosted products: Grok Bot daily for small automations [V6 8:41], Kylon as sponsor [V2], Hyperagent as sponsor [V7 3:30], with Hostinger and Glaido promotions in every description.
11. **Trust and permissions.** Start on ask for approval, hard blocks in config [V9 20:37, 21:25]; the trust ladder and menial-first work are Pocock's, and Herk agrees that clear communication beats a newer model [V1 34:01, 36:05, 40:04].

## 4. Copy, adapt, ignore

For a six-person frame-making and eye-test practice with the estate described in `estate-context.md`.

| Area | Copy as-is | Adapt, and how | Ignore, and why |
|---|---|---|---|
| Instructions and skills | The propose-first audit prompt: smallest change, cite files, edit nothing [V7 9:43]. Ask the agent which skills it used after a run [V9 23:01]. | A /doctor-style audit as a scheduled, read-only wrapper on the existing `ai-system-audit` skill, counting usage across Claude and Codex because skills are shared [V7 7:08, 10:51]. A skill-step pass marking each step mechanical, judgement or customer-facing [V6 4:35]. | Wholesale rule deletion and six-monthly skill purges [V7 0:46]: the supplier lens-line rule, patient-data rules, NHS wording and clinical recall limits guard against harm. |
| Examples and briefs | The six-field decision brief [V4 11:02]. Keep `grill-me` before every build [V1 15:59]. | An exemplar pack of the practice's best proven letters, posts and replies for drafting accounts [V3 2:25], owner-approved, counts only. A one-page shop glossary read by skills, prompts and site copy [V1 22:27]. | REA itself and any decompiling of the practice management system or supplier portals [V3 11:09]: no need, and licence risk. |
| Verification | A browser smoke test after each site push at phone and desktop widths, never submitting forms [V5 7:54]. Seen, inferred, unknown labels on every pack [V3 9:34]. | A run gate hook for build agents, limited to offline fixtures on sanitised copies [V8 7:08]. A warn-and-ask collision check for the one-session-owns-the-website rule, only after Codex has read the mod's code [V10 9:27]. | Goal Meter percentages as proof of completion [V10 8:40]. Claude Security as a second reviewer [V5 7:34]: Codex is the sole reviewer unless the owner decides otherwise. |
| Decisions | The forced-dissent rule and a dated verdict with conditions and a review date [V4 2:20, 3:55]. | Role lenses such as cash, patient trust, capacity and offer clarity instead of celebrity personas; one seat on Codex to cut single-model echo [V4 7:04]; sequence after the CFO and CMO ledgers hold real numbers. | Brains scraped from named living people [V4 7:52]: terms and copyright unaddressed. Any council on recall intervals: clinical, the optometrist decides. |
| Knowledge | The quote-or-inferred rule for every stored rule [V8 5:33]. | Raw, wiki, index and log for NHS eligibility, data protection and advertising rules, from official pages, kept outside this public repository [V8 3:58]. A source note per website guide [V7 10:17]. | The 700,000-word crawl and paid X API [V8 2:47]; the Karpathy persona itself. |
| Models and cost | Record which model and effort ran each job [V6 6:20; V9 16:41]. Check an agent's claim about its own cost against the invoice [V6 3:58]. | A medium-effort trial on repeat jobs only after checks exist and results are compared [V1 32:05]; replay saved pseudonymised examples through a cheaper model using `agent-stress-test` [V3 11:58]. | Token-saver add-ons [V5 8:56]; the API-equivalent dollar figures [V9 17:28]; opaque routing for anything touching orders, patients or money [V6 0:47]. |
| Shared and remote | An end-of-day close-out check-in through the existing Slack reception agent, test channel first [V2 17:28]. One work stream at a time [V2 19:04]. | A profile page per agent inside the AI CIO register [V2 19:52]. Any scheduled Codex task joins the live watchdog before it counts as live [V9 30:08]. | Kylon, Grok Bot as a host for Claude Code, and bring-your-own agents on staff machines [V2 5:36; V6 6:39]: secrets rule, patient-data rule, new processors. Unattended real-money tasks [V9 30:56]. Six-hourly auto-publishing [V2 7:10]. |
| Content tools | Humanizer's tell list as a review rubric that never touches NHS or clinical wording [V5 3:57]. | HyperFrames for captioned draft reels from the monthly social batch, files only [V5 0:24]. Recording Mode for Crewley.ai demos, recorded on pseudonymised fixtures [V10 5:30]. | Scrollcraft, Apify, OpenSEO, Expo, Supabase and Stripe [V5]: wrong problems or paid third parties. Sites replacing GitHub Pages [V9 27:05]. The AI OS kit [V6 4:08]: its four labels already exist here. |

## 5. Contradictions and open questions

Between videos:

1. **Specs.** V5 recommends a spec, plan and build file sequence [5:33]; V1's Pocock says specs as the main artefact degraded his results over months [27:17]. The reconciliation the summaries support is: spec to start, the working artefact as the truth, which is how the five-stage gate already treats packages.
2. **Context size.** V7 says cut [0:00, 2:22]; V8 and V4 compile corpora of hundreds of thousands of words [V8 3:10; V4 7:52]. The thin-router-plus-folder pattern squares the two, but no video measures it.
3. **Autonomy.** V9 says start on ask for approval [20:37] and then shows unattended trading with real money [30:56]. V2 shows an approval step [6:22] and a loop that publishes every six hours [7:10]. V1 relays ambitious-first advice from unnamed figures and then endorses menial-first [40:04].
4. **Routing.** V6 wants visibility and per-skill pinning [6:20] yet prefers and uses the platform that hides them [8:41], and V2 sells hosted tiers that route too [12:55].
5. **Hooks and mods.** V10 says Collision Guard differs from a hook because it asks rather than blocks [9:11]; V8's hook simply blocks [7:08]. The V10 summary notes no explanation of why a hook could not ask.
6. **Sub-agents.** V4 prefers sub-agents to agent teams on cost and voice, unmeasured [7:04]; V1's Pocock says organising many agents is unsolved [41:31].
7. **Titles against content.** "Game changers" and "10x" headline videos whose own speaker calls the handoff button a small saving [V10 3:57] and whose figure concerns Anthropic's own prompt [V7 0:00]. V5's title says six, he says ten, the description links twelve. V5 also withdraws two of his May recommendations [8:56], which shows the shelf life of his tool advice.

Between the videos and the estate's governance:

8. **Owner presses.** Goal-and-step-back [V9 7:57], scheduled tasks [V9 30:08], agent-to-agent messaging [V2 0:47] and six-hourly publishing [V2 7:10] all assume an agent may finish without a human. The estate's permission split and watchdog allow read-only and draft work to run, and reserve every live write, patient message, supplier action and money movement for the owner. Anything adopted must keep that line, which means the autonomy in these videos applies to drafts, checks and reports only.
9. **Cost.** Seven seats over three rounds [V4], a 700,000-word crawl [V8 3:10], a dozen concurrent goal sessions [V10 7:23]: none is measured, and viewers in V4 expect heavy usage. The estate counts Make operations against a monthly budget and keeps agents frugal; councils and crawls need a cost estimate before a first run.
10. **Data protection.** Hosted workspaces and bots add processors [V2; V6; V7 3:30; V9 27:05]. Bring-your-own agents inherit the host's environment variables and accounts [V2 5:36]. Recording Mode masks the display while real values still reach the model [V10 6:19]. Session-log mining reads logs that may hold patient detail or keys [V10 1:55]. The estate's rules are that secrets live only in protected files, patient data is never pasted into chat, and no compliance approval exists for AI on clinical records. Each of these ideas must run locally on sanitised material or not at all.
11. **One vendor.** The playbook runs almost entirely on Claude Code and Anthropic models, with Grok Bot and Kylon routing to Opus too [V6 0:47; V2 13:30]. The estate already splits build and review across two vendors. The open question is whether a council or a rules wiki on one model echoes itself, as a V4 viewer argues, and whether a Codex seat fixes that.
12. **Named people as advisers.** V4 and V8 build agents from named living people's material without discussing terms or copyright. The estate's house style already follows two named marketing writers; a house-style checklist should quote short and cite, not impersonate.

Open questions the summaries leave: what a teammate's message can reach on a local agent [V2]; whether /doctor usage counts see skills used through Codex [V7 7:55]; whether the practice's Make-scenario prompts, which /doctor never sees, deserve the same audit [V7]; the cache lifetime on the owner's actual plan, since it differs by plan [V10 3:10]; and whether a first-party phone route already covers what the Grok Bot hack offers [V6 6:39].

## 6. Candidate AI accounts the evidence supports

Raw material, not the roster. Each sits inside the split that the agent collects, checks, flags and drafts while the owner approves, signs and presses. The first four already have designs in the owner's internal reports and are listed so the rest can be hung off them.

1. **ai-ceo**, exists. Read-only chief of staff: weekly facts pack, source and date on every figure, argues the other side, says not measured. Videos: V4 forced dissent and verdict with conditions [2:20, 3:55]; V9 phone and voice as a read-only front end [12:42, 31:44]; V1 primary-source briefing habit [7:15]. Reports to the owner.
2. **ai-cmo**, exists. Scorekeeper and sceptic with a numbers ledger and a scored decision log. Videos: V3 exemplar-led drafting [2:25]; V5 Humanizer rubric and HyperFrames drafts [3:57, 0:24]; V7 source note per guide [10:17]. Reports to the owner.
3. **ai-cio**, exists. Watches, counts, reminds and drafts, never presses; keeps the registers. Videos: V7 scheduled instruction audit [7:08, 10:51]; V2 agent profiles [19:52]; V9 scheduled-task register [30:08]; V5 vet-before-install [9:28]; V10 collision check [9:27]. Reports to the owner.
4. **ai-cfo**, exists. Read-only management view; code computes, model explains. Videos: V2 usage by person, room and agent [15:52]; V6 metered services against native features [2:22, 3:10]; V9 model as a cost dial [16:41]; V5 spend tracker [8:56]. Reports to the owner.
5. **decision-council**. Pressure-tests one named decision before money is spent: role-lens seats, three rounds, forced dissent, dated verdict with conditions and a review date; counts only, no clinical rulings. Videos: V4 [0:46, 2:20, 6:17, 11:02]; V8 keep the understanding [10:20]; V1 agents that argue [41:31]. Reports to the owner, fed by ai-ceo.
6. **brief-and-interview**. Turns the owner's dictated thoughts into the six-field brief, runs scheduled grill-me interviews on named gaps such as how patients heard of the practice, and writes dated process notes; asks only. Videos: V4 [11:02, 12:37]; V1 [15:59, 22:27]; V2 [10:21]. Reports to ai-ceo.
7. **rules-librarian**. A cited wiki of public rules the practice must state accurately: NHS eligibility, data protection, advertising. Raw, wiki, index, log; quote or inferred label; weekly list of uncited or changed rules; held outside this repository. Videos: V8 [3:58, 5:33, 9:31]; V4 brain folders [7:52]; V1 teach pattern [7:15]. Reports to ai-cio.
8. **exemplar-librarian**. An owner-approved library of the practice's best proven outputs with a note on why each works, plus a short cited house-style checklist, read by every drafting account. Videos: V3 [0:48, 2:25]; V8 the same four steps for any author [1:35]. Reports to ai-cmo.
9. **instruction-auditor**. Monthly read-only audit of Claude and Codex instruction layers and shared skills: usage across both tools, token cost per listing, duplicates, broken front matter, skill steps marked mechanical or judgement; one ranked page, edits nothing. Videos: V7 [7:08, 9:43, 11:05]; V10 log mining, sanitised [1:55]; V9 which skills ran [23:01]; V6 skill splitting [4:35]. Reports to ai-cio.
10. **model-and-cost-ledger**. Records which model and effort ran each scheduled job and what it cost, flags over-tiering, replays saved pseudonymised examples through a cheaper model and reports whether results match; never switches a live model. Videos: V6 [5:33, 6:20]; V9 [16:41, 19:50]; V3 [11:58]; V2 [15:52]; V5 [8:56]. Reports to ai-cfo, with a line in the ai-cio register.
11. **site-smoke-tester**. After each website push, opens the live pages in a real browser at phone and desktop widths and checks the booking widget and phone links without submitting anything; before a push, scans the public repository for keys or patient data. Videos: V5 [7:54]; V1 agent sees its own output [32:52]. Reports to ai-cio, results copied to ai-cmo.
12. **build-verifier**. A run gate that stops a build agent finishing until its code has run against offline fixtures, plus a pre-Codex ship check: what would the owner delete, does it work in the setting staff use. Videos: V8 [7:08, 8:43]; V1 raise the floor [4:48]; V3 rebuild and test [10:21]. Reports to ai-cio.
13. **close-out-chaser**. End-of-day prompt in Slack asking owners of open items to confirm status, attendance and sale value, with a stalled-item ping after a day for bespoke frame jobs and open owner decisions; nudges only, never moves a card; test channel first. Addresses the no-scorecard gap. Videos: V2 [17:28, 18:16]. Reports to the owner through the ai-ceo weekly pack.
14. **first-draft-assistant**. Drafts replies to existing reviews and caption variants from the exemplar pack, runs the tells checklist, and records how much staff edit each draft as the first trust measure; nothing posts. Videos: V1 menial and measurable first [40:04]; V5 Humanizer [3:57]; V3 study the output [2:25]. Reports to ai-cmo.
15. **reel-finisher**. Turns workshop clips into captioned, titled draft reels and short motion cards from a goal with a countable finish line checked by screenshot; files only, generic captions, owner approval for any staff or customer likeness. Videos: V5 [0:24, 0:47]; V9 [7:57]. Reports to ai-cmo.
16. **tool-intake-reviewer**. Before any third-party skill, plugin, mod or MCP is installed: read the source, note what leaves the machine and what it can write, pin a version, log it, and have Codex review it in a scratch project. Videos: V5 [9:28, 8:56]; V10 mods are not sandboxed and a viewer read every line; V2 the open question of what a shared agent can reach [5:36]. Reports to ai-cio.

Held back, with reasons: a pocket console or always-on host [V6 6:39] until a first-party route and the terms are settled; a Next Steps panel [V10 0:46], which Nate himself doubts for knowledge work; any account that reads clinical records, which has no compliance approval.

## 7. Sources

Each file is a verified summary in `ai/videos/`. Confidence is as each summary reported it.

| Ref | File | Video | Confidence reported |
|---|---|---|---|
| V1 | `01-matt-pocock-most-valuable-ai-skill-2027.md` | Matt Pocock interview, 16 Oct 2026, 44:51 | High on what was said; medium on proper nouns and model names; self-reported figures unverified |
| V2 | `02-multiplayer-ai-agents-kylon.md` | AI Agents Just Became Multiplayer, 15 Oct 2026, 22:24, sponsored | Medium: high on content, low on product claims and availability |
| V3 | `03-reverse-engineer-anything-skill.md` | Reverse Engineer Anything, 13 Oct 2026, 14:59 | Medium-high on what Herk said; medium on the five-step framing; low on his performance claim |
| V4 | `04-roast-room-board-of-advisors-skill.md` | Roast Room board of advisers, 12 Oct 2026, 14:45 | High for content; lower for how the skill behaves, repository not inspected |
| V5 | `05-six-best-github-repos-for-claude.md` | Six best GitHub repos, 11 Oct 2026, 10:37 | High on content; medium on truth of claims; one claim contradicted |
| V6 | `06-grok-bot-two-upgrades.md` | Grok Bot two upgrades, 8 Oct 2026, 9:11 | Medium: names and figures garbled, platform facts second-hand |
| V7 | `07-anthropic-context-engineering-claude-code.md` | Context engineering and /doctor, 8 Oct 2026, 12:23 | Medium: article and figures matched to sources; /doctor behaviour and private-setup figures unconfirmed |
| V8 | `08-expert-clone-andrej-karpathy.md` | Expert clone of Andrej Karpathy, 5 Oct 2026, 10:45 | High on content; medium on external claims, secondary corroboration only |
| V9 | `09-master-codex-in-35-minutes.md` | Master 96% of Codex, 3 Oct 2026, 34:34, possibly promotional | High on content; medium on product claims and usage economics |
| V10 | `10-five-claude-code-mods.md` | Five Claude Code mods, 2 Oct 2026, 11:19 | High for what was shown; medium for platform facts; low for benefits |
| V11 | `11-build-and-sell-software-as-a-non-techie.md` | Build and sell software as a non-techie, interview, 2 Oct 2026, 1:09:33, one sponsored segment | High on what was said; medium on garbled names; low on the productivity and security claims |
| V12 | `12-codex-ultrafast-tested.md` | Codex Ultrafast tested, 1 Oct 2026, 9:03 | High on what was shown and measured; low on the general speed and usage claims and the plan-pricing dispute |
| V13 | `13-openai-dots-vs-meta-muse.md` | OpenAI Dots against Meta Muse, 30 Sep 2026, 16:30 | High on what Herk showed and concluded; low on model names, pricing, limits and privacy |
| V14 | `14-sonnet-5-5-vs-opus-5-5-tested.md` | Sonnet 5.5 against Opus 5.5, 28 Sep 2026, 25:49 | Medium: figures clearly stated but unchecked; one chapter badly garbled; single-run judgements |
| V15 | `15-gpt-6-astra-stock-trading-experiment.md` | GPT-6 Astra trading experiment, 28 Sep 2026, 18:00 | High on what was shown and said; low on any conclusion about AI trading |
| V16 | `16-seven-best-ai-tools.md` | Seven best AI tools, 19 Oct 2026, 10:16, one sponsored section and one partner product | High on what was said; low to medium on whether the claims are true; the Hostinger and Glaido sections are commercially tied |
| V17 | `17-roast-room-how-nate-uses-it.md` | Roast room revisited, 22 Oct 2026, 15:00, one sponsored section | High on what was said; medium on the vote split; cost claims his own; repository not opened |

Context files: `research/nate-herk/business-context.md` and `research/nate-herk/estate-context.md`. The structured index `round1-key-ideas.json` was read as a cross-check and treated as data. No transcript is quoted here.

## 8. Addendum: videos 11 to 15 (28 September to 2 October 2026)

Written 17 October 2026 from the five verified summaries `11` to `15` in `ai/videos/`, the five videos published just before the ten above. Citations follow the pattern above; nothing was checked against the videos themselves. None is a build walkthrough. Sponsored, promotional and self-reported claims are labelled as they arise.

### 8.1 What each video adds

**V11, building and selling software as a non-technical person.** An interview whose lasting idea is a four-rung ladder of risk: a tool for yourself, for your team, sold to a company, sold to the public, with legal and data duties rising at each rung and a warning not to skip one [V11 12:42 to 15:20, 17:06]. What separates beginners from veterans is the quality of instructions and review, not the tools [V11 17:58]. On testing: define good, make examples the test set, let an agent loop against a measurable target [V11 29:39 to 32:18]; for subjective output, a second model as judge, scored for agreement with a human who marked a sample and retuned when the model changes [V11 36:44 to 39:25, 41:12]. He says specs and plan mode matter less than a year ago [V11 22:31, 28:46]; that is his own practice, and his report that Anthropic engineers agree is second-hand. CodeRabbit is sponsored, Hostinger and First Client SOP are promotional, and the tenfold productivity figure and the near-impossible-to-hack claim are unsupported assertions [V11 1:28, 53:42].

**V12, Codex Ultrafast.** A test of a top speed setting that, per Herk, comes only on the most expensive plan [V12 0:00]: same prompt, two settings, with time, share of weekly allowance and a side-by-side of outputs recorded [V12 5:12, 6:35]. The reel ran about 2.5 times faster against an advertised eight, for about four times the allowance; the guide ran about seven times faster for three times the allowance, with no quality difference [V12 4:52, 5:39, 7:14]. Verdict: speed bought no visible quality, and a constant need for speed means the planning is wrong [V12 8:00, 8:12]. One run per setting; the comment that the plan is a repriced older tier is unverified. Glaido and Hostinger links are promotional.

**V13, two consumer personal agents.** OpenAI's Dots against Meta's Muse, both always-on cloud agents with memory, schedules and connectors [V13 1:34], after about a day with each. Herk values an approvals tab and a 30-minute heartbeat over documents and email [V13 8:36], memory and persona as two editable files [V13 3:08], and an agent reachable from a team Slack channel [V13 4:42]. He dislikes memory gone stale from old chat history [V13 2:21], scheduled tasks hidden from the product's own screen [V13 11:43] and a product that misdescribed its own features [V13 12:30]. Model names, free-tier limits and the failed demo are one reviewer's account from garbled captions [V13 0:47, 7:02]; privacy is not covered.

**V14, Sonnet 5.5 against Opus 5.5.** Seven tasks, same prompt, both at high effort, judged blind, with time, tokens and API cost logged [V14 2:24, 6:21]. Opus is roughly double per token, but the gap across the set was far smaller [V14 0:48, 24:44]. The rule: where the job has a clear spec and an obvious check, or a skill already defines good, start with the cheaper model; where the goal is vague or needs a thought partner, use the stronger one [V14 1:36, 12:54]. The resource-guide round, where a good skill produced near-identical output from both, is the strongest evidence [V14 23:58]. He also suggests recording which model each skill wins on [V14 1:36] and asks for spreadsheets built on formulas [V14 15:16]. His speed and price figures are unchecked, each round is one run judged by him, viewers dispute the final cost gap and note that his existing memory and skills shaped both outputs. ScrollCraft is self-promotion; Glaido is promotional.

**V15, the trading experiment.** Read strictly as a workflow lesson, never as money advice; the practice does not trade and nothing here is financial advice. Six scheduled routines wake one agent through the day in one thread, each leaving a handoff note the next reads, so short runs behave as one worker [V15 0:56, 1:54]. When the model declined to place orders, Herk split thinker from doer with a second agent woken by an email webhook [V15 3:43, 4:40]. The agent was cautious to the point of inaction and he loosened its gates mid-run, which he and the most-liked comment agree is why the result proves little [V15 2:48, 5:34, 17:36]. His daily figures are inconsistent and the "model restriction" is his account only.

### 8.2 Themes strengthened or weakened

- **2.1, a finished example beats a description: strengthened.** V11's define-good-then-test-set [29:39] and V14's good-skill-levels-the-models [23:58] are the same claim from two angles, and V14 gives it a cost dimension: a vague prompt favours the stronger model, a precise one closes the gap [12:54, 13:41].
- **2.3, proof by running: strengthened.** V11's judge model is the pack's first method for measuring subjective output [36:44 to 39:25]; V14's blind judging [2:24] and V12's same-prompt A/B [5:12] apply the discipline to model choice.
- **2.4, match model and effort to the step: strongly strengthened.** V14 supplies the rule and the per-skill record [1:36]; V12 adds speed tier as a second dial that can multiply allowance use for no quality gain [4:52, 7:14]; V11's instructions-and-review point [17:58] argues for spending on review rather than tier.
- **2.2 and 2.5, small context and interview first: slightly weakened.** V11's guest builds and reacts rather than specifying [22:31], though Herk still interviews to draw out intent [V11 24:16]; V13's stale chat memory [2:21] supports dated files the owner can read. The reconciliation in section 5 item 1 holds.
- **2.8, shared and always-on agents: strengthened as pattern, weakened as product case.** V13 and V15 show heartbeat, approvals, team channel and chained routines [V13 8:36, 4:42; V15 1:54]; V13 also shows them buggy [11:43, 12:30].
- **2.9, the trust ladder: strengthened.** V11's rungs [12:42] are the ladder with legal duties attached. V15's cautious agent [2:48] is the opposite failure in a low-stakes setting; here a conservative agent that holds and asks is the desired behaviour.
- 2.6 and 2.7 are unchanged.

### 8.3 New themes

- **The non-technical builder path and selling software.** V11's ladder maps onto Crewley.ai: the estate is rungs one and two, selling to other practices is rung three with new contract and data duties [V11 12:42 to 16:12]. The `business-filter` skill and five-stage gate already sit at that boundary; the ladder is a sorting label, not a new process.
- **Speed tiers and allowance cost.** Speed is a dial separate from model and effort and scales badly on long jobs [V12 4:52, 5:39]. The estate's slow steps are gates, not model speed. Record allowance share per job type before any premium mode is trialled [V12 1:33].
- **Model-tier choice with cost visible.** V14's rule and method [1:36, 2:24] match the estate's orchestrate, build, review split and give it a test: a side-by-side on two or three repeating jobs, on pseudonymised fixtures, before any model change. The method is carried over; the dollar figures are not.
- **Consumer AI products.** V13's useful pieces (approvals in one place, a heartbeat, editable memory files, Slack as front door) exist here in parts. Both hold memory with the vendor, which rules them out near patient data [V13 1:34].
- **Autonomous routines and handoffs.** V15's chain of scheduled runs reading each other's notes [1:54] is a pattern the estate's event-triggered agents do not use; a day-shaped, read-only chain (morning brief, midday check of existing alerts, closing summary) would suit the Frame maker's rhythm. Thinker split from doer [V15 4:40] is already the rule: the agent drafts, a person presses.

### 8.4 Contradictions with sections 2 to 5

1. **Specs (item 1).** V11 joins V1's side [22:31]. The spec stage stays for live writes; prototypes already live in the test channel.
2. **Autonomy (items 3 and 8).** V15 is V9's unattended trading run shown in full, and the agent was never left alone, so nothing was learned [V15 2:48, 5:34]. Autonomy for drafts, checks and reports only, with rules frozen for a trial window.
3. **Cost claims (item 7).** An advertised eightfold speed measured at 2.5 [V12 4:52] and a disputed final cost gap [V14 24:44] back the rule that a cost claim is reported until a usage page agrees.
4. **Routing (item 4).** V14 is the counter-practice to V6: model chosen per task, cost logged per run [2:24]. V13's products hide the model behind a persona.
5. **Hosted products (item 10).** V13 adds two consumer-grade processors with vendor-held memory [1:34]. Local on sanitised material or not at all.
6. **Model refusals, new.** V15 engineered round a refusal with a second agent [4:40]. The estate reads a refusal as a signal to keep the human step.

### 8.5 Change to the candidate accounts in section 6

No new candidates. Six existing ones gain sources:

- **model-and-cost-ledger** (6.10): V14 rule, cost per run, skill-to-model register [1:36, 23:58, 24:44]; V12 allowance share per job type, speed tier as a dial [1:33, 5:39].
- **build-verifier** (6.12): V11 define good and build the test set from examples [29:39 to 32:18]; V14 ask for the checkable definition of done first [12:54].
- **instruction-auditor** (6.9): V11 abandoned experiments as hidden dependencies, flag never delete [48:26]; V13 dated, readable memory files [2:21, 3:08].
- **ai-cio** (6.3): V13 one page of pending approvals and scheduled jobs with last run [8:36]; V15 log every rule change during a trial beside its results [2:48, 5:34].
- **first-draft-assistant** (6.14, now content-drafter): V11's judge-model method as a second trust measure beside the edit rate, on owner-marked pseudonymised samples only [36:44 to 39:25, 41:12].
- **ai-cfo** (6.4): V14's formulas-not-values rule [15:16].
- **No change** to the other ten candidates. The summaries' own role ideas (usage meter, change risk sorter, test data maker, day-shift conductor and the rest) all fold into the accounts above or into alerts already live.
- **Held back, added to the list:** consumer personal agents (V13) near patient data; any premium speed tier (V12) without a recorded allowance baseline; loosening a cautious agent's gates outside the five-stage gate (V15).

## 9. Addendum: videos 16 and 17 (19 and 22 October 2026)

Written 24 October 2026 from the two verified summaries `16` and `17` in `ai/videos/`, the two videos published after the ten above. Citations follow the pattern above; nothing was checked against the videos themselves. Neither is a build walkthrough. Sponsored, partner and self-reported claims are labelled as they arise.

### 9.1 What each video adds

**V16, seven tools he uses every week.** A personal tool list; the useful parts are habits. He pays for both Claude Code and Codex and switches per task, rating Codex better at browser use and Claude Code the better thinking partner; his opinion, and he says it may change within two months [V16 1:33]. He routes nearly all production automations through one model supplier, with a separate key per automation so the dashboard shows cost per job, a fallback model if one fails, and a cheap model sorting while a stronger one writes [V16 2:10, 2:20, 2:50]. Predictable, same-steps-every-time jobs go into hosted scripts that Claude Code writes and maintains; a full agent is overkill for them [V16 8:14, 8:38]. Weaker evidence: the always-on server is a sponsored section [V16 3:41]; he is a partner in the dictation tool and its privacy claims are his own [V16 6:28]; the free kit is his lead magnet [V16 3:13]; the provider counts and the 90% share of his work are self-reported [V16 0:46, 2:10]. Several viewers called the video an advert.

**V17, the roast room revisited.** A tour of the repository behind V4's adviser panel. Each seat is a short agent file plus a brain folder with the same file set for every person, and its summary sheet records what the brain was built from: source count, word count and date range [V17 2:22, 3:10, 3:58]. The chair now proposes which seats attend and the user can swap one; in the live run a founder-time seat was swapped for one that suited the question [V17 7:58, 9:33]. Sessions are saved as a brief, round one, round two and a verdict, with each seat's reasoning readable afterwards [V17 10:21]. Unanimity makes the chair assign a devil's advocate, stated as a rule this time [V17 11:09]. He says sub-agents replaced agent teams because teams cost more for little extra value; his own claim, no comparison shown [V17 8:46]. A New Roster skill builds a new named seat on request [V17 6:14, 13:59]. Fish Audio is a sponsored section [V17 4:46]. The most-liked comment raises the legal position of putting opinions to a living person's name.

### 9.2 Themes strengthened or weakened

- **2.4, match model to the step and see the cost: strengthened.** V16 supplies the mechanism the ledger lacked: one key per automation, so cost arrives already split by job [2:20], and the cheap-sorts, strong-writes split [2:50]. V17's sub-agents-over-teams point repeats V4 and is still unmeasured [8:46].
- **2.7, structured dissent: strengthened.** V17 states the devil's-advocate rule outright [11:09], shows the chair proposing seats with reasons [7:58], and saves sessions so a verdict can be reopened [10:21].
- **2.6, cited knowledge: strengthened.** The seat sheet with its source tally [V17 3:10] is the quote-or-inferred rule applied to a persona. It still says nothing about copyright or terms for a named living person.
- **2.3, proof by running: weakened by V16's fallback advice.** A silent fallback changes who answered without a run to prove the answer matches, and a viewer warns it can quietly change a category [V16 2:20, comments]. That conflicts with fail-loud here.
- **2.8, always-on agents: product case weakened.** The rented server is sponsored [V16 3:41], and the Make and Mac schedules with a watchdog already cover it.
- **New: scripts, not agents, for predictable work** [V16 8:38]. The estate already works this way: Make scenarios and code for fixed steps, the model only explaining. Nothing to build.
- 2.1, 2.2, 2.5 and 2.9 are unchanged.

### 9.3 Contradictions with sections 2 to 5 and 8

1. **Fail-loud against fallback (item 8, theme 2.3).** V16's fallback keeps a job running when a model fails [2:20]; the estate's rule is fail loud, never silent rollback. Any fallback here is a model change and needs fixture replay in the test channel first.
2. **Named people as advisers (item 12).** V17 goes further than V4: eleven named seats and a skill to add more [1:35, 6:14]. The legal-risk comment supports the role-lens rule, and the reason is now written into the account.
3. **One vendor (item 11).** V16 runs both coding agents and advises building files so you can switch [1:33], which matches the estate's two-vendor split. V17 runs the whole room on one model; the Codex seat stays.
4. **Hosted processors (item 10).** A model router is one more company handling prompts [V16 2:10]. Counts and sanitised fixtures only.
5. **Shelf life of tool advice (item 7).** The list is personal and changes [V16 9:21], and two of the seven tools are commercially tied. Reported, not adopted.

### 9.4 Change to the candidate accounts in section 6

No new candidates. Three gain sources and one rule gains its reason:

- **model-and-cost-ledger** (6.10): V16 one key per automation so cost per job is visible [2:20]; cheap sorts, strong writes, as a tiering pattern to check jobs against [2:50].
- **ai-cio** (6.3): V16 fallback models as a register item that conflicts with fail-loud and needs fixture replay before use [2:20, 2:50]; a subscription sweep of tools paid for one feature as a CFO or CIO register line, not an account [1:00].
- **decision-council, now advisory-board** (6.5): V17 chair proposes seats with reasons and the owner swaps one [7:58, 9:33]; a dated seat sheet per lens, held outside this repository [3:10, 3:58]; sessions saved as brief, two rounds and verdict, plus an outcome note [10:21]; devil's advocate on unanimity as a stated rule [11:09]; an optional owner-dependency lens, not a named person [0:48]; the no-impersonation rule now carries its reason.
- **No change** to the other thirteen candidates. V16's role ideas (Subscription Sweeper, Model Key Auditor, Fallback Replay Tester, Agent or Script Triage, Dictation Safety Check) fold into the ledger, the AI CIO registers, the existing agent-drafts-owner-presses split, or an owner decision; the roster re-check has the mapping.
- **Held back, added to the list:** a rented always-on server (V16, sponsored); voice dictation until where audio and text go has been checked (V16, partner product); the New Roster skill and any seat built from a named living person (V17).

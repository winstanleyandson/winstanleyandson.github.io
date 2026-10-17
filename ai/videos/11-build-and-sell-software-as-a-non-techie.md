# How to Actually Build & Sell Software with AI as a Non-Techie

- **Channel:** Nate Herk | AI Automation
- **Published:** 2 October 2026
- **Duration:** 1:09:33
- **Views:** 103,821 (at collection, 17 October 2026)
- **URL:** https://www.youtube.com/watch?v=l8ywUsEJ2XQ
- **Guests:** Dave Ebbelaar (spelled "Ablar" in the captions), a Python developer who runs a team shipping a voice-dictation product called Glaido

## What the video covers

This is an interview, not a tutorial. Nate Herk, whose audience is mostly non-programmers, asks Ebbelaar how someone with no coding background should build software with AI and what changes once other people rely on it. Ebbelaar says he no longer writes code by hand. He sorts projects into four rungs by risk: a tool for yourself, a tool for your team, a service sold to a company, and a product sold to the public. He argues that detailed specs and plan mode matter less than they did a year ago, and that you should ask for the thing, look at it and react. They then cover testing: defining what good looks like, building example data, and using a second model as a judge whose agreement with a human reviewer is measured and tuned. The final third covers architecture, one costly stack mistake, and a short security checklist (database access rules, firewalls, secrets, strong logins). It ends on career optimism and a plug for his channel. Two segments are adverts. It is not a build walkthrough.

## Chapter-by-chapter

Chapter times come from the description. The captions run in blocks of about 50 seconds, so positions are approximate.

**0:00 Intro.** The video opens with clips from later in the conversation: Ebbelaar says he writes no code himself, a single prompt can now produce something useful, and a data leak cannot be undone. The remainder of the section is the formal opening question to him about how software engineering has changed. He is introduced as a decade-long Python developer whose team has delivered over fifty AI solutions.

**1:28 A solid 10X.** Ebbelaar says that in 2013 coding was slow and hard, and that today useful tools come from one prompt. Asked for a number, he first jokes about 100 times against his beginner days, then, against his own 2022 output, claims a solid tenfold gain in production-ready code, and more in areas he could not do before, such as front-end work in a language he never learned. He argues that specialists now hit bottlenecks because agents outrun human hand-offs, so being a generalist who understands engineering principles is the better position [5:28 to 8:13]. His team still has roles but gives each person ownership of a feature from start to finish.

**8:19 Sponsor: CodeRabbit.** A paid read by Herk for CodeRabbit's pull-request review page. It groups a change into related chunks, orders them by dependency, opens on a summary and walkthrough page, and offers a view that tells moved code from changed code, with a 14-day free trial. Afterwards the conversation resumes with a question on how Ebbelaar felt about the vibe coding trend. He is in favour: fine for a personal site, but care is needed once other people's data is involved.

**12:42 The four-rung ladder.** Ebbelaar sets out the ladder: for you, for your team, sold to a company, sold to consumers. Each rung adds risk, from contract terms and data duties to personal data rights. Herk agrees you must earn each step up (about 19:50), and Ebbelaar adds that the danger is a non-technical builder skipping straight to selling custom software that firms depend on [16:12]. He says anyone can begin on the lowest rung and move up later. Both beginners and veterans now use the same tools and process; what differs is the instructions given and the review. He suggests a $20 plan to start and $100 to $200 for steady use. He names two top models; the captions read GPT6 Astra and Opus 5.5, which I could not verify and may be garbled.

**21:05 Building with agents.** Ebbelaar says spec-driven development, where the AI writes a requirements document before any code, was the norm a year ago but he now often goes straight to building. Herk adds a grill-me style interview to draw out intent, and says Google engineers he spoke to call this intent-driven engineering; Ebbelaar likes the term [24:16, 25:10]. His team builds on a separate branch of the real product so they can see and react immediately, rather than in a playground. Herk's "First Client SOP" advert for his free guide interrupts at about 26:54.

**27:04 First Client SOP.** The chapter title only covers the short advert. The rest of the section returns to planning: Herk says he used to start everything in plan mode, and Ebbelaar replies that plan mode is less needed because models and tools have absorbed the habit of thinking first. He adds that he thinks he saw Anthropic engineers say so on X, which is second-hand and unchecked [27:47 to 28:46]. The conversation then moves to testing from about 29:39. Ebbelaar says to define good for the product, gather examples, and turn them into a test set. Models can invent realistic data if you have none, and you can tell an agent to improve a measurable target in a loop [31:27]. From 34:06 they take the harder case where quality is a matter of taste, and he describes the judge-model method (idea 8 below).

**42:44 Shipping it safely.** Ebbelaar splits architecture into system level (back end, front end, database and how they talk) and project level (how files, functions and modules are organised). He advises asking the agent which stack suits your project before starting, because changing language later is costly; his team did this once. He warns of tangled code from abandoned experiments, and mentions a Matt Pocock skill for reviewing structure. The security section covers one database product, access rules per row, strong passwords with two-step login, keeping secrets out of code, and allow-listing which addresses may reach the back end and database. The last minutes are career encouragement.

## Key ideas and claims

1. Builders and veterans now use the same tools and process; the difference is the quality of instructions and review [17:58].
2. The four-rung ladder of risk: self, team, sold to a company, sold to consumers. Stakes, legal duties and data duties rise at each rung [12:42 to 15:20].
3. Do not skip rungs. A beginner selling custom software that companies depend on has skipped the learning that makes it safe [17:06].
4. Vibe coding is fine when the stakes are low; personal data changes that [10:51].
5. A broken feature is noticed and fixed, but a leaked data set cannot be recalled [19:50].
6. Ebbelaar says detailed specs and plan mode matter less now; build, look, react [22:31, 28:46]. This is his experience, and he works on a separate branch so nothing ships at once. The report that Anthropic engineers agree is second-hand.
7. Define good, collect examples, make them the test set, and let an agent loop against a measurable target [29:39 to 32:18].
8. For subjective output, use a second model as judge. A human marks around a hundred examples, the judge is scored on agreement, and its instructions are refined until agreement is high; recheck occasionally for drift [36:44 to 39:25].
9. Judge prompts may need retuning when the underlying model changes [41:12, Herk].
10. Pick the stack for the job, not the one you know; ask the agent to compare options first [45:42].
11. Abandoned experiments left in a codebase become hidden dependencies and cause late bugs [48:26].
12. A short security core: database row-level rules, strong passwords plus two-step login, secrets in environment settings, firewall allow-lists [56:24 to 1:00:50]. He says doing a handful of these things makes being hacked close to impossible; that is a strong claim and no evidence is given [53:42].

## Tools, products and repos mentioned

| Name | What it is | Link |
|---|---|---|
| Claude Code | Anthropic's coding agent, which Ebbelaar says he works through | no link given |
| Codex | OpenAI's coding agent (captions say "codeex") | no link given |
| Grok (a guess) | Ebbelaar names a third coding tool at about 17:06; the captions read "grot", which I take to mean Grok | no link given |
| Glaido | Voice-to-text dictation app built by Ebbelaar's team; a free month is offered in the description. Whether Herk is paid for it is not stated | https://get.glaido.com/nate (description) |
| CodeRabbit | AI pull-request review tool. **Sponsored** | https://coderabbit.link/ad-nate-herk-001 |
| Hostinger VPS | Rented virtual server; discount code in the description, not mentioned in the video. **Promotional** | description link is cut short; no full link given |
| First Client SOP | Herk's free guide, from his paid community. **Self-promotion** | description link is cut short; no full link given |
| Supabase | Hosted database service Ebbelaar recommends by default (captions say "Superbase") | no link given |
| Railway, Render | One-click hosting services, named as deployment options | no link given |
| Matt Pocock's engineering skills | Public skill set; one reviews codebase structure. Ebbelaar thinks it was renamed (earlier improve codebase architecture, perhaps now codebase design) and is unsure; Herk says it will be linked, but the description has no link | no link given |
| Dave Ebbelaar's YouTube channel | Source of his handbooks and builds (captions say "Dave Ablar") | no link given |

No GitHub repositories are linked in the description.

## How to apply it

Not a build. It is an interview with a risk model, a testing method and a security checklist, with no step-by-step setup.

## What viewers said

Comments are opinion, not fact.

- **Requests:** the most-liked comment asked for a deeper follow-up on security, deployment and infrastructure for intermediate builders. Others asked for a practical session, a guide to how project files and skill files should be organised, a plain-language breakdown of Pocock's skills, and a video on a tool the guest's podcast reference brought to mind.
- **Questions:** which agent handles security checks; which Pocock skill was meant; which pricing model (performance-based or value-based) makes money fastest for a service business.
- **Confirmations:** a veteran C++ developer said AI makes his work far easier and he mostly checks the output. A no-code builder found it useful. Another viewer reported long autonomous runs with goals plus hand-off notes. Others praised the chat.
- **Pushback:** one viewer thinks ten times is too modest and suggests far more for a solo developer. One said selling software you cannot code yourself is poor business. Another said the leak warning is the point to remember, and that a demo for yourself differs from handing a process to an organisation that must justify it to compliance staff. One noted the audio volume jumps between clips. One said the video does not help you choose tools or where to run them.
- **Noise:** a few comments were promotional links to unrelated videos or a list of timestamps that differs from the description. Neither is evidence about the video.

## Relevance to Winstanley & Son

- **The ladder describes the estate's own gate.** The five-stage change gate, Codex review and isolated test channel already do what Ebbelaar recommends at the higher rungs. What is new is a simple sorting label: tag each change as personal, staff-facing, patient-facing or sold-to-others, and match the review depth to it. Crewley.ai selling to other practices is rung three, which brings contract terms and data duties the shop never had.
- **Build-first versus spec-first.** The estate's spec stage is a deliberate choice for live writes, so this video does not overturn it. It supports building quick prototypes in the test channel and reacting to them, then formalising only what survives. That fits the existing prototype stage.
- **A judge model with measured agreement would be a new method.** The estate has `agent-stress-test` and fixtures, which check the agent against known answers. The estate notes list no method for subjective output such as social captions or reply wording. Marking a sample, scoring a judge model against those marks and tuning it would add one. Patient data must not enter the sample; use pseudonymised fixtures.
- **Security basics overlap with named gaps.** Secrets outside code and protected token files are already live. Two-step login everywhere and a password manager with a deputy are listed gaps, and the checklist supports them. Row-level database rules and firewall allow-lists matter only if Crewley.ai ever hosts a database-backed product; today the estate runs on Make, GHL and a static site, so they are not urgent.
- **Stack choice and tidiness.** The warning about abandoned experiments suits the Python build script and the many estate copies. It supports an occasional structure review under the AI CIO rather than a new build.
- **Caution on claims.** The tenfold gain, the claim that basic security makes hacking close to impossible, and the model names are the guest's assertions, and the video's sponsored and promotional segments are adverts. Nothing here is financial advice for the practice.

## Account or role ideas this video suggests

1. **Change Risk Sorter** (AI CIO) [12:42, 15:20]. Mission: label each proposed change by rung (personal, staff, patient-facing, sold to others) and name the review it needs. Inputs: the change request and systems touched. Outputs: a label and a checklist in the change register. Guardrails: advises only; the existing five-stage gate stands and the owner decides.
2. **Wording Judge** (AI CMO) [36:44, 38:32]. Mission: score drafts such as captions and listing text against the owner's marked examples. Inputs: a sample the owner has marked good or poor, and new drafts. Outputs: a pass or fail with reason and a monthly agreement score. Guardrails: counts only, no named patient; owner approval for staff or customer posts stays; retune after any model change.
3. **Test Data Maker** (AI CIO) [31:27]. Mission: produce realistic but invented fixtures for stress tests. Inputs: field shapes only. Outputs: labelled fake records, extending the live `agent-stress-test` fixtures. Guardrails: never copies from live records; fixtures never sent to a real number.
4. **Security Basics Keeper** (AI CIO) [56:24, 1:00:50]. Mission: maintain a plain checklist of two-step login, strong passwords, secret storage and who has access, feeding the incident and risk registers. Inputs: owner confirmations, login register without values. Outputs: a monthly page of what is checked and what is open. Guardrails: never sees password values; reports, never changes settings.
5. **Stack Choice Reviewer** (owner, for Crewley.ai) [45:42, 46:38]. Mission: before any Crewley.ai product build, compare stack options and record the choice and reason. Inputs: the product brief. Outputs: a one-page recommendation with switching costs. Guardrails: owner decides; the business-filter skill comes first.
6. **Codebase Tidy Reviewer** (AI CIO; low priority) [48:26, 49:20]. Mission: flag dead or half-used files in the build script and estate copies. Outputs: a short list for the owner. Guardrails: never deletes; copies, not live.

## Sources used and confidence

Sources: the full transcript (auto captions, with errors in names and products), the description (two links cut short; one link in the links list, a second given in full in the text), the public comments with names stripped, and the two context files. No web searches were run, so no outside facts were checked, and no pages from the links were opened.

Confidence: **high** for what was said and where, because the captions are long and mostly clear. **Medium** for who and what was meant in a few places, as names are garbled (guest surname, models, the skill author's product). **Low** for the productivity and security claims, since they are the guest's opinion with no measurements.

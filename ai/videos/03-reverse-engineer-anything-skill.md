# I Tested the Viral Reverse Engineer Anything Skill. What You Need to Know.

- Channel: Nate Herk | AI Automation
- Published: 13 October 2026 | Duration: 14:59 | Views: 173,296 (at collection)
- URL: https://www.youtube.com/watch?v=rL5tw6h78zo
- Guests: none

Chapter titles and times come from the video description. Bracketed times in the claims lists are the start of the transcript caption block where the point is made, so they are accurate to roughly the nearest 30 to 50 seconds. The captions are automatic and garble several product, model and personal names; those are flagged where they matter.

## What the video covers

Nate Herk reviews Reverse Engineer Anything (REA), an open-source tool that lets a coding agent study an existing app, explain how one of its features works, and then build a version of it. The repo was trending fast, and Herk says one well-known AI commentator half-joked that software was finished. Herk's view is that the idea is not new. He had already been getting good results by showing an agent finished examples of what he wanted and asking it to work backwards from them.

He walks through his own examples: two made before the repo existed (an Instagram Reels editing skill and a recreated motion graphic) and several made with it or by the same method (a local Loom-style screen recorder, an Instagram analysis tool, an evaluation tool inspired by Langfuse). He then explains REA with a bakery analogy, and gives a five-step way to use it: pick one feature, route by how the app is built, work from a summary first, label every finding as seen, inferred or unknown, then rebuild and test. He closes with the limits (no copying code or assets, results depend on the model) and the broader lesson: copy the method of anyone who does a task well, including in your own business processes.

## Chapter-by-chapter

**0:00 Reverse Engineer Anything.** Herk introduces the repo, attributes a half-joke that software is done to a well-known AI commentator (the remark itself is unchecked), and says the idea is that you point agents at a feature you like and they recreate it. He has used it for games, tools and apps and finds it impressive, but argues it is not new.

**0:52 Better AI Outputs With References.** Herk says AI is not creative but executes a clear vision well. He shows a Reels-editing skill built by having an agent watch about 30 of his best-performing reels and analyse them frame by frame, and a recreated motion graphic from another creator's clip, where the original was still a little better on motion and sound design. His rule for skills: study the output. A Friday report skill should look at five good Friday reports. A generic goal gives a generic result, whereas pointing the agent at an existing app is like handing it a very specific requirements document without typing one out [2:25].

**3:14 Rebuilding App Features.** He demonstrates a Loom-style recorder with a movable, resizable camera bubble, countdown and pause. It copies the behaviour, not the look, and stores recordings locally instead of in the cloud. He also describes an Instagram content analysis tool, built by pointing the agent at a product whose name the captions garble (it reads as Sandcastles), and an automation evaluation studio inspired by Langfuse (that name is garbled too). At 4:48 he pauses to promote a free website design skill.

**5:20 How REA Works.** A bakery analogy: you buy a cake you love, pull it apart, taste it and test your own version until it matches. The agent does the same with an app: inspects files and behaviour, gathers evidence, builds, compares and iterates. Herk says it works well because the agent is pointed at a concrete end result, like asking for one specific cake rather than just a cake [7:10].

**7:36 A Five-Step REA Workflow.** After asking Claude Code with REA to reverse engineer REA itself, Herk lists five steps: pick a feature, route by build, summary first, seen/inferred/unknown, rebuild and test. He explains step one as pointing the agent at specific behaviour rather than the whole app, and says picking features works better than telling it to reverse engineer all of Loom. The full REA analysis of Loom ran past a gigabyte, so it stays on disk and the agent reads a shorter summary instead of rerunning it. Guesses must be labelled so they are not built on as facts. As an example of a seen finding he cites 11 custom native add-ons in Loom (his figure, unchecked).

**11:09 Limits and Caveats.** Never copy exact code or assets; there are legal limits. The tool only inspects what is already on your machine or reachable, not private servers. Some apps need different setup, and quality depends on the model. His cost idea: once the investigation is saved, a cheaper model may manage the build that previously needed a top-tier one.

**12:57 Results and Final Takeaways.** Herk says that when he gave two coding agents the same prompt, one with REA and one without, the one without always finished first while the one with REA was slower but gave much better results; he gives no timings or scores in the spoken account. He says the repo has about 192 thousand stars, from a page he last refreshed about 30 minutes earlier, and expects future models to absorb this behaviour. The captions garble the model names he lists near 13:34. The closing lesson: reverse engineer processes and skills too. Find someone who does it well, work out why it works, adapt it.

## Key ideas and claims

1. AI is not creative but executes a clear, specific vision well; a generic goal gives a generic result. [0:48, 2:25]
2. Build skills by studying finished examples, frame by frame, rather than describing the style in words (30 best reels became an editing skill). [0:48, 1:36]
3. An existing app serves as a more specific requirements document than one you would type out; Herk applies the same logic to finished examples of any output, such as reports. [2:25]
4. Clone the behaviour, not the look; Herk's Loom-style recorder differs visibly and keeps files locally. [3:12, 4:00]
5. The repo's value is a practical framework for studying and iterating, not a new technique. [4:48]
6. Point the agent at specific features, not a whole product. [7:10, 7:58]
7. Work out what the target is built with before choosing analysis tools. [7:58, 8:48]
8. Keep heavy analysis on disk and work from a short summary; avoid rerunning it. [8:48]
9. Tag findings seen, inferred or unknown, and do not build on inferences as if they were facts. [9:34]
10. Rebuild, then run test cases and iterate; do not ship because it looks finished. [10:21]
11. Do not copy exact code or assets; results depend on the model doing the work. [11:09, 11:58]
12. Saved investigation evidence may let a cheaper model do a build that once needed a stronger one. [11:58]
13. Claimed result (Herk's own, no figures given): the agent using REA was slower but produced better output than the one without it. [12:45]
14. The method generalises to business processes and skills, not only software. [14:23]

## Tools, products and repos mentioned

| Name | What it is | Link |
|---|---|---|
| REA (Reverse Engineer Anything), morluto/rea | MIT-licensed command-line tool and MCP server, plus an agent skill, for analysing binaries, Electron and JavaScript apps, .NET assemblies, Android packages and websites. Version 6.5.0 in the clone. | https://github.com/morluto/rea (README also names rea.tools and the npm package rea-agents) |
| Ghidra, Hopper, IDA, JADX | Existing analysis tools REA can use for native and Android work (from the README; none is named in the video, though one commenter mentions Ghidra) | no link given |
| Claude Code | Anthropic's coding agent, used with REA | no link given |
| Opus 5.5, Sonnet 5.5 | Models Herk contrasts on build cost [11:58]; version numbers are as captioned | no link given |
| Loom | Commercial screen recorder used as the reference app | no link given |
| Herk's screen recorder, Instagram analysis tool | His own builds from this method. The captions garble the recorder's name and the product the analysis tool was modelled on | no link given |
| Eval Studio (name garbled in captions) | A tool his team built for evaluating automations, inspired by Langfuse | no link given |
| Langfuse | Observability and evaluation tool used as inspiration | no link given |
| Glide | Named at about 3:12 beside his landing-page example. The captions may garble it, and it is unclear whether it is the reference site or a tool | no link given |
| Scrollcraft | Herk's own free website design skill, promoted at 4:48 (self-promotion, not a sponsor). The GitHub description of nateherkai/scroll-craft (in repos.json) matches his account, an agent skill for scroll-driven websites, so it is probably the same item. The description link is truncated; his own comment in videos/03.json shows the sign-up page, so the free copy may sit behind an opt-in. | https://github.com/nateherkai/scroll-craft and https://app.aiautomationsociety.ai/optin/scrollcraft/ (tracking parameters removed) |
| Glaido (voice to text) | In the description only, not mentioned in the video: a free month through his referral link. Promotional; not described as a sponsorship. | https://get.glaido.com/nate |
| Hostinger VPS | In the description only, not mentioned in the video: hosting with a 10% discount code. Promotional; not described as a sponsorship. | link truncated in description |
| AI Automation Society (Skool) | His community. He says two companion documents on REA are in the free community [7:10, 12:45]; I could not see them. The description also claims an agency grown to over $1 million a year, which is self-reported | links truncated in description |

No sponsor is named in this video. The sponsorship-enquiries line in the description is only a contact address for would-be sponsors.

## How to apply it

This is partly a setup and method walkthrough, though not one that suits a frame-making practice (see relevance). The five steps, generalised:

1. Pick one behaviour or output you want, not the whole product.
2. Tell the agent what the example is made of (stack, file type, system) so it picks suitable tools.
3. Have it save a full analysis to disk, then work from a short summary and drill down only when a question needs it.
4. Make it label every finding as seen (with evidence), inferred (a guess) or unknown, and treat inferred items as unconfirmed until checked.
5. Have it build a version, run real test cases, compare with the example, and repeat.

Herk's labels are seen, inferred and unknown; the repo's skill file uses the near-equivalent observations, inferences and unknowns. For software targets the README says setup is `npx rea-agents setup`. I did not run or install anything.

## What viewers said

Comments are opinion, not fact. Names are omitted.

- Pushback: several viewers said this is not new. One said they had already run language-model-driven binary analysis with the Ghidra decompiler, and that REA drives the same tool through a generic layer; others said good prompting, vision and planning already covered it, and that the novelty is speed. One said enterprises are not doing this to commercial software and that real algorithm work differs from prompting. Another called REA poorly designed and said they would not install large clones made by strangers over a weekend.
- Corrections: the most-liked comment (27 likes) says REA reads actual decompiler output and re-tests until results match, which suits cases needing exactness (such as device emulation) more than copying a feature. The README confirms REA drives decompilers; I did not verify the automatic re-test loop.
- Misuse: two viewers described rebuilding a paid plug-in (called Meta tune in the comments) so it works without payment. The repo's own disclaimer rules out circumventing DRM and licence checks. One person reported a session being flagged by the model's safeguards.
- Questions: how to point the agent at a site (built-in browser or Chrome extension), what to use for frame-by-frame video analysis, standalone apps versus an editor setup, how to start a manufacturing report automation, and how the video was edited.
- Useful additions: one wrote that agents should save a plan to a Markdown file first, then run a second pass that looks for weaknesses in it, and reuse the file to recover after context compaction. Another reserves money-moving code for changes only the human can approve.

## Relevance to Winstanley & Son

- Reverse engineering software is not a fit. REA targets binaries and apps; nothing in the estate needs it, and decompiling the practice management system or supplier portals would risk licence and terms-of-service breaches. The UK legal position was not researched here.
- The transferable idea, show the agent finished examples of what you want, sits close to what is already live: the lens-ordering flow works from a redacted copy of the real order sheet, and the five-stage change gate starts from evidence and proves changes in the test channel with realistic phrasings. This video confirms the approach rather than adding a new one.
- Genuinely new for the practice: use the practice's own best outputs as the reference for the weak spots the owner's notes name. Social captions are generic and review requests are paused. A short exemplar pack of top-performing posts, the live Stannp recall and reactivation letters, and replies the owner liked would give a drafting account something specific to match. The estate notes treat generic captions both as a gap and as a deliberate play-safe rule, and staff or customer posts need owner approval, so any change there needs the owner's say.
- The seen / inferred / unknown split is a three-way version of the CMO's proven-or-reported flag and the CEO's not-measured rule (both planned, not yet live). Adding inferred is new, and suits data hygiene and benchmarking reports.
- Summary first and cheaper model after investigation match how the CEO facts pack is designed and the existing split where Fable orchestrates and Sonnet builds. Nothing new beyond testing downgrades on saved examples; the agent-stress-test skill already covers the method, and the CFO build plans similar golden-question tests.
- Do not take from this video: any auto-build of lookalike tools. Gaps such as the missing scorecard are better solved natively first.

## Account or role ideas this video suggests

1. **Exemplar Librarian** (reports to AI CMO; from [0:48] and [2:25]). Mission: maintain a small, owner-approved library of the practice's best proven outputs (recall letters by response, posts by reach, replies the owner liked) with a short note on why each works. Inputs: CMO ledger counts and owner picks, never named patients. Outputs: exemplar pack and style notes other accounts read before drafting. Guardrails: no patient data, no trading volumes, no contact-lens content; owner approves what enters.
2. **Findings Labeller** (reports to AI CIO; from [9:34]). Mission: check every weekly pack and audit before it reaches the owner and tag each claim seen, inferred or unknown. Inputs: draft packs from the CEO, CMO and CFO accounts. Outputs: labelled copy and a list of unsourced claims. Guardrails: read-only, edits nothing, sends nothing.
3. **Process Benchmarker** (reports to AI CMO; from [7:10] and [14:23]). Mission: study one well-run independent practice process at a time (new-patient welcome, booking page, review ask) from public material only and write a labelled report. Outputs: a benchmark note and one proposed change for the change gate. Guardrails: public sources only, no copying text or images, no logins, no prices or contact-lens suggestions.
4. **Model Cost Tester** (reports to AI CIO, copied to AI CFO; from [11:58]). Mission: replay saved, pseudonymised examples of stable jobs through a cheaper model and report whether results match, reusing the agent-stress-test skill and the CFO's golden-question approach. Guardrails: fixtures only, never switches a live model, owner decides.

## Sources used and confidence

Sources: the full transcript (captions, auto-generated); the description, chapter list and top public comments in videos/03.json (comments are opinion only); the morluto/rea clone (README, DISCLAIMER.md, the reverse-engineer-anything skill file, LICENSE, package.json), read but not run; the estate context file; GitHub's public API for the star count and licence; and web searches. The search returned the repo plus third-party explainers and one hands-on test of REA by another reviewer. I found no with-and-without comparison, so Herk's speed and quality claim stays unverified. GitHub showed about 297,700 stars for morluto/rea on 17 October 2026, so Herk's 192 thousand a few days earlier is not contradicted; the lower counts in search results were from earlier dates. Apart from the repo's own skill file and AGENTS.md (instructions for coding agents by design, read only as data), I found no text addressed to an AI assistant in the transcript, description, comments, README or disclaimer.

Herk says Claude Code produced the five-step list when it analysed the REA repo. The skill file covers three of the five in its own wording (route the target first, work summary-first, separate observations, inferences and unknowns) and does not present these five steps as a list. Confidence: medium-high on what Herk said; medium on the five-step framing; low on his performance claim and on the unchecked remarks (the commentator's joke and the Loom add-on count). Not researched: the UK legal position on decompiling licensed software. Relevance judgements rest on the estate context file supplied, not on any live check.

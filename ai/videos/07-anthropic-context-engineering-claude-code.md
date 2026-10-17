# Anthropic Engineers Just 10x'd Everyone's Claude Code

- **Channel:** Nate Herk | AI Automation
- **Published:** 8 October 2026 | **Duration:** 12:23 | **Views:** 108,798 (as collected on 17 October 2026)
- **URL:** https://www.youtube.com/watch?v=oz2CwrPV2Rg
- **Guests:** none

## What the video covers

Nate Herk (Nate from here on) argues that the long, rule-heavy instruction files many Claude Code users have built up now work against the newest models. He starts from an Anthropic article on context engineering for Claude 5 generation models, which reports that Anthropic removed over 80% of Claude Code's own system prompt with no measurable loss on its evaluations. From that he draws a working rule: give the model the smallest amount of context that still gets a good result. Keep what it cannot infer (your voice, audience, goals and the reason for the task) and drop what it can look up or what is repeated elsewhere.

He backs this with one informal test, in which a stripped-down setup produced a better-structured student guide than his fully loaded one, and with a tour of the /doctor command, which audited his skills, memory files and settings. He then uses a plain audit prompt to find one small fix in his YouTube script workflow. He ends by recommending regular audits, monthly or quarterly and after every new model, and scheduling them so recommendations wait for approval. A paid Hyperagent segment sits in the middle.

## Chapter-by-chapter

**0:00 Anthropic's New Context Rules.** Nate says Anthropic engineers cut over 80% of Claude Code's system prompt for the Claude 5 generation, which he reads as overturning the habit of giving Claude as much information as possible. He ties this to Boris Cherny's reported advice to delete your skills every six months, and to Anthropic's example of a hard limit on code comments being replaced by an instruction to follow the surrounding style. He adds that rules pile up after each mistake and outlive the model that needed them, then restates his advice to define what done looks like: outcome, reason and constraints. He cites a 2025 paper where accuracy fell as input grew, warning that its percentages do not predict what trimming a personal file will do, and then Anthropic's figures for loading MCP tool definitions only when needed, which he presents as measured support for the idea. The captions render the article author's name as Thoric (the post itself names Thariq Shihipar) and CLAUDE.md as Claude 3 MD.

**3:30 Hyperagent (Sponsor).** A paid advert aimed at agencies building agents for clients. The pitch is a separate workspace per client, so agents, skills, memories and documents stay inside one boundary, with builders able to edit and client staff given a role that can run agents but not change system prompts, swap models or delete skills. No evidence is offered.

**4:13 Testing Claude With Fewer Instructions.** Nate says he has tried extreme versions on his own setup, such as copying it and removing CLAUDE.md and skills, then running the same job. His example turned a Boris Cherny interview into a student guide: the full setup made the prettier document (branding, usual links, personal context), while the fresh version he compared it with was plainer but better organised, grouping ideas and adding timestamps. He says he would build a new skill for branding only (header, font, footer, logos) and leave the model to structure the content, because the old guardrails were written for earlier models such as Opus 4. This is one example judged by Nate himself, with no repeat runs described.

**6:01 What Context To Keep.** He likens over-specifying to handing an experienced designer a first-timer's checklist; that comparison and the list of context worth keeping begin at about 5:35, just before this marker. He keeps what Claude cannot work out (voice, goals, audience, how the business runs, and the reason for a request, which he files under the context part of what he calls the four C's of an AI OS) and questions anything it can look up, such as a long folder listing, repeated instructions, and procedures that matter only for one task, such as his video-editing process when he only wants a script. CLAUDE.md stays as a useful starting point: what the project is for, known traps, and pointers to deeper instructions.

**7:04 Auditing My Setup With /doctor.** Nate ran /doctor in a new session and it reviewed skills, memory, plugins, settings and installation. Its table showed each skill's location, recorded uses and the estimated token cost of its listing (the front matter used to find the skill), and flagged 18 older skills with no recorded use while sparing recent ones. It drew on 50 recent sessions from the project plus lifetime counters (252 startups, 223 transcripts). He says to review the list before deleting, especially for skills used through another tool. It also found duplicated sections, about 2,250 characters of possible cuts (roughly 563 tokens), another project's CLAUDE.md loading from a separate folder (about 2,000 tokens) and two broken skills, a wrong file name and faulty front matter, then offered to fix them. The caption near 8:43 garbles where that extra file loads into (it reads Herc, probably here), and the file's own source is given as a separate video project in his desktop folder; the wording is a best reading.

**9:43 Fixing My YouTube Workflow.** Nate's prompt asked Claude to audit the repo, find the smallest change that speeds the path from raw idea to filming-ready script, cite the exact files and edit nothing yet. Claude mapped idea, research, outline, script and teleprompter file, then found a weak handoff: the outline skill need not save its evidence where the script skill could check it, and the script skill carried a hard rule to re-verify facts. Of 25 video folders with a script, only three had a sources file; Nate adds that this does not mean the others had no research, only that the handoff was inconsistent. It proposed three edits across two skills, which he approved. One sentence in the 10:17 segment, about wanting the next step to have the evidence in front of it, is garbled by the captions.

**10:51 Scheduling AIOS Audits.** He recommends an audit monthly if the setup changes often, quarterly if stable, and whenever a new model arrives, since each reads instructions slightly differently. Once the audit prompts are trusted, a local scheduled task in the Claude desktop app (he says to leave the app open) could leave recommendations to approve or decline. His case is that human inconsistency, such as forgotten updates and duplicates, is the weak point of personal AI operating systems.

**12:11 Final Thoughts.** The sign-off only: thanks, a request to like the video, and goodbye. The substantive closing thought falls just before the marker, in the 11:53 segment: a self-cleaning, self-improving AI operating system, and then the next problem of keeping a team in sync rather than each person building their own.

## Key ideas and claims

1. Anthropic reports removing over 80% of Claude Code's system prompt for Claude 5 generation models without measurable loss on its evaluations [0:00]. This is a company reporting on its own product, and the figure concerns Anthropic's system prompt; Nate's claim that most of a user's own information slows Claude down goes further than that figure tests.
2. Rules written for older models can become too restrictive; the code-comments limit is the example, replaced by a style-matching instruction [0:46].
3. Rules accumulate after each mistake, get duplicated across CLAUDE.md and skills, and stay after the model improves [0:46, 1:34]. Cherny's six-monthly skill deletion advice is relayed by Nate with no source [0:46].
4. Define done by outcome, reason and constraints, then leave the model room to work [1:34].
5. Anthropic's applied AI team recommends the smallest context that gets the result; Nate's own version adds highest quality at the lowest cost. Minimal is not the same as short [1:34, 2:22].
6. A 2025 paper tested five models on maths, question answering and coding and found accuracy fell as inputs grew, even where the models could still find the relevant material, with reported drops of 13.9% to 85%; Nate cautions these were controlled experiments on older models [2:22].
7. Loading MCP tool definitions only when needed cut token use by 85% in Anthropic's example and lifted its MCP evaluation scores from 49% to 74% (Opus 4) and 79.5% to 88.1% (Opus 4.5), with the tools still available to Claude [2:22, 3:13]. These are Anthropic's own reported results.
8. Keep context the model cannot infer: voice, goals, audience, how the business works and the intent behind the request [5:35, 6:22].
9. Nate would keep branding in a skill and let the model decide structure; he says his old guardrails confined a stronger model [4:47].
10. Keep CLAUDE.md as a useful starting point and load task-specific procedures only for that task [6:22].
11. As Nate shows it, /doctor can report recorded skill usage, token cost of listings, duplication, stray instruction files and broken skills; the owner reviews before deleting [7:08, 7:55]. Third-party web results attribute the per-skill usage report to a separate /skill-doctor command, which is unconfirmed against Anthropic's documentation.
12. Repeat the audit monthly or quarterly, at each model change, and eventually on a schedule with approve-or-decline output [10:17, 11:05].

## Tools, products and repos mentioned

| Name | What it is | Link |
|---|---|---|
| Anthropic article, *The new rules of context engineering for Claude 5 generation models* | The post the video is built on. The post's page, fetched on 17 October 2026, names Thariq Shihipar as author, dates it 24 July 2026 and states the over-80% system prompt claim | no link given in the video or description; found by web search at https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models, which redirects to a claude.dev copy |
| Claude Code, /doctor, desktop-app scheduled tasks | Anthropic's coding agent, its diagnostic command and recurring local tasks; the files audited are CLAUDE.md, skills, auto memory and CLAUDE.local.md | no link given |
| Models named (Opus 5, Fable 5 and 5.1, Opus 4, Opus 4.5) | Versions behind the claims | no link given |
| Hyperagent (sponsored) | Platform with per-client agent workspaces and role-limited staff access | https://www.hyperagent.com/nate100 and https://www.hyperagent.com/agencies |
| Nate's free community (plugged at 9:30) and AI OS template (description) | His own promotional resources | link truncated in the description; no usable link given |
| Glaido voice-to-text (promotional) | Dictation tool in the description, not discussed in the video | https://get.glaido.com/nate |
| Hostinger VPS (promotional, discount code) | Hosting offer in the description, not discussed in the video | link truncated in the description; no usable link given |
| Boris Cherny interview | Referred to, not identified by title | no link given |
| 2025 input-length paper | Not named in the video. A web search matches it to *Context Length Alone Hurts LLM Performance Despite Perfect Retrieval* (arXiv 2510.05381, October 2025), whose abstract gives the same 13.9% to 85% range | no link given |
| Anthropic's tool-loading results (85% token cut; 49% to 74%; 79.5% to 88.1%) | Not sourced in the video. A web search matches the figures to Anthropic's own engineering post on advanced tool use (November 2025), where Anthropic reports them as results of its own testing | no link given |

## How to apply it

This is a repeatable audit routine rather than a build. The order below is the summariser's arrangement of Nate's points, not a procedure he states:

1. Run /doctor in a fresh Claude Code session, as Nate did, and read the report before accepting any fix.
2. Check the usage and token-cost table (if it does not appear, the separate /skill-doctor command named by third-party sources may be the source). Before removing a skill with no recorded use, confirm it is not used through another tool.
3. Look for the same instruction in more than one place, and for instruction files loading from unexpected folders.
4. Fix broken skills (wrong file names, faulty front matter) so descriptions are actually seen.
5. For a skill you suspect is over-written, run the same task with and without it and compare. Keep the specifics only you can supply, such as branding.
6. Use a propose-first prompt on one workflow: audit it, name the smallest change, cite exact files, edit nothing.
7. Read what each proposed change touches before approving (Nate approved his three edits together), then repeat monthly or quarterly and after each model change.

## What viewers said

- **Pushback:** The most-liked comment mocks the endless 10x titles. Several viewers called the topic old news or outdated, one asking what the point was of publishing a year later. The Anthropic post is dated 24 July 2026 on the post's page, about eleven weeks before the video, so a year is wrong, though the topic was not fresh. Others called it hype, AI-made or thin on detail. One found it counterintuitive that less detail helps; another said enterprise software needs plenty of context. One said Claude still writes a lot of code comments and follows surrounding style poorly, which cuts against the video's comments example.
- **Questions:** Where can viewers get the doctor tool Nate shows (one viewer called it a skill), and is the audit command a viewer says he uses (called /audit there, though the transcript names only /doctor and his own audit prompts) his own and shared? Why are the Anthropic sources not linked? Do skills still matter if Claude loads them itself? One Cowork user complained that uploaded skills cannot be edited in place.
- **Confirmations:** One viewer cut a bloated setup from over 60,000 tokens at chat start to about 20,000 and reported better quality, speed and lower usage. Another said models need less spelling out of obvious steps such as git. One liked the trim-not-pile-on takeaway, though another found keeping up exhausting.

These are opinions and anecdotes, not evidence.

## Relevance to Winstanley & Son

- **Already live, so not new:** a short router CLAUDE.md, memory index, dated handoffs, shared short skills and an on-request `ai-system-audit` skill. Much of the video's structure advice is how the estate already runs.
- **Partly new:** that skill already checks duplication, staleness and demonstrated usefulness, so the duplicate check is not new. What the video adds is measured numbers (recorded skill usage and token cost per listing) and a schedule. Skills are shared with Codex, so Claude-only usage counts would undercount; never delete on those counts alone.
- **Trim style, not safeguards:** the 80% claim concerns a coding agent's system prompt. The strict supplier lens-line rule, patient-data rules, NHS wording and clinical recall limits guard against real harm and should stay. Any trimming of style or procedure goes through the existing test channel with realistic phrasings first, which is the video's compare-before-removing step.
- **Make-scenario prompts are untested ground:** /doctor audits local Claude Code setup, not prompts inside Make scenarios such as the reception agent. Any rewording there would go through the five-stage change gate.
- **Evidence file between steps:** the sources-file finding suggests each website guide could carry a short note of the primary source checked and the date, which matters for NHS eligibility wording. It also fits the planned AI CMO numbers ledger. Check whether guides already carry such notes.
- **Scheduled audit:** a read-only monthly or per-model-change instruction audit, recommendations only, fits the drafted AI CIO charter (watches, counts, reminds, never presses). The estate notes list nothing like it as live.

## Account or role ideas this video suggests

1. **Instruction auditor** (reports to AI CIO). Mission: monthly read-only audit of Claude Code and Codex instruction layers, a scheduled wrapper around the existing `ai-system-audit` skill. Inputs: skill usage counts, token costs, memory files, front matter. Output: one ranked page of proposed cuts, merges and fixes naming exact files. Guardrails: edits nothing, counts usage across both tools, leaves safety, compliance and supplier rules to the owner. From [7:08] and [11:05].
2. **Model-change re-tester** (reports to AI CIO). Mission: when a new model arrives, replay realistic staff phrasings against current and trimmed instructions in the isolated test channel, building on the existing `agent-stress-test` skill. Output: a pass or fail table of cards and messages, no live changes. From [4:13] and [11:05].
3. **Evidence-handoff checker** (reports to AI CMO). Mission: confirm each guide or landing page has a source note (primary source, date checked) before wording updates. Input: site pages and source notes. Output: list of pages missing notes. Guardrail: clinical and NHS wording is flagged for the owner, never auto-edited. From [10:17].

## Sources used and confidence

- Sources: the auto-generated transcript, the video description and its links list, about 40 public top comments (names stripped), and web searches and page fetches on 17 October 2026: the Anthropic post's page (title, author, date and the 80% claim confirmed from a page fetch, not a full read), search results matching the 2025 paper and Anthropic's tool-loading figures, and third-party posts about /doctor. The video links no repositories. Timestamps are the transcript's segment markers, roughly 45 seconds apart, so a point may sit slightly after the stamp. No text addressed to an AI assistant was found in the transcript, description or comments.
- **Confidence: medium.** What Nate said is clear from a short, readable transcript, and the article details and the paper and tool-loading figures now match published sources. Still unconfirmed: whether the article itself repeats the tool-loading figures, the Cherny advice (relayed with no source), the exact behaviour of /doctor against Anthropic's documentation, whether the audit command a viewer asked about is Nate's own, and the 25-folder, three-sources-file and 563-token figures, which come from Nate's private setup.

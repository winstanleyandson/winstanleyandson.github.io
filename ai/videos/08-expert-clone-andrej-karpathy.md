# I Built Another Andrej Karpathy Using Claude

- **Channel:** Nate Herk | AI Automation
- **Published:** 5 October 2026 | **Duration:** 10:45 | **Views:** 73,524 (as collected on 17 October 2026)
- **URL:** https://www.youtube.com/watch?v=bvGptCLDhyo
- **Guests:** none

## What the video covers

Nate Herk (Nate from here on) shows how he turned the public output of Andrej Karpathy, the AI researcher and teacher, into a helper inside Claude Code. It is not a voice clone. It is a small agent that works the way Karpathy teaches: build the smallest working version, say what you expect before running it, show the broken version, and never claim code works until it has been run.

Nate calls it a four-step recipe. His closing recap groups the steps as: give Claude everything the expert has published and compile it into a linked wiki; turn that into rules, each tied to an exact quote; make the agent run its code before it answers; and test it on real work. The build he walks through is more granular. A crawl with one agent per source collects the material. Claude compiles it into a wiki, following a note Karpathy wrote about LLM-maintained wikis. A rules step extracts the expert's rules with a quote and source for each. The rules are packaged as a sub-agent and a skill, a hook stops the agent finishing until its code has been run, and the result is tested on real work. A last skill adds new material from a single link.

It is a demonstration. The transcript describes no side-by-side against ordinary Claude, and the description gives no download link for the finished agent. Nate's pitch is that the same recipe works for any teacher, author or coach.

## Chapter-by-chapter

Timestamps are the video's chapter markers. Transcript blocks run about 48 seconds, so a cited moment may sit a little either side of its marker.

**0:00 Karpathy's brain.** A short cold open. Nate says he has turned Karpathy into a Claude agent and promises four steps. He calls him one of Anthropic's lead engineers, which is looser than the pre-training role he describes next.

**0:18 Who is he?** A short biography: founding member of OpenAI in 2015, about five years leading AI at Tesla, then education work and Eureka Labs, and since May 2026 the pre-training team at Anthropic. Nate insists the build is neither an impression nor a voice clone. It captures how Karpathy explains things, through seven rules drawn from his own writing and lectures.

**1:07 Why bother?** Ordinary Claude can over-explain or make things up, leaving you more confused, and client work then ships code nobody can fix. Nate says Karpathy posted in August 2025 that Claude Code would not teach while it wrote code. His wider argument: output quality depends on the expertise in the system, nobody is expert in everything, so pull a real expert in, talk until you understand, then wire that knowledge into your own skills and workflows. He plugs his free AI OS kit near 2:23.

**2:47 700K words.** The build runs in Claude Code with six prompts shown on screen. Step one is collection: blogs, lecture transcripts, code repositories and posts on X. Captions come from two free Python packages, and X posts from a paid service that cost roughly a dollar for everything since 2023. The crawl prompt names each source and its tool, runs one agent per source in parallel and records what was fetched. It took 45 to 60 minutes and produced over 700,000 words in a raw folder. Pointing Claude straight at it would work badly, he says, because it is too messy to search.

**3:50 His own wiki.** The fix is Karpathy's April idea: an LLM reads untouched raw files and compiles linked pages, an index and a log, so questions can follow relationships. Nate pastes Karpathy's gist into prompt two and aims it at the raw folder. The result is viewed in Obsidian, which is optional. It holds a page per source plus topics, principles, rules, methods, and how he explains and debugs. Links run both ways between rules and sources.

**5:37 7 rules.** Prompt three extracts the rules. Each must carry an exact quote and its origin, and where there is no source the agent must say it is inferring. The seven, in my words: build to understand; start with the one term that matters and add one thing at a time; state the expected result, run, then compare; show the wrong version first; prove rather than claim; state your assumptions; prefer the simpler option. In Obsidian a quote opens its source page. The transcript drops a word where Nate says what the rules are pulled from (probably the wiki), so that detail is not relied on.

**6:42 Mini Karpathy.** Prompt four turns the rules into two files. The first is a sub-agent, which Nate explains as a separate Claude with its own instructions, memory and context window. It holds the rules, how it talks and the loop it runs on every task. The second is a skill: a slash command plus what you are stuck on sends the task to the agent, which then grades its answer against a one-line-per-rule checklist.

**7:38 Run it first.** Prompt five adds a run gate, a hook that fires when the agent tries to finish. If code was written and never run, the hook blocks the answer and tells it to run the code. Nate says you do not write the hook yourself; the prompt asks Claude to. His first test is a byte pair tokeniser build. The agent defines what done means, builds the smallest version, states its expectation, runs it, shows a version that breaks and why, fixes it, then lists what ran and which rule applied.

**8:48 Would it ship?** A review test: would the client accept this, and what would they delete? A comment-pulling script that ran for Claude is predicted to crash on an emoji in a standard Windows terminal, and it does, before writing any files, so working was true only in one setting. The agent trims the script and runs old and new side by side. Nate then ingests a link to Karpathy's July post about dictating to a model for about ten minutes and having it tidy the text: the skill adds a source page, updates the pages it touches, promotes a one-source rule to a real rule on a second source, and refreshes the index, a hot page and the log. A recap and sign-off follow.

## Key ideas and claims

Timestamps are the start of the transcript block containing the idea.

1. Clone the method, not the voice: the agent encodes seven working rules taken from the expert's own material. [0:48]
2. The target failure is an assistant that sounds right instead of being right, over-explains and does not teach while coding. Nate cites an August 2025 Karpathy post on this; a web search found no sign of it. [0:48, 1:35]
3. Output quality is capped by the expertise in the system, so pull a real expert's public material into the project and wire it into skills and agents. [1:35]
4. Collect with one agent per source and a suitable tool for each, writing down what was fetched. Nate reports 45 to 60 minutes and over 700,000 words. [3:10]
5. Leave raw files untouched and compile a linked wiki with an index and a log, so retrieval follows relationships rather than searching a heap. [3:58]
6. Every extracted rule needs an exact quote and source, and a rule with no source must be labelled as inferred. This is the control against invention. [5:33, 6:20]
7. Package the rules as a sub-agent for the thinking and a skill that routes tasks and grades answers against a checklist. [6:20, 7:08]
8. Enforce process in code: a hook blocks the final answer when code was written but not run. [7:08]
9. Test by predicting before running, by showing the broken version, and by asking whether the client would accept the work. His example script worked in one environment only. [7:56, 8:43]
10. The brain compounds: one link in, and the affected pages, a one-source rule that gains its second source, the index and the log update without hand edits. [9:31]
11. Closing principle, which Nate says Karpathy said this year: "you can outsource your thinking, but you cannot outsource your understanding." Secondary web pages attribute a near-identical line to a 2026 Karpathy interview; I found no primary source. [10:20]

## Tools, products and repos mentioned

No GitHub repositories are linked in this video.

| Name | What it is | Link |
|---|---|---|
| Claude Code | Anthropic's coding agent; the whole build runs in it | no link given |
| Sub-agent, skill, hook | Claude Code features: a separate Claude; a command-run instruction set (`/karpathy-teach`, `/karpathy-ingest`, names as heard in the captions); a script that can block finishing | no link given |
| YouTube Transcript API, yt-dlp | Free Python packages Nate used to pull YouTube captions | no link given |
| twitterapi.io | Paid API for X posts; about a dollar for his pull | no link given |
| Karpathy's LLM wiki gist | Karpathy's note on compiling raw sources into a maintained wiki. Nate says it is in the description, but it is not in the captured links. Web search found only secondary write-ups dating it April 2026 | no link given |
| Obsidian | Note app that shows the wiki's pages and links; optional | no link given |
| AI OS kit | Nate's own free template sign-up (lead magnet), plugged at about 2:23 | https://app.aiautomationsociety.ai/optin/ai-os/ (from Nate's own comment on the video, tracking tags removed; the description copy is truncated) |
| Agency playbook | Nate's own free sign-up (lead magnet), listed in the description; not mentioned in the video | truncated in the description; the one captured link is https://app.aiautomationsociety.ai/opaa-ads-optin, probably this one by elimination, not confirmed |
| Skool | Nate's free resources page on Skool, a community platform; listed in the description | truncated in the description; no link given |
| Glaido | Voice-to-text app, free month. Promotional link in the description's tools list; sponsorship not stated; not mentioned in the video | https://get.glaido.com/nate |
| Hostinger VPS | Hosting with a 10% annual-plan code. Promotional link in the description's tools list; sponsorship not stated; not mentioned in the video | truncated in the description; no link given |

## How to apply it

This is a build walkthrough. Steps as Nate shows them:

1. Choose an expert and a goal. (My addition, not in the video: check you may copy their public material, including paid sources and their terms.)
2. Run the crawl prompt: one agent per source, one tool per source type, a written record of what was fetched, a raw folder with a subfolder per source.
3. Paste Karpathy's wiki note and tell Claude to compile the raw folder into linked pages with an index and a log. Obsidian is optional.
4. Extract rules, each with an exact quote and source, or an explicit inferred label.
5. Turn the rules into a sub-agent file (rules, voice, loop) and a skill (routes the task, grades against a checklist).
6. Add the run gate: a hook that blocks finishing when code was written but not run.
7. Test on one real build and one real review.
8. Add an ingest skill for new links. The transcript does not describe creating it, and a viewer says the prompt is not shown.

## What viewers said

About 30 comments were captured. They are opinion, not fact.

- **Pushback:** one viewer fears it would look like a gimmick that clutters Claude's thinking, adds bias and drifts from the original goal. Another asks whether it inflates output and usage cost. A third is confused and asks for a practical example and a reason to build it.
- **Questions:** where the gist link is (one viewer asked two days before collection); where the ingest skill is created; why six prompts are promised when only five cards could be found; whether the wiki belongs in a second-brain vault or apart; and how long setup takes. One viewer also reports that the agent is missing from the quarter's resource sheet and had hoped to download it.
- **Confirmations and extensions:** several say they built something similar, such as a library of this channel's videos. One suggests pairing it with Karpathy's autoresearch repository. Two want the same treatment for Alex Hormozi, one asking for a repository. Most of the rest is thanks.

## Relevance to Winstanley & Son

- **Already live, so nothing to copy:** Claude Code with a router file, memory index, dated handoffs and short shared skills; a five-stage change gate with Codex as sole reviewer; and a test channel where checks assert on artefacts, not status codes. The video's prove-it and would-the-client-accept-it habits already exist there as process.
- **New, a source-cited rules wiki:** the AI CMO plan wants a plain-Markdown knowledge folder, and the AI CEO plan wants a source and date on every figure. The raw, wiki, index, log pattern and the quote-or-label-inferred rule give that folder a structure and an ingest loop. Best content is what must be stated accurately: NHS eligibility, data protection guidance, advertising rules, from official public pages only.
- **New, a mechanical run gate:** the estate's change gate is a process (review, contained import, owner press), and its context notes list no automatic stop on a build agent finishing. A hook could stop a build agent finishing until its checks have run. It must use offline suites on sanitised copies, never live scenarios, tokens or patient data.
- **New and modest, a teach mode:** a skill that explains an automation through a small example, expectation versus result, a broken case and listed assumptions helps staff and owner understand a flow without reading code.
- **Ignore the clone itself:** a machine-learning teacher helps a small independent frame maker little. The method transfers; the persona does not, and attributing opinions to a named living person needs care.
- **Caution:** this repository is public, so a wiki built from anything internal must live outside it.

## Account or role ideas this video suggests

1. **Rules Librarian** (reports to the AI CIO). Mission: keep a cited wiki of public rules the practice must state accurately. Inputs: official public pages fetched by script. Outputs: pages, index, log, a weekly list of uncited or changed rules. Guardrails: exact quote and URL or an inferred label; no patient data; the owner approves any wording change. [3:58, 5:33, 9:31]
2. **Build Verifier** (AI CIO). Mission: stop a build agent finishing until its code has run against offline fixtures. Output: a pass or block note, logged in the AI CIO's planned change register. Guardrail: offline only. [7:08]
3. **Plain-English Tutor** (owner). Mission: explain an automation or report using the smallest example, expected versus actual result, a broken case and listed assumptions. Guardrail: copies and fixtures only. [0:48, 7:56]
4. **Ship-Check Reviewer** (AI CIO). Mission: before a package reaches Codex or the owner, ask what the owner would accept and delete, test in the setting staff actually use (an extra step ahead of the existing review and test channel), and compare trimmed against original, aiming for fewer review rounds. [8:43]
5. **House-Style Brain** (AI CMO). Mission: hold cited rules from the marketing writers the letter house style follows (business-context.md names Hormozi and Kennedy), as a checklist for drafts before the owner sees them. Guardrails: short quotes, public sources, counts not named patients. [1:35, 7:08]

## Sources used and confidence

- Transcript (auto-generated, with name errors and one garbled line in the block starting 5:33), the description (several links truncated), 31 top comments including one by the creator. No repositories linked.
- Web searches, treated as data. Reports from 19 May 2026 (Axios among them) say Karpathy joined Anthropic's pre-training team, matching the video. Secondary write-ups date the wiki note to April 2026; the gist itself was not found. Secondary reports dated 24 July 2026 corroborate the voice-rambling post. No trace of the August 2025 post turned up.
- Confidence: high on what the video says; medium on external claims. Karpathy's May move, April note and July post are corroborated by secondary reports only. His August 2025 post and the exact wording of the closing quote are not confirmed from a primary source. Nate's word counts, timings and costs are self-reported, and demo outputs seen only on screen cannot be confirmed from the transcript.

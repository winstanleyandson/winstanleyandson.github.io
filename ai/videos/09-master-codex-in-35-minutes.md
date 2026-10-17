# Master 96% of Codex in under 35 minutes

- Channel: Nate Herk | AI Automation
- Published: 3 October 2026 | Duration: 34:34 | Views: 80,634 (as captured on 17 October 2026)
- URL: https://www.youtube.com/watch?v=DFlELTiSPk8
- Guests: none
- Disclosure: the description tags OpenAI, carries #ChatGPT_Partner, promotes a voice-to-text tool, a hosting discount code and his own community, and invites sponsorship enquiries. No payment is stated; treat as possibly promotional.

## What the video covers

Nate Herk tours 18 core ideas in OpenAI's Codex desktop app for a non-technical viewer, in four parts: foundations, environments, control and customisation, and tools and scale. He uses Codex as a general work assistant, pointed at one folder on his own computer that he calls his AI operating system.

The through-line: a project is a folder of files, a plain Markdown rules file tells the agent where everything lives, and repeatable work becomes skills, written recipes he corrects after each run. He also covers where the agent runs (his machine, a cloud sandbox, or his phone steering the desktop), the model and effort dials and their cost, three permission levels, plugins and a logged-in browser, a hosting feature called Sites, subagents on cheaper models, scheduled tasks, and voice control of several threads.

Almost everything is shown on his own setup. It is a concept tour, not a build, and the cost and newer-feature claims are his own.

## Chapter-by-chapter

**0:00 Projects And AGENTS.md.** A project is only a folder of files and rules about him, so the agent builds up knowledge instead of starting cold. Asked for a month in review, it reads the folder and his earlier Codex chats. AGENTS.md is a readable rules file Codex reads before every message; his is mostly a routing map saying where business, voice, course and project material live.

**3:58 Agent Loop And Goals.** Codex, Claude Code and Hermes agent are harnesses: a model wrapped in a loop of thinking, using tools and replying. He shows the visible steps and says watching them teaches you a lot about how to work with the tool. The slash goal command keeps the agent going until a finish line is met, shown with a goal that made this video's motion graphics. At 8:45 he tells Claude Code users he kept a copy of his CLAUDE.md rules file as AGENTS.md and copied his Claude skills and settings into the Codex-side folders, or you can ask Codex to make the project Codex-ready. The folder names are garbled in the captions (probably .agents, .codex and .claude).

**9:54 Local, Cloud, And Remote.** Local means files and outputs that exist only on the machine in front of you; a localhost web address cannot be opened by anyone else. A chat can run locally or in a cloud sandbox, which hides the model and permission pickers. He rarely uses cloud, because a machine left switched on feels much like one. The ChatGPT phone app's Remote tab shows the same Codex threads, so he can steer the desktop session from anywhere.

**13:25 Worktrees And Codex Settings.** A worktree is a copy of the project for risky experiments, merged back afterwards. He almost never uses them for knowledge work but says they appear in the interface. The Codex settings folder exists twice, inside the project and at user level (memories, sessions, automations); when unsure, ask Codex, which can search its own documentation.

**16:10 Models, Tokens, And Usage.** A model can be chosen per chat and switched between messages. The strongest costs most and drains the weekly limit fastest, with at least two cheaper tiers below (the names are spelled inconsistently in the captions). He explains API pricing per million tokens versus subscription limits and extra credits, and what a token is.

**19:18 Effort And Permissions.** Effort runs from low to extra high, with an ultra level that needs full access, plus a fast mode he puts at about 1.5 times the speed for more usage. He calls the top model at high effort overkill for writing an email, and uses the middle tier at medium for ordinary knowledge work. Permissions are full access, ask for approval, and approve-for-me, which interrupts only for actions judged unsafe. He suggests starting on ask for approval; hard blocks can go in config files.

**21:38 Skills And .agents.** A skill is a recipe: do a task well once, then correct the recipe when a result is off. Across two requests on a local video file, Codex used six of his skills (YouTube description, timestamps, LinkedIn post, X article, X article from video, and X article formatting), which he confirmed by asking it which skills it had used. A skill is a Markdown file with a name, a when-to-use line and instructions, and it can point at other skills, scripts and style guides. It runs by plain request or slash command, at project or user level.

**25:03 Plugins And Browser Use.** Plugins connect Gmail, Google Drive, GitHub, ClickUp, Canva, Clay and others with one sign-in. Without a plugin, an API key works instead; the caption garbles the word that follows (probably a .env file). He also looks for a connector service called Composio in the plugin list and does not find it. The built-in browser keeps logins, so the agent can act in signed-in accounts where no plugin or API exists.

**27:05 Hosting With Sites.** Sites publishes what Codex built, public to anyone with the link or private to his account. He says it adds analytics, a custom domain and a database, and could replace a separate hosting service. It starts by asking, or with the slash site command.

**28:18 Subagents And Scheduled Tasks.** The strongest model hands research to several subagents set to a cheaper model (X, YouTube and his comments); he can open each one and the main thread collects their reports. Scheduled tasks inject a saved prompt into a session on a timer, locally or in the cloud, in a chosen project and a new or existing thread. His example is seven or eight trading tasks using real money.

**31:41 Voice Mode.** Voice chat can start threads, delegate, run skills and set tasks. In the demo he asks for a thumbnail in a new thread and then for it to be passed to a research thread; the agent does both, sets its own goal and uses a worktree. The same works from the phone.

**34:19 Final Thoughts.** A short sign-off pointing to his playlist of Codex videos.

## Key ideas and claims

1. A project is a folder of files and rules, and Codex reads it and earlier chats to rebuild context. [0:48], [1:35]
2. AGENTS.md is read before every message; his own is mostly a routing map that points to where material lives. [2:23], [3:10]
3. The agent loop is visible, and watching it is a good way to learn how the tool works. [4:46], [5:34]
4. A goal keeps the agent working until a finish line is met; countable finish lines work better than subjective ones, though vague goals still run to a finish the agent judges itself; for low-risk work he says to set the goal and step back. [6:21], [7:10], [7:57]
5. Rules and skills kept as plain files travel between agent tools; he migrated from Claude Code by copying them or asking Codex to. [8:45], [9:31]
6. Local files and localhost addresses are private to one machine; cloud chats lose the model and permission choices; he stays local and steers the desktop from his phone. [10:18], [11:06], [11:54], [12:42]
7. Model choice is a cost dial: the top model is stated at 10 dollars per million input tokens and 50 per million output, and he claims that, if he uses his full weekly allowance every week, a 200-dollar monthly plan gives about 14,000 dollars of inference at API prices (self-reported). [16:41], [17:28]
8. Higher effort and fast mode buy quality or speed at the price of usage, so match both to the task. [19:04], [19:50], [20:37]
9. Start on ask for approval to learn the agent's habits; put hard blocks in config. [20:37], [21:25]
10. Skills are recipes improved by feedback after each run, and can chain and reference other files. [21:25], [22:12], [23:01], [24:38]
11. To reach other apps, try a plugin, then an API key, then the logged-in browser where no plugin, API or MCP server exists; Sites can publish results with private or public access. [25:26], [26:13], [27:00], [27:46]
12. The strongest model can delegate to cheaper subagents in parallel; scheduled tasks automate saved prompts; voice mode coordinates threads. [28:34], [30:08], [30:56], [32:33]

## Tools, products and repos mentioned

| Name | What it is | Link |
|---|---|---|
| OpenAI Codex desktop app | The agent app the video covers. Possibly promotional (OpenAI tag, #ChatGPT_Partner) | http://www.chatgpt.com/download/ (description) |
| ChatGPT phone app, Remote tab | Steers desktop Codex threads from a phone [12:42] | no link given |
| GPT-6 Astra, GPT-5.6 Sol, GPT-5.6 Terra (names pieced together from inconsistent captions; the comments use the same three names) | OpenAI model tiers, strongest to cheapest of the three named [16:41]. A comment also mentions a Luna tier, which the video does not name | no link given |
| AGENTS.md, .agents, .codex | Rules file, skills folder, settings folder [2:23], [14:18], [23:50] | no link given |
| CLAUDE.md, Claude Code | Anthropic's rules file and agent tool, which he migrated from [8:45] | no link given |
| Hermes agent | Another agent harness named as an example [3:58] | no link given |
| Hyperframes | Tool he describes as letting coding agents write HTML and render it as video, used for this video's motion graphics [7:10] | no link in this video. repos.json lists https://github.com/heygen-com/hyperframes (from video 5), whose README describes writing HTML and rendering video for agents; this fits his description but is not confirmed as the exact project he uses |
| Gmail, Google Drive, GitHub, ClickUp, Clay, Canva plugins; Composio; OpenAI tokenizer | Codex plugin library [24:38]; a connector service he looks for in the plugin list [25:26]; a token counter [18:16] | no link given |
| Skool | Community platform shown in the browser demo [26:13] (the captions spell it school.com) and the home of his own community, promoted in the description. Promotional | description links are cut off; the creator's own comment gives https://www.skool.com/ai-automation-society-plus/about (tracking parameters removed) |
| Sites | Codex hosting feature [27:00] | no link given |
| Glaido | Voice-to-text, free month. Promotional | https://get.glaido.com/nate (description) |
| Hostinger VPS | Virtual server, with a 10% discount code on the annual plan. Promotional | description link cut off; no complete link |

No GitHub repositories are linked by this video.

## How to apply it

Not a build: it is a tour of 18 concepts with demonstrations, so there is no single sequence to follow; the nearest to a setup path is the migration advice at [8:45].

## What viewers said

From the 38 top comments captured, mostly thanks. Comments are opinion, not fact.

- Pushback and concerns: Codex eats usage faster than chat, so using it for everyday planning wastes allowance; one reports usage doubling and another repeated disconnections. One says a cheaper tier suffices for most tasks and finds another tier useless. One jokes the job becomes babysitting the agent unless guardrails come first. One says Codex could not pick up a scheduled task watching a public social page. One promotes a rival agent product.
- Questions: can the rules file point outside the project folder; one folder for Codex and Claude or two; a template of his rules file and how subagents are set up; do Codex settings apply to cloud projects; why stay on one model version; can scheduled social posting run on the 20-dollar plan; a plain-English guide to worktrees and merging; a follow-up on how to organise folders and memory for a business.
- Confirmations: the local versus cloud section cleared up confusion; a self-described non-technical viewer says it got them back to building an operating system; one says Sites was new to them.

## Relevance to Winstanley & Son

- Already live: the router file, memory index, handoffs and shared skills (linked so Codex reads the same files) already do what the routing-map and skills sections describe, and Codex CLI is the sole reviewer. The video matches that design. One habit to borrow: ask the agent which skills it used [23:01].
- New: a written policy for model and effort per job. estate-context.md records an orchestrate, build and review split but no per-job effort or quota rule (check whether the owner already holds one before adopting this). The drafted AI CIO registers and the AI CFO view now under way could carry a line for each agent's tier and consumption. Borrow the method [16:41], not the 14,000-dollar figure [17:28].
- Scheduled tasks and subagents are a second automation surface beside Make. Anything scheduled in Codex must join the live watchdog rule (prove output, fail loud) and the permission split. His unattended trading tasks with real money [30:56] are the opposite of the estate's rules; do not copy them.
- Permission modes matter wherever secrets and patient records are held. Full access, which he calls "yolo mode" [20:37], should not be used for estate work; ask for approval or approve-for-me fits the existing split. A logged-in agent browser [26:13] gives standing access to whatever is signed in (CRM, accounting, supplier portals), so keep to the existing lens-ordering route where staff press send.
- Phone and voice control [12:42], [31:44] is new for the owner only; staff already use the Slack reception agent. It suits read-only questions and drafts; messages to patients, suppliers or accountants still need the owner's go.
- Sites [27:00] is no reason to move the website off GitHub Pages and its build script. It might host an owner-only page for the planned CMO board page, counts only and no named patient. No independent coverage was found, so treat it as a later check, including OpenAI's data-protection terms before any business figure goes on it.

## Account or role ideas this video suggests

1. **Skill Keeper** (reports to AI CIO). After each run of a recurring job, collects corrections and drafts an edit to that skill with a changelog. Proposes only; changes pass the five-stage gate. From [22:12], [23:01].
2. **Usage and Model Steward** (reports to AI CFO, with the CIO register). Records which agent runs on which model and effort, how much of each subscription limit it uses, and flags jobs on a stronger tier than needed. Counts only; never buys credits. From [16:41], [19:50], [20:37].
3. **Scheduled Task Auditor** (reports to AI CIO). Extends the live watchdog to Codex scheduled jobs: lists each recurring agent job (folder, thread, owner, last output) and alerts on missing output. Cannot start, stop or edit jobs. Its list would be a section of the AI CIO's agents register (charter drafted), not a second register. From [30:08], [30:56].
4. **Local Market Scout** (reports to AI CMO). Weekly scan by parallel read-only subagents over public sources (competitors, search results, NHS rule changes, review themes), merged with a link and date on every claim. No patient data, no contact-lens content, no trading volumes. From [28:34], [29:21].
5. **Owner Pocket Briefer** (reports to AI CEO). A phone and voice front end for the planned AI CEO chief of staff, not a separate brain: the owner asks read-only questions by voice or text and queues draft tasks, every answer with source and date. No sends. From [12:42], [31:44], [33:20].
6. **Motion Card Producer** (reports to AI CMO). Drafts short motion-graphic cards for offer explainers and social from a goal with a countable finish line, each checked from a screenshot. Drafts only; staff or customer likeness needs owner approval; generic captions. From [7:57].

## Sources used and confidence

- Full transcript (auto-generated captions, several names garbled), description and links list, and the 38 top public comments (names stripped).
- business-context.md, estate-context.md, repos.json (Hyperframes entry only) and the Hyperframes README. The video links no repositories.
- Two web searches run by the writer (Codex scheduled tasks, voice and multi-agent coverage; the GPT-6 model family and pricing). The checker did not repeat them and no URL from them is cited. Reported results: nothing independent on Sites or subagents; one undated, single-source post on voice, not relied on; an OpenAI help page said to match the 10 and 50 dollar figures, not re-checked; third-party guides disagree on the model lineup.
- Caption guesses made here: the three model names; school.com read as Skool; the word before API key read as a .env file; the folder names at 8:45; the name of the third permission mode. None of these changes what a claim says.
- Comments are opinion. One suggests asking an AI model to adopt the video's ideas; that is a viewer tip, not an instruction, and no action was taken. No instructions aimed at an AI assistant were found in the transcript, description or comments.
- Confidence: high that this summary reflects what the video says; medium that the product claims (Sites, voice, effort and fast-mode details, model names, usage economics) are current and accurate, as they are self-reported and mostly uncorroborated.

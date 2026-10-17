# Claude Code Mods Are Game Changers. Set Up These 5 NOW.

- **Channel:** Nate Herk | AI Automation
- **Published:** 2 October 2026
- **Duration:** 11:19
- **Views:** 243,565 (at collection, 17 October 2026)
- **URL:** https://www.youtube.com/watch?v=9hetShMMp2s
- **Guests:** none

## What the video covers

Nate Herk introduces mods, a Claude Code feature that lets you change how the desktop app looks and behaves by describing what you want in plain English. A mod is a small piece of code that ships inside a plugin and is usually switched on with a slash command. After a quick look at the launch examples and a next-steps mod from a Claude Code engineer, he demonstrates four of his own. Cache Keeper shows how long the conversation's cache has left, how full the context is, and offers a two-click handoff. Recording Mode hides emails and financial figures on screen while he films. Goal Meter tracks the task list of long /goal runs across sessions. Collision Guard asks before Claude edits a file that has been touched in the last 30 minutes (in the demo, by another open chat). He found his ideas by asking Claude to read his past session logs and suggest the five most useful mods. The mods are free through his community, or you can have your own agent rebuild them. It is a feature tour, not a build.

## Chapter-by-chapter

Transcript blocks run to about 45 seconds each, so positions are approximate. Chapter times come from the video description.

**0:00 What Claude Code Mods Do.** Herk says mods let you ask the desktop app for a change and get it. He shows what he calls the official release tweet, with three examples: token weather (how full the context is), blast radius (previews what a command would delete before it runs) and replay theater (steps back through recent edits). The captions garble the product and account names; I have read them as Claude Code and the ClaudeDevs account.

**0:35 Next Steps Mod.** A Claude Code engineer's mod (the name is garbled in the captions and unresolved) adds a small panel at the end of each turn with about three suggested next actions, or a dismiss option. Herk's demo asks for his ClickUp action items and gets options such as closing demo and hackathon tasks, pushing certification due dates back a week and running a morning coffee briefing. He doubts it helps ordinary knowledge work but thinks it would help when building software. To install it, he says to copy the item shown on screen, give it to Claude and ask it to set the mod up, which he says takes about 30 seconds [1:35]. The captions do not say exactly what is copied.

**1:55 Building Mods With Natural Language.** Mods ship inside plugins, are installed with /plugin in the command line or desktop app, and can be created by asking Claude. His first step was to have Claude read many past session logs, spot what he repeats, and propose the top five mods. He did not take every suggestion. He also built a pet mod he calls pretty useless, and is unsure the viral visual mods on X would help him.

**2:53 Cache Keeper.** Herk explains that everything in a chat is cached, so each new message is not re-read at full price. By his account the cache lasts 60 minutes, after which the whole conversation is paid for again; each new message resets the countdown (it ticks from 57 back to 60 in his demo). The mod shows the countdown, the cost of an expiry, context size (109,000 tokens in the demo), the five-hour and weekly limits, and what the session would have cost at API prices. A button runs his session-handoff skill; a second click clears the chat and pastes the handoff note in. He admits this saves little time over doing the steps by hand, and thinks it could become one click. Five minutes before the cache goes cold it sends a notification offering a reprompt, compact or handoff. A promotion for his free first-client guide interrupts at about 4:46.

**5:30 Recording Mode.** Herk films videos and does not want emails, internal details or financial figures visible. With the mode on, Claude answers with placeholders instead of real addresses, and pasted text is masked on screen. In his demo he pasted a page with a $29 price and asked for $39. The real numbers reached Claude and the file changed, but the screen showed masked values. A slash command turns the mode on and off. The recording label on screen only shows the mode is on; Claude is not recording the screen.

**7:23 Goal Meter.** He runs many /goal prompts and loses track of progress. The mod shows the goal, a planning phase, minutes elapsed and, once Claude writes a task list, the tasks with a percentage complete. His first test finished almost at once because the work already existed. The second made four tasks, from finding a comment-fetching tool to reporting the main theme in viewer comments. A combined view lists goals from his other chats, which he finds useful with something like a dozen sessions running goals, as he says he often does.

**9:11 Collision Guard.** Before every edit, write or notebook edit, the mod checks whether the file was touched in the last 30 minutes. In the demo one chat changed a price; a second chat, asked to add a badge to the same page, was paused with a note that another open chat had just edited it. The options were proceed, move to a worktree, cancel, or type something else. Herk says this differs from a hook because it asks rather than blocks; the video does not explain why a hook before a tool call could not also ask. A skill or instruction file could do similar work, he adds, but a mod was quicker.

**10:35 Get the Free Mods.** Join his free community, open the classroom, find the YouTube resources and download the zip file or repository. Or give the transcript to your own agent and describe the behaviour you want. The captions are clear here.

## Key ideas and claims

1. [0:00] Mods let users change Claude Code's desktop interface and features by asking in plain English. Launch examples were token weather, blast radius and replay theater.
2. [1:35] Mods are plugins installed with /plugin. Herk says setup takes about 30 seconds if you give Claude the copied item shown on screen and ask it to set the mod up.
3. [1:55] Herk's first step was to ask Claude to read many past session logs, find what he repeats and propose the five best mods for his workflow. He used the answer as a prompt for ideas and did not adopt every suggestion.
4. [3:10] Herk says the cache lasts 60 minutes, reset by each new message, and that a lapse means paying again for the whole conversation. Anthropic's Claude Code documentation (read on 17 October 2026) says the main conversation gets a one-hour lifetime on a Claude subscription within plan usage, and five minutes with an API key, usage credits or a cloud provider. His figure therefore fits a subscription, not every setup.
5. [3:10, 3:57] Cache Keeper puts the cache countdown, the cost of a lapse, context size, usage limits and API-equivalent cost in the app window so he can read them at a glance.
6. [3:57] Handoff can be cut to two clicks: run the handoff skill, then clear and continue. This resets the context and avoids what he calls context rot. He says it saves little time compared with doing the steps by hand.
7. [4:46] Five minutes before the cache goes cold, a notification offers a reprompt, compact or handoff.
8. [6:19] Recording Mode masks sensitive text on screen while Claude still receives the real values, so it hides things from people watching a recording, not from the model.
9. [7:52, 8:40] Goal Meter shows the goal, elapsed time and Claude's own task list with a percentage complete, and lists goals running in other chats.
10. [8:40, 9:27] Collision Guard checks before every edit, write or notebook edit whether the file was touched in the last 30 minutes, and asks the person to choose. It does not decide for them.
11. [10:13] A skill or instruction file could do a similar job, but a mod was quick to build.

## Tools, products and repos mentioned

| Name | What it is | Link |
|---|---|---|
| Claude Code mods | Anthropic feature, announced 1 October 2026 (see Sources): code inside plugins that changes the interface and behaviour; runs in the command-line version and the desktop app; Anthropic's page says mods are not sandboxed | no link given |
| /plugin | Command that installs plugins and the mods inside them | no link given |
| Token weather, blast radius, replay theater | Example mods shown in the release tweet, per Herk | no link given |
| Next Steps | Mod by a Claude Code engineer (name garbled in the captions) suggesting about three next actions each turn | no link given |
| Cache Keeper, Recording Mode, Goal Meter, Collision Guard | Herk's four mods, shared through his free community | no link given (description link cut short) |
| Command centre (as heard in the captions) | Another of Herk's mods, seen only as a notification at about 2:22 and not explained | no link given |
| Session-handoff skill | Herk's own skill that writes a note for a fresh chat | no link given |
| /goal | Claude Code command for long-running goals | no link given |
| ClickUp | Task manager used in the next-steps demo | no link given |
| AI Automation Society (Skool) | Herk's free community, name inferred from the cut-off description link (the captions say school); self-promotion | no link given (description link cut short) |
| Glaido | Voice-to-text tool with a free month, promoted in the description under his tools list. Whether it is sponsored or an affiliate deal is not stated | https://get.glaido.com/nate |
| Hostinger VPS | Hosting, with a 10% annual-plan discount code in the description. Whether it is sponsored or an affiliate deal is not stated | no link given (description link cut short) |
| First-client guide | Free guide advertised mid-video | no link given in the description |

No GitHub repositories are linked. The mods sit in a zip file or repository inside his community classroom, which the video neither names nor links.

## How to apply it

Not a build. The setup shown is to give Claude the copied item shown on screen (or install through /plugin), ask it to set the mod up, then ask how to turn it on and off [1:35, 7:06]. His four mods come as a zip file or repository in the classroom of his free community [10:13].

## What viewers said

Comments are opinion, not fact. Forty were collected; many are short thanks, and three ask for dubbed audio.

- **Pushback.** One viewer notes that a handoff or compact after the cache has lapsed costs the full conversation, the very cost the mod aims to avoid. Others say similar apps exist, that harness-specific features do not appeal if you switch tools, and that one-click handoff is just compacting (Herk presents it as a note plus a fresh chat).
- **A careful installer.** One viewer had Claude go through all four mods before installing and reports that the only outbound traffic was periodic keep-warm requests. The same viewer changed the handoff to save worthwhile notes to memory first, and replaced a compact-first option with handing off to a fresh chat. A third change, about chats that were open before the mod was loaded, is cut off in the data. The viewer describes a cold-send guard and keep-warm requests, neither of which appears in the video, so the downloadable mods may go beyond the demo. Another viewer suggests a keep-warm timer that starts once a chat has been idle for 45 minutes.
- **Questions.** Does it work in the terminal-only version, the VS Code extension or beside Obsidian? One VS Code user who set the mods up from the transcript could not use them. Anthropic's announcement names only the command-line version and the desktop app (see Sources). Others ask about mods for other vendors' models, combining /goal with handoff so sub-agents report to the new chat, a theme switcher, and watching sub-agents live.
- **Confirmations.** Handoff is called the most useful idea against context rot. Cache Keeper is praised for avoiding surprise costs across long sessions. One viewer wants the pet mod released. One viewer says mask is a better word than blur [6:28].

## Relevance to Winstanley & Son

- **Handoff already exists.** The `session-handoff` skill is live, so do not build another. Cache Keeper adds a visible countdown and a one-click button on top. The new point is timing: hand off before the cache lapses, not after. The lifetime depends on the plan (one hour on a subscription within plan usage, five minutes on an API key), and Claude Code's own `/usage` screen already reports whether the cache is warm (Anthropic's documentation, version 2.1.251 or later), so confirm what is actually missing before installing anything.
- **Collision Guard automates a manual rule.** The estate says one session owns the website at a time. A prompt at the moment of an edit would back that rule for the build script and estate copies. The demo shows only two chats in one app, and the video does not say whether it sees edits from Codex, other tools or other machines, so it cannot replace the one-owner rule.
- **Recording Mode suits demos.** It would help Crewley.ai demos and the unlisted videos embedded on the site by masking names and figures on screen. Real values still reach the model [6:19], so it does not relax the rule that patient data is never pasted into chat. Record with pseudonymised fixtures.
- **Goal Meter helps the owner follow long builds.** It shows a build as a task list with elapsed time. It reports Claude's own list, not proof, so the evidence rule (check cards, rows and messages) still applies. The video shows chats in the app only, so scheduled agents still need the watchdog that checks they produced output.
- **Mods are code that runs on the machine.** Anthropic's announcement says they are not sandboxed and have the same machine access as Claude Code, which matters on a Mac holding protected token files. Installing one belongs inside the five-stage change gate: read the code, have Codex review it, trial it in a scratch project. The viewer who checked every line is the standard to copy. That viewer also reports keep-warm requests in the downloaded code, which the video never mentions; check what they do and what they cost.
- **Session-log mining is not listed as live.** It would support `ai-system-audit`, but logs can hold patient data and keys, so it must run locally and output only sanitised counts.

## Account or role ideas this video suggests

1. **Session Steward** (reports to the AI CIO) [3:10, 3:57]. Mission: keep long Claude sessions cheap and lossless, building on the live `session-handoff` skill. Inputs: cache age, context size, limits. Outputs: a warning and a drafted handoff note. Guardrails: never clears a chat without the owner's click; notes hold no patient data or token values.
2. **Edit Collision Warden** (AI CIO) [8:40, 9:27]. Mission: stop two sessions overwriting one file. Inputs: edit events and a 30-minute touch log. Outputs: a question (proceed, separate worktree, cancel) and a change-register line. Guardrails: asks, never overrides; the one-owner website rule stands.
3. **Demo Redactor** (owner, used by the AI CMO) [5:32, 6:19]. Mission: allow screen recordings without exposing patient or financial detail. Inputs: an on/off switch and patterns for names, phones and amounts. Outputs: masked display. Guardrails: display only; fixtures not live data; owner reviews a recording before posting.
4. **Build Progress Board** (owner, fed by the AI CIO) [7:52, 8:40]. Mission: one view of every running goal. Inputs: task lists. Outputs: progress and a stalled flag. Guardrails: percent complete is never proof; completion needs an artefact check.
5. **Workflow Miner** (AI CIO) [1:55]. Mission: find repeated requests in local session history and propose the top five skills. Outputs: a ranked shortlist with counts. Guardrails: runs locally; sanitise before output; owner chooses.
6. **Next Step Suggester** (owner; low priority) [0:46]. Offers three next actions after each turn. Herk was lukewarm, so trial only.

## Sources used and confidence

Sources: the transcript (auto captions, names garbled), the description (links cut short, empty links list), 40 public comments, `business-context.md`, `estate-context.md`, and the writer's two web searches (coverage of the announcement and third-party guides; those pages were not opened in full). At the check on 17 October 2026 I also read two Anthropic pages through a summarising fetch tool: the announcement, https://claude.com/blog/claude-code-mods (dated 1 October 2026; command-line version and desktop app; not sandboxed; no minimum version stated, whereas one third-party summary names v2.1.287), and the Claude Code prompt-caching documentation, https://code.claude.com/docs/en/prompt-caching (cache lifetimes by plan). No repositories were linked.

Confidence: **high** for what Herk showed, as the transcript is short and clear. **Medium** for platform facts, which rest on summaries of two Anthropic pages and on search results. **Low** for benefits, since he gives no measurements and says the handoff button saves little time.

# AI Agents Just Became Multiplayer. Here's How to Build Them.

- Channel: Nate Herk | AI Automation
- Published: 15 October 2026 | Duration: 22:24 | Views: 75,691 (as captured on 17 October 2026)
- URL: https://www.youtube.com/watch?v=KZiF2J83zaY
- Guests: none
- Sponsored: yes. The description says Kylon sponsored the video, and Nate says Kylon approached him [2:24].
- Timestamp note: each [m:ss] marks the start of a caption block, so it is accurate to within about 45 seconds.

## What the video covers

Nate argues that most people use AI in single-player mode: one person, one personal AI operating system, and skills and connected accounts that only help that person. His alternative is multiplayer AI, where a small team and its agents share a Slack-style workspace split into rooms, each room holding its own chat, apps, automations and files.

The video is a sponsored demonstration of Kylon, a product that does this. Nate shows his live rooms, a fresh account being set up, how a person's own Claude Code and Codex subscriptions can be plugged in as agents, and how credits are charged and tracked. He closes with a rollout plan: do not rebuild your tools or move everyone at once, start with one small work stream, find quick wins, then add rooms. He admits nothing shown was impossible before; the product removes plumbing rather than adding a capability. The most-liked comments treat it as a paid copy of free alternatives.

## Chapter-by-chapter

**0:00 Humans and Agents in One Workspace.** Nate opens a Slack-like screen with channels on the left and chat on the right. In a room called AIS Media, three people talk to one shared agent at once, alongside agents backed by Nate's and one teammate's Claude Code and Codex subscriptions. One agent built a dashboard and another restyled it, and the two messaged each other without Nate prompting [0:47]. Each room has its own apps, automations and files.

**1:17 Single Player vs Multiplayer AI.** Single player means a personal AI operating system wired to Slack, ClickUp, Gmail and Notion, which Nate describes as "20 arms and 30 desktops" [1:36]. Teams share results through tools such as Google Drive, but skills, memory and connected accounts stay with each individual, so work is sometimes duplicated. Multiplayer means everyone builds agents that anyone, including other agents, can talk to.

**3:00 Why I Tried Kylon.** He discloses that Kylon approached him to make the video and says he was hesitant, mainly about price, since a Claude Code subscription already goes a long way. He says the Kylon team showed him how they handle many of his objections, but he does not say which answers won him over. He lists the pain of individual setups: someone must keep Drive current and sync automations running.

**4:01 Moving a Team to AI Native.** He introduces his agent to teammates and describes a council room of several humans and agents. Citing podcasts he has watched, he says moving a large team all at once works badly, while one person or business unit at a time works better [4:48]. His pilot is a new media initiative whose processes, automations and tracker sheets are built in Kylon first. He reports it going well, with no figures.

**5:29 AIS Instagram Room Example.** In this room it is Nate, his Claude Code and his Codex. Because they run on his subscriptions they already had his environment variables and skills [5:36]. They built carousels and a board of post status, analytics and pipeline [5:36, 6:22]. Collaborators can edit apps together, and the team can choose who gives final approval before one goes live [6:22]. An automation runs every six hours to research, create, publish and analyse [7:10]. A request can open its own thread; one carousel was drafted, approved and published [8:00].

**9:28 Fresh Workspace Setup.** He names a new team and skips inviting anyone; billing is per workspace, not per member [9:34]. A head agent asks him to confirm his website, then interviews him. His tip: ask your existing AI OS to write a markdown brief about you and hand it over [10:21]. Gmail, Google Calendar, GitHub and Notion are built-in connections, and he demonstrates Gmail with a sign-in prompt [11:08, 11:55]; other services need a pasted API key, after which the agent reads their documentation [11:55]. The demo workspace name is garbled in the captions.

**12:55 Bring Your Own Claude Code and Codex.** A new agent gets a name, specialty and run mode. Kylon-hosted agents use a mix of models (his guess is that the system routes to a suitable one), and you pick an intelligence level: fast (captions say a tenth of the cost, taken to mean of max), pro (half of max cost) or max, which the Kylon team told him uses Opus (captions give version 5.5, unconfirmed) [12:55, 13:30]. Codex can run on Kylon's cloud around the clock; the Claude Code and Codex options run on your computer and go quiet when it is off, with a VPS or always-on Mac mini as workarounds [14:17]. Connecting means pasting a generated prompt into Claude Code [15:04]. These agents use the subscription, not Kylon credits, and billing shows usage by person and room [15:52].

**16:30 How to Get Started With Your Team.** Do not restart; bring existing skills across. Teammates can message each other's Claude Code, useful when the person is away [16:39]. Keep ClickUp and Drive and connect them. One of his first builds was a weekly commitments tracker plus an end-of-day agent check-in, because tasks get done but not ticked; as an example he says his AI OS can think a colleague has finished one of eight tasks when it is really four [17:28]. He plans a pipeline for a new interview show in which an untouched item pings its owner after about a day [18:16]. Start with one channel and quick wins, and tell the agent your tools, pain points and roles [19:04]. Humans and agents get profiles; sharing a subscription is optional, which he says is good for privacy [19:52].

**20:57 Final Thoughts.** He concedes everything could have been built before; his ClickUp-based attempts needed custom apps, polling, deployment and staff training [20:39]. He likens Kylon to Grok Bot with teammates invited and plans to keep building with it [21:27].

## Key ideas and claims

1. Personal AI operating systems keep skills, memory and accounts with one person, so teams sometimes duplicate work [2:24].
2. Multiplayer means humans and agents, including each person's own subscription-backed agents, working in shared rooms [0:00].
3. A room is the unit of organisation, with its own apps, automations and files [7:10].
4. Agents can message each other without a human in the loop; shown once, not measured [0:47].
5. Roll out one person or business unit at a time. This rests on podcasts, with no data given [4:48].
6. Onboard an agent with a markdown brief exported from your existing AI OS [10:21]; connect tools by sign-in or API key [11:55].
7. Stated billing model (the video gives no prices): per workspace, monthly credits used up by messages, and bring-your-own-subscription agents use none; usage is visible by person, room and agent [9:34, 15:52].
8. Local-subscription agents are unreachable when the host computer is off [14:17].
9. An end-of-day agent check-in is meant to correct status drift in task lists; one illustrative example, no results shown [17:28].
10. Pipelines need an owner pinged when an item stalls; planned, not yet built [18:16].
11. Nate's own caveat: no new capability, just less plumbing [20:39].

## Tools, products and repos mentioned

| Name | What it is | Link |
|---|---|---|
| Kylon (sponsored) | Workspace with Slack-style rooms where humans and agents share chat, apps, automations, connectors and credits | Sponsor page from the description: https://kylon.io/lp/nate-herk (tracking parameters removed). Home page https://kylon.io/ was found by web search, not given in the video |
| Claude Code, Codex | Anthropic's and OpenAI's coding agents, run from personal subscriptions; Codex can also run on Kylon's cloud | no link given |
| Grok Bot (captions: Grockbot) | Personal agent Nate uses and compares Kylon to | no link given |
| Devin (captions: Devon, probably Devin), Gemini, Hermes | The agent captioned as Devon is offered as a subscription option now, and Gemini, Hermes and Grok Bot (captioned as Grock Build) are described as coming; both readings of the captions are unconfirmed | no link given |
| Gmail, Google Calendar, GitHub, Notion | Kylon's built-in connections | no link given |
| ClickUp, Google Drive | His team's task and file systems, kept and connected | no link given |
| Glaido | Voice-to-text app promoted in the description; sponsorship not stated | https://get.glaido.com/nate |
| Hostinger VPS | Promoted in the description with a discount code; sponsorship not stated | no link given (truncated in description) |
| Skool community (his own) | Free-resources community promoted in the description | https://www.skool.com/ai-automation-society/about (from the creator's pinned comment, tracking parameters removed; the description copy is truncated) |
| Buzz (from comments) | Free, open source team chat from Block where Claude Code and Codex can join as agents; Apache-2.0 licence and early-stage status per the repository page, checked 17 October 2026 | https://github.com/block/buzz (found by web search, not given in the video) |
| Paperclip; Claude team plan (from comments) | Alternatives named by viewers; not checked | no link given |

## How to apply it

This is a setup walkthrough for Kylon. The steps below are put in a practical order; the timestamps show where each comes from in the video, which covers rollout advice last:

1. Pick one work stream and a small group, not the whole team [19:04].
2. Create the workspace and name the team; inviting members can wait, and billing is per workspace [9:34].
3. Ask your existing AI OS for a markdown brief about you and your business; give it to the head agent [10:21].
4. Connect tools by sign-in or API key; keep your existing task and file tools [11:55, 16:39].
5. Add agents, hosted or on your own subscription via the pasted prompt; note that agents on your own computer go quiet when it is off [12:55 to 15:04].
6. Build one thing that fixes a real pain, such as a daily check-in [17:28].
7. Watch credits, then add the next room [15:52, 19:04].

## What viewers said

The top 39 viewer comments were read (plus the creator's pinned comment, which only repeats links); most are short. They are opinion, not fact.

**Pushback.** Several resent it as an advert. The commonest reply, in at least four comments, is that a free tool called Buzz already does this; others name Paperclip, Claude's own team plan or Claude Tag. Some find the price too high, one citing a $50 plan with 500 credits and a small free allowance that runs out quickly. The $50 and 500 credits figure matches the Core plan on Kylon's own pricing page (checked 17 October 2026); the free-credit figure was not confirmed, as that page offers a short card-required trial instead. Others would build it in-house. One says Anthropic rules out multiplayer set-ups like this and points to its team plan instead (unverified). One asks whether the vendor can see their content.

**Questions.** How do Claude and ChatGPT team plans compare? What can a teammate's message reach on someone's local agent, such as the host's stored variables and connected accounts, and can that be limited channel by channel? Cloud versus local pros and cons? The video does not answer any of these.

**Confirmations.** Bringing Claude Code and Codex into one workspace was called very cool. A few had built similar setups, one running several models in a shared chat on a Mac. Three tips came from long comments with no likes (unverified anecdotes, possibly generic engagement): let only one agent edit a shared document while the others read; run fewer agents, write handoffs down and review at each stage; stop a Mac sleeping by using its built-in caffeinate command.

## Relevance to Winstanley & Son

- **Already live and close to this.** Staff already share one Slack room with an agent that creates and updates lab-order cards in GHL with button confirmation, and lens orders wait for staff to press OK to send. Nate's thread that drafts, asks approval and publishes has the same shape. Nothing here argues for replacing Slack, Make or GHL; Nate himself says to keep ClickUp and Drive [16:39, 17:28].
- **Do not copy bring-your-own-agent on staff machines.** Nate's local agents already had his environment variables and skills because they run under his own login [5:36]; what a colleague's message could reach through such an agent is an open viewer question. That would clash with the rule that secrets live only in protected files. A hosted workspace would also likely add a new data processor under UK GDPR, and no compliance approval exists for AI reading clinical records. Kylon's site claims GDPR compliance and lists SOC 2 and ISO 27001 audits as in progress (vendor claims, not checked). Its pricing page calls bring-your-own-agent a preview with terms not final, and a search snippet called the product private alpha while the pages fetched did not; treat availability as unproven.
- **New: spend and usage by room, person and agent** [15:52]. The estate notes list no per-automation or per-subscription cost view; they say automations count activity, not money. It fits the AI CFO read-only view and the AI CIO agent register, both still being built.
- **New: an end-of-day check-in for records that lag reality** [17:28]. The estate names attendance not marked and sale values not captured on order cards. It differs from the late-order alert, which fires on lateness, not stale status. Test channel first.
- **New: a written profile per agent and per staff role** [19:52]. Registers exist only in research notes. Staff profiles are personal data: keep them out of this public repo and ask consent.
- **Confirms existing discipline.** Starting with one work stream and quick wins [19:04] fits the five-stage change gate and the rule that nothing reaches staff before the isolated test channel has proved it.

## Account or role ideas this video suggests

- **Spend Tally Clerk** [15:52], reports to the AI CFO, copy to the AI CIO. Mission: one monthly line per automation and AI subscription. Inputs: Make and subscription usage pages, read-only. Output: a table with source and date per figure. Guardrails: no payment changes or top-ups, no patient data. Fold it into the AI CFO build if that build already covers Make usage, rather than starting a separate account.
- **End-of-Day Close-out Chaser** [17:28], reports to the owner via the AI CEO weekly facts pack. Mission: ask owners of open items to confirm status, attendance and sale value in Slack. Output: a tally of confirmed, unconfirmed and changed. Guardrails: staff only, no patient messages, test channel first.
- **Stalled-Work Chaser** [18:16], reports to the AI CEO. Mission: ping the named owner when a bespoke frame job or open owner decision sits untouched for a day. Check first that the late-order alert does not already cover bespoke jobs. Guardrails: nudges only, never moves a card.
- **Agent Profile Keeper** [19:52], reports to the AI CIO. Mission: one page per agent covering purpose, model, owner, schedule, last-output check and cost. Guardrails: no credential values, read-only. Take the last-output check from the existing watchdog rather than building a second one, and build it as part of the AI CIO register, not as a separate account.
- **Role Brief Interviewer** [10:21, 19:04], reports to the AI CIO, owner approves. Mission: interview each staff member for responsibilities, tools and pain points, then draft a short role brief. Guardrails: consent, no clinical or patient detail, stored outside the public repo.

## Sources used and confidence

Sources: full transcript (auto captions; Codex, Grok Bot, Devin, one account name at 5:36 and the demo workspace name are garbled); description and links list; the top 39 viewer comments plus the creator's pinned comment; web searches and page fetches on 17 October 2026 of kylon.io (home and pricing pages) and the Buzz repository on GitHub; estate-context.md and business-context.md. No repositories are linked from the video and none were read. No text addressed to an AI assistant was found in the transcript, description or comments.

Still unverified: the hosted-tier cost ratios and the Opus claim (relayed by Nate from the Kylon team); the free-credit figure from one comment; whether the product is in private alpha (one search snippet said so, the pages fetched did not); whether using a personal Claude Code or Codex subscription this way fits the providers' terms; what a teammate's message can reach on a local agent; Kylon's handling of user content; results of the media pilot and the six-hourly Instagram automation (no figures given); and the commenter anecdotes. Buzz's scheduled workflows exist on its repository page, but its approval steps are listed as still in progress and nothing was tested.

Confidence: **medium**. High on what the video says, since the transcript is complete and the walkthrough clear. Low on product claims: the video is sponsored, hosted-tier costs are relayed second-hand, the availability and free-credit details conflict across sources, and nothing was tested.

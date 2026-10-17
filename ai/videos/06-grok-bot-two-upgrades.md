# Grok Bot Just Got 2 Massive Upgrades. Do These Things Now.

- **Channel:** Nate Herk | AI Automation
- **Published:** 8 October 2026
- **Duration:** 9:11
- **Views:** 122,027 (at collection, 17 October 2026)
- **URL:** https://www.youtube.com/watch?v=MgvwZaDPCs4
- **Guests:** none

## What the video covers

Nate Herk walks through two changes to Grok Bot, a hosted agent product in which bots run on a cloud computer with a shared file system. The first is automatic model routing: the platform now chooses a back-end model for each task. Herk says it will run on Claude Opus 5.5 and assumes that is the default, with a faster Grok model expected to take simple requests once it is released. He likes the direction but wishes users could see and set the model. The second change is built-in X search, which replaces a paid X developer API. He moved his bots across; by his own account the old API spend was about five dollars a week.

He then draws one design lesson from routing: split large skills so cheap steps and reasoning-heavy steps can be handled separately. The final third is his favourite trick. Use a bot's terminal to install Claude Code or Codex, sign in with your own subscription, clone your repositories, and reach your projects from a phone through a machine that is always on. A free AI OS kit, which is his own product, is promoted in the middle. The video is partly commentary on platform news and partly a short setup walkthrough.

## Chapter-by-chapter

Transcript blocks run to about 45 seconds each, so positions below are approximate.

**0:00 Two Major Grok Bot Upgrades.** A short opening in which Herk names the two upgrades and promises a hack, set up in about five minutes, at the end.

**0:14 Automatic Model Routing.** Herk retells Elon Musk's announcement from the day before: the bot will pick the best back-end for a task, naming Claude 5.5 (the captions render it oddly), Midjourney for images, Suno for music, and unnamed other leading APIs. He lists the questions he and others had: whether the choice can be seen or controlled, and what it does to weekly usage. He says it will run on Opus 5.5, which he assumes is the default, though there is no visibility of the model or effort level. Musk's follow-up, as Herk relays it, says simple questions go to small fast models, hard ones to large models, and most requests to a fast Grok 4.8 once it is released. Herk would like a harness that works with any model and any subscription. He notes that some users want to opt out of Anthropic models.

**2:00 Native X Search.** Bots gain built-in ability to look up, read and watch X without the paid API, a change Herk says arrived later the same day. He had his X-monitoring bot switch his routines over, then message his other bots about it (names garbled in the captions). The old API spend was about five dollars a week, by his own account; two balance figures (roughly 104, then 89) are unclear, and it is not clear what they measured. A test with a second bot returned five posts, a reported cost of zero, and a free daily allowance with 995 reads left, resetting around 7 p.m. Central. The captions garble the allowance figure (a,000); 1,000 is inferred from 995 left after five posts. At about 3:58 he cautions that a bot does not always know how it works.

**4:08 Free AI OS Kit.** A promotion for a free template for an AI operating system, built on his framework, the Herk Loop, of context, connections, capabilities and cadence. He says it has six skills, helps you set up a central knowledge store (he calls it a brain), and interviews you about your priorities and business. Self-promotion, not related to Grok Bot.

**4:35 Rethinking Your Skills.** One skill doing seven jobs may suit a single capable agent today, but under routing it may balance cost and quality badly. His example is a video-creation skill covering ideas, research, comments, animation and packaging: perhaps four steps suit a fast cheap model and three need strong reasoning, design or taste. He guesses, and says so, that routing makes one choice per prompt, not a mid-task switch, because of cache expiry and handoff. A bot fanning prompts out to six others means six choices. He wants to see model and effort, and to pin a model to a skill, since skills behave differently across models.

**6:39 Running Claude Code Inside Grok Bot.** The hack. Herk says Grok Bot itself stays on its own subscription while the tools inside it can use your separate Claude or Codex plan, though the captions make this passage confusing. The bots share one computer and file system but each has its own screen, and a terminal means command-line tools can be installed. He shows a bot inside Claude Code in his repository, on Opus 5.5 and his team plan. The steps as he describes them: ask the bot to install the tool, sign in yourself when prompted and authorise, then clone your repositories so skills and instruction files come along. Because the machine stays on, Claude Code is reachable from a phone. He prefers API keys to desktop-app plugins so that changing host means migrating one file; the captions do not make clear which file.

**8:59 Final Thoughts.** Mostly a sign-off; the comparison starts at 8:41. Herk says two similar agent-computer products exist (names garbled) and he prefers Grok Bot, using it daily for small automations across many bots.

## Key ideas and claims

1. [0:14] Musk said Grok Bot will route each task to the best back-end, naming Claude 5.5, Midjourney, Suno and other APIs. This rests on Herk's retelling; secondary coverage matches, but no official xAI page was found.
2. [0:47] Herk says it will run on Opus 5.5 and assumes that is the default, but admits there is no visibility of model or effort. Musk's stated aim, as relayed, is small fast models for simple work and large models for complex work, with a fast Grok 4.8 handling most requests once it is released.
3. [1:34] Herk wishes Grok Bot were a harness he could steer using any model and any subscription, which he says foreshadows the hack at the end. Some users object to requests reaching Anthropic and ask for an opt-out.
4. [2:22] Built-in X search is described as free to the user and replaces the paid developer API. Herk had his X bot switch his routines and message his other bots.
5. [3:10] Herk's own figure for the old API spend is about five dollars a week. The zero cost and the free daily allowance (995 left; 1,000 inferred) are the second bot's self-report, and Herk himself says to treat that with caution [3:58].
6. [4:35] Split a mega skill into pieces according to the model each piece needs: cheap fast steps versus reasoning and taste steps.
7. [5:33] His guess is one model choice per prompt, with no mid-task switching. Fan-out across several bots multiplies the choices. This is speculation.
8. [6:20] Skills do not perform the same on every model, so he wants per-skill model pinning and visibility.
9. [6:20] Grok Bot stays on its own subscription; the CLI tools inside it use your separate Claude or Codex plan (the captions make this passage confusing). Bots keep separate screens but share a file system, and an always-on machine puts Claude Code on your phone [7:07].
10. [7:54] Setup order: bot installs, human completes sign-in, repositories are cloned, one file is migrated (probably a keys file; the captions are unclear). In his view API keys beat desktop-app plugins for portability.
11. [8:41] Herk prefers Grok Bot to two comparable products and uses it daily for quick automations.

## Tools, products and repos mentioned

No GitHub repositories are linked from this video, and none of the entries in repos.json comes from it. Nothing is labelled as sponsored; the description carries promotional links.

| Name | What it is | Link |
|---|---|---|
| Grok Bot | Hosted agent product; bots share a cloud computer and file system, each with its own screen and a terminal. Subscription routes named in the captions (Cursor, SpaceX, Super Grok) are unclear | no link given |
| Automatic model routing | New Grok Bot feature that picks a back-end model per task | no link given |
| Claude Opus 5.5, Midjourney, Suno | Anthropic model assumed to be the default back-end; image and music services named as routing targets | no link given |
| Grok 4.8 | xAI model, described as not yet released at filming | no link given |
| Native X search and the paid X developer API | The free built-in feature versus the metered interface it replaces | no link given |
| Claude Code, Codex CLI | Coding agents installed in the bot's terminal; the captions garble Codex as *codec* | no link given |
| Herk's AI OS template (Herk Loop framework) | Free kit behind an opt-in page; his own product, so promotional. The description also links his Skool community (links truncated) | Truncated in the description; the creator's comment gives https://app.aiautomationsociety.ai/optin/ai-os/ (tracking parameters removed) |
| Glaido | Voice-to-text tool, named from its link; free-month offer under My Tools in the description only, not mentioned in the video. Promotional, probably affiliate, not stated | https://get.glaido.com/nate |
| Hostinger VPS (discount code) | Hosting, in the description only, not mentioned in the video. Promotional, probably affiliate, not stated | truncated in the description, no complete link |
| Two rival agent-computer products | The captions give *Dots* and *Muse*; names uncertain | no link given |

## How to apply it

The final third is a short setup walkthrough. Herk's steps, as described:

1. Have an active Grok Bot subscription and a bot to work with, or create one named for the tool.
2. Ask the bot to open its terminal and install Claude Code (or Codex).
3. When it asks you to sign in, do that yourself and authorise.
4. Ask it to clone the repositories that hold your skills and instruction files.
5. Move one file across (probably your API keys, though the captions are unclear) instead of relying on desktop-app plugins.
6. Reach the bot from your phone and work on your projects.

This is not recommended for the practice as it stands. See the relevance section for why.

## What viewers said

Comments are opinion, not fact.

- **Pushback:** One reasons that the platform will never allow model choice, because everyone would pick the strongest. Others suspect motives such as collecting training data or draining a rival's capacity. One warns that extra usage can be used up within minutes and that support is unhelpful (the provider is not named). One fears the bot's own computer use burns two sets of tokens at once.
- **Noise:** The four most-liked comments, with near-identical like counts, all name an unrelated-sounding product called Claudixum, and one more in Bengali does the same. They read as coordinated promotion; the first four say nothing about the video and the Bengali one at most nods at it.
- **Questions:** One wants a full video on Claude Code subscriptions inside the bot. Another asks for a video on protecting personal information and credentials when handing them to agents. A third says the video should explain why this helps and supplies the reason themselves: the bot's computer means your own desktop need not be on.
- **Confirmations:** A few say running Claude Code in a bot's terminal, or the hack in general, has greatly increased what they get done. One says voice chat copes with long parallel tasks. One says Grok Bot feels smarter this week but burns allowance quickly, and that it hands routine work to Grok 4.7, whose allowance is hard to exhaust; that names 4.7, not the unreleased 4.8 Herk mentions, so there is no conflict. Others say they have already connected Codex or Claude Code to a bot, or plan to run both through one, and one keeps a separate bot per function.

## Relevance to Winstanley & Son

- **Already live and touched:** the practice already assigns models by job by hand (Fable orchestrates, Sonnet builds, Codex reviews), keeps short single-purpose skills, and has the ai-system-audit skill for checking shared skills for duplication and staleness. Herk's skill-splitting advice mostly confirms that. What is new is a deliberate step-by-step pass over each existing skill, marking steps as mechanical, judgement or customer-facing, and noting which model ran each job.
- **Opaque routing clashes with the change gate.** The estate proves changes in the isolated test channel with realistic phrasings. If a platform silently swaps the model, the same phrase could behave differently live and in test. Anything touching lab orders, patient messages or money should run on a named, recorded model.
- **Native X search has no home here.** The estate has no X workflow; marketing runs on Meta, Google, Business Profile posts and the GHL Social Planner. The native-first rule already says to use what the platform provides before building or paying for more. The only fresh angle is for the AI CFO, now being built: list per-call paid services and check for native alternatives.
- **Always-on Claude Code on a third-party host is new, and it cuts across the estate's own rules.** Putting a Claude login, the repository and a keys file on another company's machine conflicts with the secrets rule (values only in protected files) and the patient-data rule. Anthropic's legal-and-compliance page (read on 17 October 2026) says third-party developers may not offer Claude.ai login or route requests through subscription credentials for their users. It also says an end user may sign in to the unmodified Claude Code binary with their own plan, including on a platform that hosts it, and that a hosting platform needs Anthropic's Commercial Terms. Whether Grok Bot meets those conditions is unverified. This research pack began in a first-party cloud session, so a phone-reachable route plausibly exists without Grok Bot (not tested).
- **Fan-out between specialist bots multiplies where data can travel.** One bot briefing others suits change notices, but bots must exchange counts and non-identifying references only, never patient detail.
- **The AI OS kit likely adds little.** Its four labels (context, connections, capabilities, cadence) map onto the router file, system list, skills and scheduled jobs already in place. The kit itself was not inspected. The estate's real gap, a scorecard, is unlikely to come from a generic template.

## Account or role ideas this video suggests

1. **Skill-fit reviewer** [4:35], reports to the AI CIO. Mission: building on the existing ai-system-audit skill, read each shared skill and mark every step as mechanical, judgement or customer-facing, then propose splits. Inputs: skill files and run notes. Output: a one-page proposal. Guardrails: read-only; any change goes through the five-stage gate and the owner presses.
2. **Model-and-cost ledger keeper** [5:33, 6:20], reports to the AI CIO, with a monthly line to the AI CFO. Mission: record which model and effort ran each scheduled agent and what it cost, because hidden routing was Herk's main complaint. Inputs: run logs from Make and Slack. Guardrails: counts and costs only, no message content.
3. **Metered-spend watcher** [2:22, 3:10], reports to the AI CFO. Mission: each month list paid per-call services, compare them with native features, and draft a saving for the owner. Guardrails: read-only; the bot's own cost claims are checked against the invoice.
4. **Change broadcaster** [2:22], reports to the AI CIO. Mission: when a rule or capability changes, draft the note that each account's instructions need and log it in the change register. Guardrails: drafts only; the owner approves.
5. **Pocket console** [6:39], reports to the AI CIO, on hold. Slack already delivers the live alerts and finance status to a phone, so this would add only read-only access to repository files and skills from a phone. Hold until a first-party route and the terms and data checks are settled.

## Sources used and confidence

- Transcript (auto-generated captions), the description, the creator's comment (which repeats two promotional links) and 40 public comments, with commenter names removed.
- No repositories were read; none are linked from this video.
- Web checks, 17 October 2026. A MindStudio post dated 9 October 2026 (https://www.mindstudio.ai/blog/grok-bot-model-routing-upgrade/) reports the same routing and X search story, including a 1,000-reads-a-day allowance and X spending falling from about five dollars a week to zero. It cites no official xAI page, treats Claude Opus 5.5 as reported rather than confirmed, and may derive from this video. Anthropic's page https://code.claude.com/docs/en/legal-and-compliance was read directly; it covers subscription sign-in and hosted Claude Code (see the relevance section).

**Confidence: medium.** The storyline is clear and consistent with secondary coverage. Product and bot names, two balance figures, the allowance figure and the migrated file are unclear in the captions. The platform facts rest on Herk's retelling of Musk's statements and on a bot's self-report.

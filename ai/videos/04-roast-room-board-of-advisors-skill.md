# This ONE Claude Skill Helps You Think Clearer Than 99% of People

- **Channel:** Nate Herk | AI Automation
- **Published:** 12 October 2026 | **Duration:** 14:45 | **Views:** 67,831 (as collected on 17 October 2026)
- **URL:** https://www.youtube.com/watch?v=nRXHWckVxoM
- **Guests:** none

## What the video covers

Nate Herk (Nate from here on) demonstrates and gives away a Claude Code skill he calls the Roast Room: a panel of seven AI advisers that debate a business decision and return a scored verdict. Each adviser is a sub-agent styled on a well-known business figure (named on screen: Jeff Bezos, Paul Graham, Alex Hormozi, Gary Vee, Dan Martell, Gino Wickman and Warren Buffett) and owns one question, for example how reversible a bet is, whether people want the product, or what a move does to cash risk. The main Claude Code session acts as chair and runs three rounds: opening positions that include scores, chair-directed argument between advisers, then a final vote. Sessions are saved and the verdict exports as a PDF. An optional visual interface animates and replays debates; Nate says it is cosmetic.

He then opens the files to show how an adviser is built: a short agent file that points to a folder of markdown knowledge compiled from public material. The last quarter covers how to write a good question, how existing context improves the answer, and a closing argument for handing off the thinking while keeping the judgement. The skill is free through his Skool community.

## Chapter-by-chapter

**0:00 Meet the Roast Room.** Nate shows the visual interface mid-debate on a four-option decision about a June 2027 conference (the event name is garbled in the captions, so it is not given here). Seven advisers write opening positions, each judging options against one question they own. In round one the advisers score the options out of 10, and all seven back option B with an average of 7.1. The interface sits on top of a normal Claude Code session where he launched the skill with a detailed brief.

**2:19 The Advisers Debate.** The chair is the main session, and the advisers are sub-agents, not an agent team. Because all seven backed the same option, the chair in this run treats that as a warning and asks two advisers to make the strongest case for option C. Advisers then address each other directly, agreeing or pushing back, and the interface lets you read each exchange and each round. Round three is the vote; it points to B again, and the verdict at 3:55 backs B.

**3:37 The Final Verdict.** The output is a verdict with conditions: run B at a set annual price, cap one tier at a set number of seats, and commit to nothing until a stated number of members have paid a stated total by a stated date (that tier's name is garbled in the captions, so it is not given here). Nate usually submits a few questions and reads the verdicts later. He does not follow them blindly; the differing perspectives help him think even when he disagrees. The verdict downloads as a PDF with scores and what each round weighed.

**4:44 Get the Free Skill.** The skill is in the classroom of his free Skool community, under an AI skills section, linking to the full repository. A past-sessions view lists earlier PDFs and can replay any debate. The chair does not always convene all seven: a hiring-versus-selling question used only four advisers. A mid-roll plug for his free first-client guide follows. Sessions are stored as files in a project folder, so the interface is optional.

**6:42 How the Council Works.** Nate casts himself as the room, Claude Code as chair, and the advisers as separate sub-agents. The flow is opening positions, reading each other and being told whom to challenge, then a vote, with everything saved and a verdict produced. He switched back from agent teams to sub-agents because, in his experience, the two gave him much the same answers, while sub-agents were cheaper and kept each voice more distinct (no comparison is shown).

**7:45 Adviser Brains and Setup.** An adviser is a short agent file giving who they are, the question they own and how they decide, plus links to their brain folder. That folder holds a summary sheet of eight decision rules, named frameworks, principles, positions, stories, voice notes and a source list, all gathered by research agents from public posts, videos and writing. The Hormozi brain is quoted as about 124 sources and over 1.3 million words. To swap an adviser, you ask Claude to build another in the same pattern, and he says the advisers then score every option and weight it by relevance (the captions leave unclear exactly what is weighted). You install it by pointing your agent at the repo. Hormozi's surname is mis-spelt several ways in the captions; the description spells it correctly.

**10:52 Asking Better Questions.** If your personal context, meeting notes and connected tools are available to Claude Code (Nate calls this his AIOS, which we read as AI operating system; the full name is not spoken), it will pull what it needs and ask clarifying questions first. A good brief states the decision wanted, two or three options, real numbers, limits such as deadlines, hours and budget, what success looks like, and which way you currently lean and why. He asks for your current lean and reasons, noting that AI sometimes agrees with the user, and says the room is built so that advisers reason from their own principles and may reverse or confirm you rather than simply agree. You can also talk loosely and ask Claude to turn it into a proper brief.

**13:02 Outsourcing Thinking, Keeping Judgement.** Nate calls this a simple skill but a habit worth building: borrow subject expertise you lack while keeping your own understanding. His hypothetical example is a security agent that researches books, articles and videos and stores what it learns, with your questions then going to it. He suggests pairing it with a CTO agent and letting the two debate. The agent's recommendation still has to be processed and understood, not accepted blindly.

**14:31 Next Steps.** A sign-off only, repeating that the skill is free in his community. Nothing substantive.

## Key ideas and claims

1. Each adviser owns one question: right bet and reversibility (Bezos), demand and growth (Graham), cash risk and long-term value (Buffett), offer, pricing and sales (Hormozi). Nate presents these as narrow, specific remits. [0:46, 7:04]
2. A three-round structure: opening positions with scores, chair-directed cross-examination, then a vote and verdict. [1:34, 2:20, 6:17, 7:04]
3. In the demo, unanimity in round one is flagged by the chair as a warning, and two advisers are told to argue for a different option. Whether this is a fixed rule of the skill is not stated. [2:20]
4. The chair is the main session and the advisers are sub-agents. Nate says he switched back from agent teams because the two approaches gave him similar answers, while sub-agents were cheaper and kept each voice more distinct. This is his experience; no comparison is shown. [7:04]
5. An adviser is a thin agent file plus a knowledge folder (decision-rules sheet, frameworks, positions, stories, voice, sources). The thin file routes to the detail only when needed. [7:52, 9:27]
6. Knowledge folders are built by research agents from public material; the Hormozi folder is said to hold about 124 sources and over 1.3 million words. [7:52, 10:15]
7. The chair can convene a subset of advisers when the question needs only some. [4:42, 5:29]
8. The deliverable is a saved, replayable session and a PDF verdict with conditions and scores, not just a chat answer. [3:55, 4:42]
9. A good brief contains the decision, two or three options, real numbers, limits, a definition of success, and your current lean. [11:02, 11:50]
10. Nate asks you to state your lean and why, noting that AI sometimes agrees with the user, and says the room is set up so that advisers reasoning from their own principles may persuade you of the opposite or validate you, not just agree. [11:50]
11. The visual interface is optional; the skill still produces the report without it. [10:15]
12. Nate's aim is to "outsource your thinking but not the understanding" [12:37], using stored expert knowledge while still judging the answer yourself. [13:25]

## Tools, products and repos mentioned

| Name | What it is | Link |
|---|---|---|
| Roast Room skill | Nate's free Claude Code skill: seven sub-agent advisers, three-round debate, PDF verdict, optional visual interface | No link given (the description link is cut off; access is via his Skool classroom, AI skills section) |
| Claude Code | Anthropic's coding agent, used here as chair and host | No link given |
| Sub-agents and agent teams | Claude Code features for delegated or coordinated agents; Nate chose sub-agents | No link given |
| AI Automation Society (Skool) | Nate's community where the skill is hosted; the base group is free, with a paid upgrade mentioned at 5:29 | https://www.skool.com/ai-automation-society (the description link is truncated; this address was checked on 17 October 2026 and resolves to the group) |
| First Client SOP | Nate's own free guide, promoted mid-roll at 5:29 (own product) | https://app.aiautomationsociety.ai/optin/first-client-SOP/ (from his own comment, tracking parameters removed; description link truncated) |
| Glaido | Voice-to-text tool, free month offered; listed in the description only, not mentioned in the spoken video; promotional link, sponsorship status not stated | https://get.glaido.com/nate |
| Hostinger VPS | Hosting, with a 10% discount code on annual plans; listed in the description only, not mentioned in the spoken video; promotional, sponsorship status not stated | No complete link given (description link truncated) |
| AIOS (read as AI operating system; expansion not spoken) | Nate's term for his Claude Code setup holding context, stories, meeting transcripts and connections | No link given |

No GitHub repositories are linked, and none were read.

## How to apply it

The video is a demo with a short setup outline, not a build walkthrough. The steps it does state are:

1. Get the skill from the community classroom and ask your Claude Code agent to install it in a project. [4:42, 8:40]
2. Write a brief: decision, two or three options, real numbers, limits, success definition, current lean. [11:02 to 12:37]
3. Run the skill; answer any clarifying questions the chair asks first. [11:02]
4. Read the verdict and each round's reasoning, then decide yourself. [3:55, 13:25]
5. To add or swap an adviser, ask Claude to build one to the same pattern from public sources. [7:52, 8:40]

## What viewers said

- **Pushback:** several expect a run to use up a subscription's allowance quickly. One argues seven advisers on one model are one set of training echoing itself and that a real board needs different model providers. Others say AI is wrong too often to trust any verdict, that a board built on criteria suited to your own business beat one built on famous individuals, that it resembles an earlier council skill that used a lot of tokens, and that the models may already know most of this. Two object to the line-up of advisers.
- **Questions:** whether the usage fits a $20 plan; whether all advisers run the same Claude model; how Nate ensures agents actually read their brain files before voting; how to give an agent that much context; whether it works with Gemini or Codex; requests for a video on building the persona agents.
- **Confirmations:** several say they will install it or build their own. Two already run multi-provider boards, and one claims task routing cut their API spend by about 80%, which is unverified and reads partly promotional. One suggestion worth keeping: have each adviser state the one assumption in your plan that is most likely to be mistaken, so the panel tests the plan instead of flattering it.

Comments are opinion, not fact.

## Relevance to Winstanley & Son

- **What it touches that is already live:** the owner's pressure-testing today comes from separate shared skills (an interviewing one, a commercial-filter one, an agent stress-test one) and Codex review of build packages. As far as the estate notes show, none convenes several distinct viewpoints on one decision and keeps a scored, dated verdict, so that format looks new (the skill files themselves were not checked).
- **Fit with the AI leadership plans:** the AI CEO design already includes arguing the other side of big decisions and the AI CMO design has a scored decision log. This video supplies a mechanism for those steps: a structured brief, forced dissent, a saved verdict with conditions. Build it inside those plans, not as a competing account.
- **First test cases exist:** the 6-month-plus reactivation plan awaiting decisions, the Meta form trial, and the paused review requests. Try it first on a decision still open, with counts only; replaying a settled decision would be a dry run and must not reopen it.
- **Limit set by the estate's own gaps:** the brief wants real numbers, but the notes record no scorecard and no sale values on order cards. Until the CFO and CMO ledgers fill, a council would argue from reported figures, so sequence it after those.
- **Guardrails the video does not cover:** recall intervals are clinical and the optometrist decides, so no seat may rule on them. Patient data stays out (aggregates only). Public-claim rules apply (no volumes, no contact lenses, no prices in listings). The video also does not discuss whether compiling public figures' material into advisers is allowed under their terms or copyright, so check that before building named-person seats. A verdict is advice, not approval; the five-stage gate and the owner's press still apply. Decisions stand once made, so use it before deciding, not to reopen.
- **Echo risk:** all seats on one model share one training, and in the demo all seven backed the same option in round one and the verdict backed it too. The estate already uses Codex as an independent reviewer, so one seat on a different model is a design option; the video does not show how.

## Account or role ideas this video suggests

1. **Decision Council (Roast Room style).** Mission: pressure-test one named decision before money is spent. Inputs: a six-field brief and ledger figures. Outputs: scored verdict, dissent, conditions, review date. Guardrails: read-only, counts only, no clinical rulings. Source idea: chair plus single-question seats and three rounds [0:46, 2:20, 6:17, 7:04]. Reports to: the owner, fed by the AI CEO.
2. **Brief Builder.** Mission: turn the owner's dictated thoughts into a complete brief and ask the missing questions before any panel runs. Inputs: voice notes, weekly facts pack. Output: the brief. Guardrail: flags any unsourced figure. Source idea: clarifying questions and talk-then-shape [11:02, 12:37]. Reports to: AI CEO.
3. **Reference Brain Librarian.** Mission: keep short, dated, source-listed knowledge folders for weak spots (NHS eligibility rules, UK GDPR, advertising rules). Outputs: a rules sheet and source list per topic, plus a review date. Guardrails: public sources only; clinical points go to the optometrist. Source idea: the brain folder structure and the security-agent example [7:52, 13:25]. Reports to: AI CIO, which holds the compliance dates register.
4. **Offer and Spend Sparring Panel.** Mission: a small set of role lenses (cash, patient trust, capacity, offer clarity) that challenge campaign and offer proposals. Output: a verdict attached to the CMO's decision log. Guardrails: no patient-level data. Source idea: each seat owns one question and reasons from its own principles rather than simply agreeing [0:46, 11:50]. Reports to: AI CMO.
5. **Decision Archive keeper.** Mission: file each dated verdict and later record what actually happened. The video stores and replays sessions [4:42, 6:17] but does not describe checking outcomes; that is our extension. Reports to: AI CEO.

## Sources used and confidence

- **Used:** the full auto-generated transcript, the description (links truncated), the creator's own comment and 37 public comments with names removed (opinion, not fact), the estate and business context files, one web search and one page check. Neither found the Roast Room page or repo; they only confirmed the Skool group's address and that it has a free tier. No repos were linked or read.
- **Confidence: high** for what the video says (transcript read in full, mostly clean apart from garbled names). **Lower** for how the skill behaves in practice, since the repository sits behind the community sign-up and was not inspected, and Nate's cost and quality comparisons are his own, unmeasured claims. Still open: the conference name, the tier name in the verdict and what is weighted by relevance (all garbled or unclear in the captions); token cost per run; whether the advisers really disagree; and whether the Glaido and Hostinger links are sponsored.

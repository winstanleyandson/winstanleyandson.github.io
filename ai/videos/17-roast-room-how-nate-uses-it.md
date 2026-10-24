# /roast-room: How I Use Claude to Think Like the Top 1%

- **Channel:** Nate Herk | AI Automation
- **Published:** 22 October 2026 | **Duration:** 15:00 | **Views:** 29,752 (as collected on 24 October 2026)
- **URL:** https://www.youtube.com/watch?v=DSS1Yqb6-qE
- **Guests:** none

## What the video covers

This is a follow-up to the Roast Room video (summary 04). Nate Herk (Nate from here on) shows his council of AI advisers in use again, this time looking inside the repository that holds it and adding a new adviser live. Each adviser is a sub-agent styled on a well-known business figure and owns one question. A debate runs in rounds, and a verdict comes out with a score and a downloadable PDF.

The new material is the structure underneath. The repository now holds eleven seats. Each seat is a short agent file plus a "brain" folder of markdown built from public material, with the same set of files for every person. A new skill, called New Roster in the captions, builds a fresh adviser, brain and cartoon portrait on request, and he demonstrates it with Elon Musk. He then runs a live decision about where to hold a summer 2027 event, shows that the chair swaps a seat to suit the question, and opens the saved session files. Fish Audio sponsors the middle section. The skill is free through his Skool community.

## Chapter-by-chapter

**0:00 Meet the Roast Room.** Nate opens on a debate in progress between seven advisers, who attack one another's positions in turn. He reads out three seat questions: cash, risk and long-term value; whether people will pay; and whether the business can run without the founder. The debate ends in a verdict for option C, with a PDF to share. He stresses that the visual page is only a layer over ordinary Claude Code sub-agents. At about 1:35 he asks Claude how many seats exist and is told eleven (the default seven plus four extras). The four extras are named in his answer as Naval, Cody Sanchez, Sara Blakely and Leila Hormozi; the agents-folder listing at about 2:22 shows "Blake Lively", which is a caption garble of Sara Blakely.

**2:03 How the Advisors Are Built.** Each adviser is one markdown file in the project's agents folder, covering how they debate, how they talk and their lens. These files are short. The detail sits in a "brains" folder inside the skills folder, with one subfolder per person. Nate opens one and lists the same files in each: a summary sheet (the captions say "hot"; the real file name is unclear), books, frameworks, positions, principles, sources, stories and voice. In the example he opens (one of the four extra seats), the summary sheet states the seat's central question and what it was built from: 48 sources, about half a million words, dated 2021 to 2026, including 14 interviews and 34 of the person's own videos. Separately he says every person has eight rules they decide by; the captions do not make clear whether those sit in the summary sheet.

**4:46 Sponsor.** Fish Audio is promoted: a voice-generation model that takes plain-English direction for delivery, supports multi-speaker scenes, returns word-level timestamps for captions, and has an API, an MCP server and an n8n node. The model name is garbled in the captions.

**6:14 Build Your Own Roasters.** Nate describes the New Roster skill: ask for a person and it creates the agent file, the brain and the sources, plus a cartoon character for the visual page. He starts it for Elon Musk and leaves it running while he demonstrates a normal session.

**6:49 Running a Live Council.** He opens a fresh session, switches the model to Opus and asks, in plain language, where to hold an in-person event in summer 2027, listing four cities and the factors that matter (sponsors, local incentives, airports, transport, restaurants, things to do). Claude loads the skill, gathers context, asks four clarifying questions and recommends who should sit. Nate pretends the event is not yet decided. The chair drops one seat that focuses on protecting the founder's time and adds a seat whose question is whether a move builds leverage and equity or rents out time. He says he moved from agent teams to sub-agents after testing because teams cost more for little extra value, and that the sub-agents still address one another.

**10:06 Debate Logs and Opening Votes.** He opens the project's saved sessions: each holds a brief, round one, round two and a verdict, and each adviser's reasoning is stored and readable in the page. Round one posts a vote and a score out of ten per seat. Every seat backs the first city (option A, Salt Lake City) except the newly added leverage-and-equity seat, which prefers San Francisco (option B). He reads three votes aloud, all for the first city, and says everyone else did the same. He adds that unanimity would make the chair assign a devil's advocate, then argues for borrowing the proven thinking of people who have done what you want to do.

**13:13 Final Votes and Verdict.** Final votes arrive, with the leading city at 7.9 out of 10 at that moment, which he expects to be the final verdict. He points to each adviser's key points; one conceded to two others and disagreed most with a third. The PDF downloads, and the winning city matches the real decision made earlier.

**13:59 Adding Elon Musk.** The New Roster run has finished: a portrait, several views for when the character speaks, a new agent file and a new brain with the same set of files. Nate does not run Musk in a debate.

**14:34 Get the Free Skills.** He directs viewers to his free Skool community, classroom, AI skills or all YouTube resources, for the repository and his other free material. The captions end slightly earlier than the chapter marker.

## Key ideas and claims

1. Every seat owns one question, and the example questions cover cash and risk, willingness to pay, and dependence on the founder. Repeated from video 4. [0:00, 0:48]
2. **New.** The default room is now seven seats plus four extras, eleven in all, and he plans to add more. [1:35]
3. **New.** An adviser is a short agent file (how they debate and talk) plus a separate brain folder holding the substance. All brains share one file set: summary sheet, books, frameworks, positions, principles, sources, stories and voice. He also says each person has eight rules they decide by. [2:22, 3:10, 3:58]
4. **New.** The summary sheet records what the brain was built from (source count, word count, date range), which shows how much stands behind that seat. [3:10]
5. **New.** A New Roster skill builds a new seat, its brain and its portrait from a one-line request. [5:34, 13:35]
6. **New.** The chair recommends which seats attend, and the user can amend the list; here one seat was swapped because the question was about an event, not founder time. Video 4 only said the chair could convene a subset. [7:58, 9:33]
7. He says sub-agents replaced agent teams because, after a lot of testing, teams cost more for little extra value. Repeated from video 4, where the reason given was similar. His own claim; no comparison is shown. [8:46]
8. **New.** Sessions are stored as a brief, round one, round two and a verdict, so a debate can be reopened and questioned later. Video 4 also covered saved, replayable sessions; here he opens the files. [9:33, 10:21]
9. Unanimity makes the chair assign a devil's advocate. Repeated; here it is stated as a rule, not just something seen in one run. [11:09]
10. **New.** His wider argument is that following "someone that's actually walked the path you want to walk" is a better signal than trusting the model's own judgement or his own. He still does not accept results blindly. [11:59, 12:47]

## Tools, products and repos mentioned

| Name | What it is | Link |
|---|---|---|
| Roast Room repository ("Roaster Room" in captions) | Nate's free repo: agent files, brains, New Roster skill, optional visual page | No link given (reached through his Skool classroom) |
| Claude Code | Anthropic's coding agent; chair and host; Opus selected for the live run | No link given |
| Sub-agents and agent teams | Claude Code ways to delegate; he chose sub-agents | No link given |
| Fish Audio | AI voice generation; **sponsored section** at 4:46 | https://fish.audio/invite/?fpr=nateh (description; referral link) |
| Glaido | The description offers a free month of a voice-to-text tool; in the video (about 0:48 to 1:35) it appears to send his prompt, and he calls a new feature one that orchestrates chats between coding agents. These may be one product with a new feature, but the captions are unclear (rendered "Glydo"), so the link between them is an inference. Promotional, sponsorship not stated | https://get.glaido.com/nate (description) |
| Hostinger VPS | Hosting, discount code on annual plans; description only, not spoken; promotional | No complete link given (description cut off) |
| AI Automation Society (Skool) | His free community, where he says to get the repo from the classroom | Description link is cut off; his own comment gives https://www.skool.com/ai-automation-society/about |

No repository was opened by this review.

## How to apply it

The video is a tour and a demo, not a step-by-step build. The steps it shows are:

1. Get the repository from the community classroom (the AI skills or all YouTube resources areas). [14:34]
2. Write the question as a decision with two or three options and context. [7:09, 7:58]
3. Answer the chair's clarifying questions, then check and edit the recommended list of seats. [7:58, 8:46]
4. Let the rounds run: opening positions with scores, cross-challenge, final votes. [10:21 to 13:13]
5. Read each seat's key points and the saved session files, then take the PDF. [10:21, 13:35]
6. To add a seat, ask the New Roster skill for a named person and wait for the agent file and brain to appear. [5:34, 13:35]

## What viewers said

- **Pushback:** One commenter urges checking the legal position on putting a real person's name and views to an opinion they never gave, especially if shared. Another says that online material is a curated persona, so a seat may miss hidden working methods or a quieter partner. A third says that people act on advice only when they already agree with it, and that a model carries no responsibility, so trust is the missing piece, not the quality of the answer.
- **Questions:** What does a run cost? Did the Musk seat shift the outcome or mainly agree with the others? One request for a video on a different model.
- **Confirmations:** One practitioner says the lasting value is in how each seat is built on the person's real decision habits, and that without it the output is generic. Another says the rounds, not averaged answers, make the trade-offs visible. Others praise the demo without detail.

Comments are opinion, not fact. Names are removed.

## Relevance to Winstanley & Son

- **The advisory-board account already has the main structure** (chair, six-field brief, single-question seats, three rounds, forced dissent, dated verdict). This video adds detail, not a different design. Nothing here argues for rebuilding it.
- **Likeness is the point this video sharpens.** Video 4 already used named, living people; this one adds a new one on request. The account's rule of role lenses, never impersonation, is right, and the top comment about legal risk supports it. Keep the rule and write it into the account as a stated reason, not just a preference.
- **Seat knowledge sheets are worth borrowing in role-lens form.** A short dated sheet per seat (eight rules, sources, last reviewed) would stop a seat drifting into generic opinion. This is the Reference Brain Librarian idea from video 4, and it should report to the AI CIO's compliance register.
- **A founder-dependency seat fits a one-owner practice.** "Can this run without the owner holding it together?" matters when the owner is the only decision-maker and locums cover tests. It is a lens, not a named person.
- **Saved session files match the decision log.** A folder per decision (brief, two rounds, verdict) maps onto the AI CMO's scored log and the account's review-date step.
- **Limits are unchanged.** The video does not cover clinical matters, patient data, cost per run or approval. Recall intervals stay with the optometrist, only counts reach the board, and a verdict is advice.

## Account or role ideas this video suggests

1. **Seat sheet keeper (extension of the Reference Brain Librarian).** Mission: keep a one-page dated sheet per role lens with its question, rules, sources and review date. Source idea: the brain file set and its source tally [3:10, 3:58]. Reports to: AI CIO.
2. **Seat proposer step inside the advisory board.** The chair proposes which seats attend and why, and the owner can swap one. Source idea: the swap in the live run [7:58, 9:33]. Reports to: the owner, through the advisory board.
3. **Decision folder convention.** Each decision gets brief, round one, round two and verdict files, plus an outcome note at the review date. Source idea: saved sessions [10:21]. Reports to: AI CMO (decision log).
4. **Owner-dependency lens.** A seat that asks what breaks if the owner is away. Source idea: the third question at 0:48. Reports to: AI CEO, for the weekly pack.

## Sources used and confidence

- **Used:** the full auto-generated transcript, the description and chapter list, the creator's own comment and 20 public comments with names removed, the estate and business context files, summary 04 and the advisory-board account. No web searches were used, and the repository was not opened.
- **Confidence: high** for what the video says. **Medium** for the vote split at about 10:21 to 11:09 (the captions are choppy, but the lone dissenter reads clearly as the added seat). **Resolved from the transcript:** the four extra seats are named at 1:35; the source and word counts belong to one extra seat's summary sheet and are his on-screen figures, unchecked; Glaido's two descriptions may be one product with a new feature. **Not verified:** the Fish Audio model name (the captions give two different spellings), the file name rendered "hot", his cost claim for agent teams (his own, no comparison shown), whether seats actually read their brains before answering (he says they draw on them; not shown), and whether the Musk seat changes any verdict (never run). The added Naval seat dissented in round one but the leading city still won. The Skool and Hostinger description links are cut off. No cost per run is given.

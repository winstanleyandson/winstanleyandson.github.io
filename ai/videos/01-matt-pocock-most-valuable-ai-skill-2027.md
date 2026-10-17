# Matt Pocock: The Most Valuable AI Skill to Learn 2027

- **Channel:** Nate Herk | AI Automation
- **Published:** 16 October 2026 | **Duration:** 44:51 | **Views:** 62,315 (at collection)
- **URL:** https://www.youtube.com/watch?v=Z8lf5oWKfj0
- **Guests:** Matt Pocock (interviewee). Nate Herk hosts.

The transcript has no speaker names, only turn markers. Who says what is inferred from context: Herk asks, Pocock answers.

## What the video covers

This is an interview, not a build. Herk talks to Matt Pocock, a developer who coded by hand for about ten years and now has agents write all of it. Pocock's central argument is that the best results come from telling an agent what you care about and from improving the environment it works in (tests, checks, a way to see its own output), rather than hunting for a better model.

Other threads: distrusting what agents teach unless you read the primary source; the opportunity in fitting agents to each organisation's own processes; an interview skill, grill me, that surfaces what you have not thought of; why spec-driven development made his code worse over months; why he runs Opus 5.5 at medium effort; and a trust ladder for beginners. He also advises giving agents menial, checkable work first, which he sets against advice Herk attributes, without a source, to figures the captions give as Elon, Boris and Sam. A Hostinger sponsor read and a promotion for Herk's free AI OS kit sit inside the interview.

## Chapter-by-chapter

**Intro (0:00)**
Four teaser answers open the video (communication, unknown unknowns, opportunity, a spec-driven failure). Herk then introduces Pocock, says he uses his skills often, and notes Pocock taught himself to code and thinks it is easier than people claim.

**When Coding Agents Clicked (1:50)**
Pocock was a long-time sceptic, with about ten years of coding and about eight years of it professional (the captions leave unclear whether the eight sits inside the ten). He dates his turning point to December 2025, when Opus 4.5 was released and the OpenClaw project was built, after which he stopped writing code himself. The dating is his own recollection and was not checked. He had always liked improving his colleagues' working environment, so he applied that habit to agents. The captions split OpenClaw into two words (*Open Claw*).

**Tell Agents What You Care About (4:24)**
Asked how non-technical people can use engineering principles, Pocock says the human-agent communication gap never closes, so you must keep saying what matters and keep the agent's surroundings worth working in. He compares it to raising the floor for the weakest coder in a large team, using long-standing practice such as good tests. On trusting what agents teach him, he says do not: his teach skill fetches primary sources with quotes and links. He says hallucinations have fallen but not gone, and he uses teach sessions to get introduced to a topic before reading the source himself. A Hostinger sponsor read runs from about 8:26 to 9:37. One caption near 8:04 has him saying a model called Fable still invents things; the name is left as captioned and was not checked.

**Where the Opportunities Are (9:39)**
Pocock sees demand for teaching because organisations resist adoption, notes ethical worries about training data and energy use, and says the technology is staying. He rejects the idea that agents have no learning curve: trust, organising agents, controlling their information and turning processes into reusable ones all take work. Code is easy to verify, he says, but real-world work is not. The opportunity is fitting agents to each organisation's particular way of working.

**Unknown Unknowns & Grill Me (14:55)**
Herk asks how a non-coder can steer by intent without missing things. Pocock sees no divide between coders and others, since nobody fully knows their requirements. His grill me skill has the agent interview him persistently, exposing concerns like security and deployment. The skill, he says, is awareness that your design is incomplete. Herk adds that human inputs are unpredictable, so he tells clients he monitors what he builds.

**How to Stand Out (19:43)**
Herk asks how to look credible when anyone can build a portfolio in a weekend. An AI OS kit promotion (about 20:27 to 20:53) interrupts. Pocock admits he has never bid against others for work, but says clients want someone who understands what they care about, and a quick prototype can show it. Half-jokingly, he adds that if fast delivery unsettles a client, you can charge for five days of work, and he says he cannot give concrete advice on this. The best students, he says, are the best communicators. He recommends one shared vocabulary across code, product and client (domain-driven design), which his grill with docs variant builds up.

**The Spec-Driven Development Failure (26:03)**
Asked for a war story, Pocock says he kept detailed specs as the main artefact for his custom video editor, after an OpenAI talk at the AI Engineer conference argued specs are the new code. The captions give the speaker as *Shawn Grove*, which Pocock himself hedges; third-party write-ups name the OpenAI speaker as Sean Grove, but the talk itself was not watched. Over months the code and results got worse, so he went back to caring about the code as the agent's environment. Captions render spec-driven as *spectrum development*. He closes by saying models will never read minds, so a process layer will remain.

**Models, Harnesses & Effort Levels (30:48)**
Pocock runs about four agents on long tasks, experiments with a chief-of-staff skill that manages sub-agents, and reports far higher daily commit counts, about 200 to 300 against about 20 before (self-reported). He uses Claude Code with Opus 5.5 at medium effort and is considering lower, for token efficiency and faster replies, since tests catch mistakes. He says the biggest payoff came from getting his video-editor project into a state where the agent can click through it and take screenshots, and he thinks an older model such as Opus 4.5 with that setup would do about as well. Herk agrees clear communication beats a newer model.

**How to Get Started (35:27)**
Pocock suggests downloading his skills and any main harness without agonising over the choice, then climbing the trust ladder, an idea he credits to Lauren Tan (the captions say she works at GrokBot): learn the brake before the accelerator, start in an empty folder with a real idea, watch the agent closely, and only then add a second agent, skills and data sources such as Slack or email. Asked why some well-known figures tell people to give models their most ambitious tasks (Herk names Elon, Boris and Sam, with no source), he disagrees and recommends boring, measurable work first, such as draft replies. He says he drafts his written content with Sonnet 5.5 (captioned *Sonic 5.5*) and edits the result.

**What's Next for Matt (41:31)**
Pocock calls himself a teacher, not a pundit. He is excited by software factories that improve a code base over time, by agents that argue for doing things properly, by better ways of organising many agents (which he says nobody has found), and by open models reaching today's top level. He names a newsletter, Twitter and YouTube as places to find him; his site name is garbled in the captions.

## Key ideas and claims

1. Telling the agent what you care about gets the best work out of it, because the human-agent communication gap persists however capable the model [4:24 to 4:48].
2. The environment drives output quality: in his view a neglected code base produces poor agent work, and good tests and checks that raise the floor are the remedy he points to [4:48 to 6:27].
3. Treat agent teaching with scepticism: use it to get oriented, then read the primary source, which his teach skill supplies with quotes and links [7:15 to 8:26].
4. Agents have a hidden learning curve and real-world work is harder to verify than code, so the opportunity is converting each organisation's processes into something agents can follow [12:50 to 14:25].
5. Pocock cites The Pragmatic Programmer for the line "no one knows exactly what they want" (his citation, not checked against the book), and says interview-style prompting exposes unknown unknowns [15:59 to 17:36].
6. The best performers are the best communicators, and a shared vocabulary across code, product and client aligns everyone [22:27 to 24:53].
7. Keeping and refining detailed specs as the main document made the code and agent output of his video-editor project worse over months, so he went back to improving the code; this is one project and his own account [27:17 to 28:53].
8. Models and harnesses will keep improving but cannot read your mind, so a process layer stays necessary [29:41].
9. He claims most people set effort too high; with strong tests he uses medium and may go lower for speed and token efficiency [32:05].
10. Making the application runnable and visible to the agent was, in his experience, the largest gain, and he thinks an older model with that setup would do about as well [32:52 to 34:01].
11. Beginners should climb a trust ladder, an idea Pocock credits to Lauren Tan: begin narrow, watch closely, then add skills, a second agent and data sources [36:05 to 38:58].
12. Give agents menial, measurable work first, not your most ambitious task, because errors are cheap to correct [40:04 to 41:19].

## Tools, products and repos mentioned

| Name | What it is | Link |
|---|---|---|
| Matt Pocock's skills (grill me, grill with docs, teach) | Skill files for coding agents. The video and its description give no link; the repository page was opened directly on 17 October 2026 and shows an MIT licence and skills named grill-me, grill-with-docs and teach. His chief-of-staff skill is only an experiment. | https://github.com/mattpocock/skills (not linked in the video or description; checked directly) |
| Claude Code | Anthropic's coding agent harness, Pocock's current choice | no link given |
| Opus 5.5, Sonnet 5.5 | Anthropic models he says he uses: Opus 5.5 in Claude Code, Sonnet 5.5 for first drafts of written content (captioned *Sonic 5.5*, read as Sonnet). Names come from the captions and his own words, not checked elsewhere. | no link given |
| Codex, GitHub Copilot | Other harnesses he lists as acceptable starting points | no link given |
| OpenClaw | Agent project he links to the late-2025 turning point | no link given |
| VS Code | Editor he suggests for looking inside the code | no link given |
| Hostinger VPS (KVM 2, Claude Code template) | **Sponsored** cloud server, read at about 8:26 to 9:37 | http://hostinger.com/nateherkvps (description) |
| Glaido | Voice-to-text tool in Herk's description with a free-month offer; not mentioned in the video; promotional, sponsorship not stated | https://get.glaido.com/nate (description) |
| Free AI OS template (context, connections, capabilities, cadence) | Herk's own promotion, about 20:27 to 20:53 | https://app.aiautomationsociety.ai/optin/ai-os/ (creator's comment; the description link is cut off) |
| Skool community | Herk's free group, in the description only; link cut off there | no link given |
| Grok Bot (captioned *GrokBot*) | Employer of Lauren Tan according to the captions; Pocock credits her with the trust ladder | no link given |
| OBS, Descript | OBS is named as running locally for his video editor project. The captions read *Dscript* for the product the editor resembles; Descript is a guess. | no link given |
| Domain-driven design, The Pragmatic Programmer | Concept and book cited for shared vocabulary and unknown requirements | no link given |

## How to apply it

This is an interview, not a build walkthrough; the only step list is the beginner trust ladder at 36:05 to about 39:00, summarised in key idea 11.

## What viewers said

Comments are opinion, not fact. Most are short praise or first-post jokes; one is course promotion and the creator's own comment repeats the sponsor and promotion links.

- **Pushback:** One viewer asks whether insisting on human code review blocks truly automated, high-volume shipping. Another argues engineers overvalue tidiness and suggests agents might learn from several projects sharing one environment, with non-engineers consulted. A few say the interview never explained how to communicate with AI, that the skill is just reading and writing, or that Pocock is hype.
- **Questions:** Where to find Pocock's skills. A non-technical viewer feels overwhelmed and asks where to begin. Another asks whether others are winning clients as automation developers.
- **Confirmations:** One viewer, whose comment also promotes a course, says environment, context and feedback loops matter as much as the model and calls the trust ladder a good entry point. Another says Pocock's point about the harness matches their own trouble getting an agent to see a screen properly. One engineer says unknown unknowns are familiar from requirements work. One commenter says supplying reliable context to agents is vital and hard, that a document inbox is convenient but cuts against keeping files with their projects, and that summarising documents loses information (the comment is cut off). One non-coder says it transfers to their work.

## Relevance to Winstanley & Son

- **Mostly confirms what already runs.** The estate already has a grill-me skill, the five-stage change gate, the isolated test channel and the rule that agents draft while the owner presses. The trust ladder Pocock borrows from Lauren Tan and his raise-the-floor argument describe the same discipline, so this is reassurance, not a new build.
- **New: a shared shop glossary.** The estate notes mention no shared vocabulary file. A public-safe glossary defining order, draft, reglaze, stock job, recall band and the two sites' order prefixes could be read by skills, agent prompts and website copy, backing up the Slack agent's tolerance for natural speech. It must hold no patient data.
- **New: primary-source briefings for rules that must be right.** NHS eligibility, eye-test intervals and supplier terms demand accuracy. The teach pattern (quote, link, owner reads the source) suits them, as a briefing only, with no tax or clinical advice. It extends the source-and-date habit already planned for the AI CEO and AI CFO from figures to rules.
- **New: let the builder see its work.** The site is built by script and uploaded by Claude. The estate notes mention no automatic render-and-look check at phone and desktop width before upload. His gain from agents viewing their own output suggests one, if it does not already exist. His medium-effort setting is a cost idea to trial only after such checks exist and results are measured.
- **New: menial, measurable first jobs.** The owner's gaps include generic captions, paused review requests and no scorecard. Drafting captions or replies to existing reviews, scored by how much staff edit them, gives a first trust measure. Public content still needs owner approval.
- **Crewley.ai.** His view that buyers want someone who understands their business, and that value lies in fitting agents to each organisation's processes, fits done-for-you first. A grill-me style interview could open each audit. His pricing remarks are untested, by his own admission.

## Account or role ideas this video suggests

1. **Glossary Keeper.** Mission: maintain one public-safe vocabulary file and flag inconsistent terms across site copy, skills and agent prompts. Inputs: repo text, skill files, anonymised test-channel phrasings. Outputs: glossary updates as drafts. Guardrails: no patient data; owner approves. Source: 23:14 to 24:53. Reports to the AI CIO, whose registers are not yet maintained files.
2. **Process Capture Interviewer.** Mission: run short scheduled grill-me interviews with the owner or staff on named gaps (how an order is really handled, how a recall call goes, how patients heard of us) and write each into a dated process note with open questions. Guardrails: asks only, never changes live systems. Source: 16:47 to 17:36. Reports to the owner, copied to the AI CEO's weekly pack.
3. **Primary-Source Briefer.** Mission: on request, brief an NHS, VAT or supplier rule with quoted lines, dates and links, and name the one source the owner should read. Guardrails: no advice, no patient records, say so when sources conflict. Source: 7:08 to 8:26. Reports to the AI CEO.
4. **Site Preview Checker.** Mission: after each site build, render key pages at phone and desktop width, compare with the last build and report visible breaks before upload. Guardrails: read-only, never uploads; noindex and frozen-title rules respected. Source: 32:52 to 34:01. Reports to the AI CMO.
5. **First-Draft Assistant.** Mission: draft replies to existing reviews and caption variants, and record how much staff edit each (the measurement is the new part). Outputs: drafts plus an edit-rate figure for the weekly pack. Guardrails: nothing posts; no clinical or named-patient detail; owner approves public content. Source: 40:04 to 40:51. Reports to the AI CMO.

## Sources used and confidence

- **Used:** the full auto-generated transcript, the description and chapter list, the top public comments (names already removed), `business-context.md`, `estate-context.md`, a direct look at the skills repository page on GitHub, and one web search on the OpenAI talk (third-party write-ups only). The video links no repositories.
- **Confidence: high** on what was said and its order, since the transcript is complete and readable. **Medium** on proper nouns and model names, because the captions garble several (the OpenAI speaker, Sonnet, the site name). Self-reported figures such as commit counts are unverified.

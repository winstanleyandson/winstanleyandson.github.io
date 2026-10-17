# I Tested Sonnet 5.5 vs Opus 5.5. What You Need to Know.

- **Channel:** Nate Herk | AI Automation
- **Published:** 28 September 2026
- **Duration:** 25:49
- **Views:** 155,125 (at collection, 17 October 2026)
- **URL:** https://www.youtube.com/watch?v=7eo-11K2e3c
- **Guests:** none

## What the video covers

Nate Herk compares Anthropic's Sonnet 5.5 and Opus 5.5 by giving both the same prompt in seven separate sessions, all at high effort, and judging the results blind before revealing which model made which. The tasks are a landing page, a motion showreel, a 90-day growth plan for a new show, an investor deck with a spreadsheet, a visual explainer, a news dashboard and a resource guide written from one of his own videos. For each he reports run time, tokens and dollar cost at API rates. Opus costs roughly double per token, but over the whole set it cost only about 16 dollars more by his count.

His conclusion is a rule of thumb. Where the job has a clear spec and an obvious way to check the result, or where a reusable skill already defines good, start with Sonnet. Where the goal is vague, subjective or needs a creative thought partner, use Opus. He scores it four to three to Sonnet but says it was never a fair head-to-head. It is a model-choice guide, not a build.

## Chapter-by-chapter

Transcript blocks run to about 45 seconds each, so positions are approximate. Chapter times come from the video description.

**0:00 Sonnet 5.5 vs Opus 5.5.** Herk says Sonnet 5.5 is a clear step up from Sonnet 5, about 30 percent faster and 30 percent cheaper for most work. He has been using it on his real workflows (websites, messy data into spreadsheets, motion design, dashboards, planning) and promises speed, token counts and dollar cost for every test. The captions often render "Claude" as "cloud" and "Sonnet" as "Son of" or "Sonet".

**0:41 Pricing and Choosing Your Model.** He quotes Sonnet 5.5 at 2 dollars per million input tokens and 10 per million output, against 4 and 20 for Opus 5.5, so Opus is about double. He reads out Anthropic's own guidance: Sonnet for well-scoped everyday coding, bug fixes, high-volume development and polished documents, slides and spreadsheets; Opus for careful judgement, long-running agentic work and the hardest problems. His reading is that Sonnet suits work with a clear spec and an obvious check. He suggests testing each skill on both models and recording which wins. All runs were at high effort.

**2:07 Website Design Comparison.** The prompt asks for an immersive, high-converting landing page for a canned coffee-and-protein drink (name garbled in the captions, heard as "perk form"), using an image-generation service (heard as "key.ai"). Shown blind, one page has an interactive 3D hero that tracks the mouse but an invented can rather than the real product image; the other has a plainer hero but uses the genuine generated brand images. He prefers the second, which is Opus, but credits Sonnet's hero. Sonnet ran 28 minutes and Opus 52, with Opus costing about double. He would re-prompt Sonnet to use the real image and so gives this round to Sonnet.

**7:13 Motion Design Comparison.** Both models are asked to make a motion showreel for a product, researching branding on their own. The captions in this section are badly garbled, with unrelated coding phrases mixed into the narration, so I cannot report the showreel content in detail. Herk finds Sonnet's version creative and better than expected: it shows the product in use, has a voice-over he thinks came from a voice service (he guesses ElevenLabs), and a pixel animation that forms a letter G and turns into generated video. Opus's feels more on-brand, with better copy, a quote from him taken from the product's website and stronger sound design. Opus was faster and used fewer output tokens but cost more: Sonnet about 14 dollars and Opus about 20.55 (the caption reads "2055", and he later says about 20.5). Opus wins.

**9:57 Creating a 90-Day Action Plan.** A deliberately vague prompt asks for a research-backed plan to reach 1,000 subscribers for a new show (name garbled in the captions). Both first returned Markdown, then were asked for a readable document; Sonnet produced a local HTML page and Opus a Claude artifact. Sonnet's timeline launches on 2 November and feels crowded to him; Opus's runs as a Q4 sprint, is split by month and opens a task-level write-up with tick-off tasks that he says he could drop into a task tool (the captions garble its name). Opus ran 20 minutes against 14 and cost a little over 9 dollars against just under 5. Herk says a tightly specified prompt would have closed the gap, but on a vague one Opus wins.

**14:15 Spreadsheets and Investor Decks.** Both are given mock company data and asked for a spreadsheet and a pitch deck. The decks look very similar, share the familiar Claude house style and feel less than premium; Sonnet made slightly more slides. Both workbooks use formulas rather than hard-coded values, which he values because changing the data updates everything. Sonnet's workbook looks a little less polished but has more tabs. Opus was cheaper and faster here, so it takes the round.

**17:43 Visual Explainers With Skills.** Using his own simple HTML explainer skill, he asks what AI models his own PC could run. Opus's page explains the graphics-memory rule better; Sonnet's is more visual but explains less. Similar timing, but Sonnet cost half as much. He argues one follow-up prompt would bring Sonnet ahead and awards it to Sonnet.

**20:24 Building an AI News Dashboard.** The task is to scrape X for the day's AI news and build an interactive dashboard. Sonnet's dashboard has heat scores, filters, a content-plan list and a calendar. Opus's looks better, with posts-per-hour charts, rumour/shipped tags and a live scraping progress bar. Opus ran about seven minutes longer and cost about six dollars more. He says Sonnet gives you the baseline of what you asked for while Opus goes outside the box. Given the price, he awards it to Sonnet.

**23:16 Creating a YouTube Resource Guide.** Both use one of his existing skills to turn a link to a video into a resource guide. The outputs are near identical in structure and length. Sonnet was twice as fast and about 1.40 dollars cheaper, so it wins. His explanation is that the skill defined good clearly enough for a less capable model to follow it.

**24:49 Final Results and Takeaways.** Sonnet takes four rounds and Opus three. Across all seven runs Opus took about 46 minutes longer and about 38 million more input tokens, yet fewer output tokens, and cost about 16 dollars more, not double. He closes by urging viewers to test on their own skills and prompts.

## Key ideas and claims

1. Sonnet 5.5 is described as 30 percent faster and 30 percent cheaper than Sonnet 5 for most work. [0:00]
2. Listed prices: Sonnet 5.5 at 2 and 10 dollars per million input and output tokens, Opus 5.5 at 4 and 20, so Opus is roughly double. [0:48]
3. Anthropic's own guidance points everyday, well-scoped work and polished documents to Sonnet, and careful judgement or the hardest problems to Opus. [0:48]
4. Herk's rule: if the task has an objective definition of done, try Sonnet first; if it is subjective and you want a thought partner, use Opus. [1:36]
5. Run different skills on different models and record which model each skill does best on. [1:36]
6. Judge outputs blind, then reveal the model; he deliberately did not use his subscription so the cost shown is the API cost. [2:24, 6:21]
7. A wrong-looking result can often be fixed by re-prompting the cheaper model, so he judges what a second Sonnet attempt would likely reach. [5:34]
8. A vague prompt favours Opus; a precise prompt would narrow the gap and favour Sonnet's lower cost. [12:54, 13:41]
9. Spreadsheets that use live formulas rather than pasted values are the standard to ask for. [15:16]
10. Opus is not always the expensive choice: on the deck and workbook task it was cheaper and faster. [16:52]
11. A well-made skill lets a less capable model match a stronger one, shown by the resource-guide round. [23:58]
12. Overall result: four rounds to Sonnet, three to Opus, with about 16 dollars extra for Opus across all seven (his figure; a viewer says 26). [24:44]

## Tools, products and repos mentioned

| Name | What it is | Link |
|---|---|---|
| Claude Sonnet 5.5 | Anthropic's mid-priced model, tested | no link given |
| Claude Opus 5.5 | Anthropic's top model of this pair, tested | no link given |
| Claude artifacts and local pages | Opus's plan was shown as a Claude artifact and Sonnet's as a local HTML page; the captions do not say which app ran the sessions | no link given |
| ScrollCraft | Herk's free website design skill (scroll animation, layering, typography); promoted mid-video | https://app.aiautomationsociety.ai/optin/scrollcraft/ (full address from his own comment on the video; the description link is cut short) |
| AI Automation Society (Skool) | Herk's community, promoted in the description; also the source of his free resources | Description links are truncated; skool.com/ai-automation-s... |
| Glaido | Voice-to-text app with a free month, in his tools list; it is also the subject of the motion showreel round. Whether it is sponsored or an affiliate deal is not stated | https://get.glaido.com/nate |
| Hostinger VPS | Hosting; a discount code for 10 percent off the annual plan is in the description. Whether it is sponsored or an affiliate deal is not stated | Description link truncated: hostinger.com/vps/claude-... |
| Image generator (heard as "key.ai") and a voice service (guessed as ElevenLabs) | Used by the models during the runs; captions are garbled and he was unsure of the voice service | no link given |
| HTML explainer skill, YouTube resource-guide skill | Herk's own private skills | no link given |
| X (Twitter) | Scraped for the news dashboard | no link given |

No GitHub repositories are linked.

## How to apply it

Not a build. It is a model-choice comparison. The reusable takeaway is a method: run the same task on both models, record time and cost, and decide per task type.

## What viewers said

Comments are opinion, not fact.

- **Pushback on method:** The most-liked comment says Herk and others keep claiming a cheaper model could match with a re-prompt, and asks for a video that tests it. Two others say the setup was not a blank slate, since his existing memory files, skills and connected services shape what both models produce, so a newcomer would not reproduce the results. Several ask for an end-state test that measures total cost, including human time, to reach an agreed result, noting Sonnet may need more prompts; others ask for a different effort pairing.
- **Pushback on value:** One commenter cites a third-party intelligence and cost-per-task index to argue Opus at medium effort is a better default for coding than Sonnet at its highest effort. I have not checked those figures.
- **Preference and corrections:** One viewer preferred Sonnet's animated hero. One points out the final cost gap was about 26 dollars, not 16; I could not confirm which is right: the per-round costs given in the captions are too incomplete to total.
- **Questions and requests:** Requests for the motion-showreel prompt and skill, for how the demo videos were made and whether a video tool was used, for blind tests of future releases, and for a beginner series on everyday AI use.
- **Confirmations:** Several thank him, and one says the video cleared up when to use each model.

## Relevance to Winstanley & Son

- The estate already runs on a split of Fable orchestrating, Sonnet building and Codex reviewing. This video does not change that, but it gives a testable rule for the Sonnet half: use it where a spec and a check exist, which is exactly the lens-ordering, recall and finance routines already running.
- The "clear spec plus a way to check" test matches the five-stage change gate and the test channel. A new automation that cannot state its definition of done is a candidate for a stronger model during design only.
- The resource-guide round supports the existing practice of short, reusable skills such as the Essilor order and handoff skills: a good skill is what lets the cheaper model do a repeat job. New is the idea of recording, per skill, which model it was proven on.
- New to the estate: a small side-by-side bake-off with cost and time logged, run on two or three real, repeating jobs in the test channel before any model change, rather than choosing on reputation.
- The spreadsheet point (formulas, not pasted values) is worth carrying into the CFO read-only views and the Speke costing sheet, so figures stay checkable.
- The dashboard and website tests are consumer-style demos. Page titles are frozen for SEO and one session owns the site, so none of that applies directly.

## Account or role ideas this video suggests

- **Model bake-off clerk** (reports to the AI CIO). Mission: when a model or skill changes, run a fixed set of past tasks on both candidate models in the test channel and log time, tokens, cost and a pass or fail against the written definition of done. Outputs a one-page table per change. Guardrails: sanitised or fake inputs only, no live writes, owner decides. Idea from 1:36 and 5:34.
- **Skill-to-model register** (reports to the AI CIO). A maintained list saying which model each shared skill was proven on and the date. Guardrail: updated only after a recorded test. From 1:36.
- **Spec-checker for new requests** (reports to the AI CIO). Before a build starts, asks "what is the checkable definition of done?" and flags vague requests for a design conversation rather than a cheap build. From 12:54.
- **Spend note for the AI CFO view** (reports to the AI CFO). Adds a monthly line of agent run cost per routine beside its output, so cost per result is visible. From 24:44.

## Sources used and confidence

- Transcript (auto-generated captions, taken from YouTube's transcript panel), the video description, the chapter list and the top public comments in the collected data file.
- No web searches were used.
- **Confidence: medium.** Prices, run times and the final tally are clearly stated. The motion-design chapter has heavily garbled captions (the Opus cost is recoverable as about 20.55 dollars from his later remark), and the final dollar gap differs between the narration and one viewer comment. The 30 percent and price figures are Herk's own and were not checked against Anthropic's price page. The model-quality judgements are Herk's own opinion on single runs, not a controlled test.

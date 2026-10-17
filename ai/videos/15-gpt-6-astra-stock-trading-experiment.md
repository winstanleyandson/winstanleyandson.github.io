# I Gave GPT 6 Astra $10,000 to Trade Stocks...And This Happened

- **Channel:** Nate Herk | AI Automation
- **Published:** 28 September 2026
- **Duration:** 18:00
- **Views:** 128,092 (at collection, 17 October 2026)
- **URL:** https://www.youtube.com/watch?v=eg_1NXDcoPk
- **Guests:** none

## What the video covers

Nate Herk gives a Codex agent running GPT-6 Astra $10,000 of real money and seven trading days to beat the S&P 500. He filmed it as a daily diary. The interesting part for anyone building agents is the set-up, not the money. Six scheduled "routines" wake the agent through the trading day, all in one Codex thread, and each leaves a handoff message that the next one reads, so the run feels like one continuous worker. When Astra declined to place trades itself, Herk added a second agent, a Grok Bot with its own email address, which received Astra's recommendations by email and placed the orders through a broker. He allowed himself up to two strategy changes a day and used them to loosen the agent's filters after it traded too cautiously. The account finished at $9,900 against $9,980 for the S&P, so he lost his own bet. He admits seven days proves little and plans a longer follow-up. It is an experiment, not a build walkthrough.

## Chapter-by-chapter

Chapter times come from the video description. The captions garble product names; I have read "codeex" as Codex, "GBT6" as GPT-6 and "Grockbot" as Grok Bot.

**0:00 The $10K AI Gamble.** The opening plays clips from later in the run, then states the rules. Herk previously did a similar test with another agent tool, but breaks his earlier rule of leaving a system untouched once built: this time he may make up to two changes per day, and he cannot stop the agent trading even if he loses all the money. The result is judged against the S&P 500. If he loses, one viewer wins a free ticket to his October event.

**0:56 Day 0.** The market is closed, so this is set-up day. He asked the agent to research and propose a strategy, and it handed work to several sub-agents. The plan uses six action wake-ups (pre-market news and watchlist, an early look for a first trade, a midday review, an afternoon position check, a 2:15 close-out of remaining positions and a final confirmation and record) plus two notification runs. Every run reads the previous run's handoff note and writes one for the next. All routines share one thread, so he can watch everything in one place. They are shown as inactive until trading begins.

**2:48 Day 1.** The account ends at $9,991, a loss of about nine dollars. The agent bought Tesla with a stop, and the stop triggered almost at once. Herk is frustrated by the lack of risk-taking and says he would sooner have lost $500 than seen so little activity. He tells the agent to be more active; it replies that it should have acted on his feedback sooner. The fix is three entry reviews a day and a lower required reward-to-risk ratio (2:1 down to 1.5:1).

**4:07 Day 2.** Astra stops placing trades, which Herk describes as a model restriction he could not talk it out of. His workaround is the Grok Bot called Trader. A webhook fires when an email reaches the bot's address, the bot reads the recommendation and places the trade with the Alpaca broker. Astra still does the research and strategy. The day is almost flat again, and the weak spot is that the agent finds a good candidate and then rejects it at a last gate. He plans to remove some gates, wake the agent more often (perhaps every 30 minutes) and make it more aggressive.

**5:58 Day 3.** This is a weekend check-in covering Friday. The account is up about $18, holding three positions (technology hardware, an oil major and a phone maker) and roughly 60% in cash. Herk says he is not trying to turn $10,000 into $15,000 in a week and is not a day trader; the aim is only to beat the S&P. He explains the S&P as a basket of the 500 largest US companies and notes that the index was slightly down since the start. He plans to push the agent to use more cash.

**8:02 Day 4.** The account fell overnight to $9,876. The agent sold everything before the open and then bought three positions, taking about 80% of the money into the market. By close it is down $225 (about 2.3%) against about 0.5% for the S&P. It also bought an S&P fund, which Herk finds odd given the goal and says he will ask the agent about.

**10:04 Day 5.** The agent is now almost fully invested. The day ends at about $9,833, up around $36 against a small fall in the index, but still about $100 behind the S&P over the whole run. Herk observes that even with nearly all the money invested, the account moved by only tens of dollars, and says investing is mostly a long-term game unless you take large risks. He asks viewers whether they want 30-, 60-, 90-day or one-year follow-ups.

**12:15 Day 6.** The US central bank raises rates by a quarter point, from 3.75% to 4%, and the S&P drops. The portfolio falls with it, closing at about $9,759, down $85 on the day against about 0.45% for the index. The agent sold much of its holdings after the announcement, sat on about $7,000 of cash for an hour or so, then bought again. Herk wants the idle cash working on the last day.

**14:34 Day 7.** The morning briefly shows a gain, then a sharp drop; the agent sells one holding before it falls further. Herk resolves to keep his hands off. He says the account ends at $9,900, up $182 on the day (1.87%) against 1.14% for the S&P, while $10,000 put into the S&P would be $9,980, so he loses by about 0.8 points. His own figures do not quite add up (see the checks at the end).

**15:22 Final Results.** Herk says he effectively got five real trading days because the first two were too passive. He suggests options could magnify both gains and losses, plans to keep tuning, and recalls a longer earlier test that did beat the index. He concedes seven days is not enough to judge the strategy. The prize draw is explained.

## Key ideas and claims

1. Scheduled routines in one shared thread, each leaving a handoff note for the next, make several short runs act like one continuous agent [1:54].
2. A day can be split into fixed jobs: research, look for entries, review, manage, close out, record [0:56].
3. By Herk's account the model would not place trades itself, so a second agent was given the execution step through an email-triggered webhook [3:43, 4:40].
4. Separating the thinker (strategy and research) from the doer (placing orders) is a workable design when one model will not do the act [4:40].
5. The agent was cautious to the point of inaction; Herk's remedy was loosening gates and lowering the reward-to-risk threshold [3:43, 5:34].
6. Human changes during the run are a central confound: the agent was not trading alone [2:48, 5:34].
7. Short-run results are mostly noise; Herk says seven days does not show whether the strategy works [17:36].
8. Over the whole run the portfolio finished at $9,900 against $9,980 for the S&P [14:56, 16:41]. Herk's day-by-day figures are reported as he gives them and I have not checked them against broker records.
9. A macro event (the rate rise) moved the portfolio and prompted the agent to sell and rebuy within the day [12:15].
10. Herk says an earlier 30-day stock-only test beat the index; this is his claim and is not shown here [15:49].

## Tools, products and repos mentioned

| Name | What it is | Link |
|---|---|---|
| Codex | Coding agent app, used here to run scheduled routines in one thread | no link given |
| GPT-6 Astra | The model Herk ran in Codex, set to high effort | no link given |
| Grok Bot, named Trader (captions say "Grockbot"; spelling is my reading) | A second agent with its own email address, woken by a webhook, that placed the trades | no link given |
| Alpaca | Brokerage with an API, used to execute orders | no link given |
| Glaido | Voice-to-text app, promoted in the description with a free month; the description does not say whether this is sponsored or an affiliate deal, and the video does not mention it | https://get.glaido.com/nate |
| Hostinger VPS | Server hosting, promoted in the description with a discount code; sponsorship is not stated and the video does not mention it | no link given (description link cut short) |
| Skool communities | Herk's communities, advertised in the description (one is labelled free) | no link given (description links cut short) |
| S&P 500 | The benchmark index | no link given |

No GitHub repositories are linked. I did no web searches for this video.

## How to apply it

This is not a build walkthrough; the set-up is shown briefly and no prompts, schedules or code are given. The reusable pattern (scheduled runs plus handoff notes) is covered under relevance below.

## What viewers said

Comments are opinion, not fact.

- **Pushback.** The most liked comment says the video does not show AI can trade profitably: the account lost about 1%, trailed the index, was changed by the host repeatedly, and ran only seven days. The same commenter objects to pushing for more trades and less cash as a goal in itself. Others agree the agent was not acting alone, call the thumbnail misleading, and say the real test is whether it can devise a sound strategy, which they feel it did not show.
- **Questions.** Why hold an S&P fund if the aim was to beat the S&P? Who is really deciding when a human sets the goals and the risk? One asks to see the strategy it used.
- **Suggestions.** Many want 30-, 60-, 90-day or year-long updates, other models, options, futures, exchange-traded funds or a goal-based end point. One notes paper trading exists on the broker.
- **Confirmations.** A few say it was a good experiment and thank him; one says personal judgement is never replaceable.

## Relevance to Winstanley & Son

- **Already live and touched.** The estate already runs scheduled agents with a watchdog, a Slack test channel and a handoff discipline. The video's routines-with-handoff-notes is the same idea in a different place; it confirms the design rather than adding one. Do not build another handoff skill: `session-handoff` is live.
- **Genuinely new: a sequence of runs as one worker.** The estate's agents are mostly event-triggered. A day-shaped chain (morning prepare, midday check, closing summary, each reading the last note) could suit the Frame maker's own daily rhythm, for example a morning brief, a midday check that reads the existing alerts and an end-of-day summary, provided each only reads and reports. Missed-call and late-order alerts are already live, so the chain would read them, not rebuild them.
- **Split thinker from doer.** Herk's second agent did the act the first would not. Here the equivalent is already the rule: the agent drafts and flags, a person presses "OK to send" and the owner presses activation. Treat a model refusing an action as a signal to keep the human step, not to engineer around it.
- **The cautious-agent problem.** Herk loosened gates because the agent did too little. In a clinical and supplier setting the opposite lesson applies: a conservative agent that holds and asks is a feature. Any loosening should go through the five-stage change gate, not a same-day tweak.
- **Interventions confound results.** His tuning during the run is why the result proves little. When the estate measures a new agent, freeze the rules for the trial window and log every change, as the change register intends.
- **Not applicable.** The money side is out of scope. The practice should not trade, and nothing here is financial advice; the video is useful only as an example of agent routines and handoffs.

## Account or role ideas this video suggests

1. **Day-Shift Conductor** (reports to the AI CIO) [0:56, 1:54]. Mission: run a fixed daily chain of read-only checks that hand notes forward. Inputs: scheduled slots, the previous note, existing alerts. Outputs: one daily thread and a closing summary. Guardrails: reads and reports only; no patient names in notes; the watchdog confirms each slot produced output.
2. **Action Gatekeeper** (owner) [4:40]. Mission: keep drafting and executing separate. Inputs: drafted actions from other accounts. Outputs: a short approval list for the owner. Guardrails: nothing leaves without a human press; a refused action is recorded, not routed round.
3. **Change-During-Trial Logger** (AI CIO) [2:48, 5:34]. Mission: record every rule change made while an agent is being evaluated. Inputs: edits to prompts and thresholds. Outputs: a dated log beside the results. Guardrails: results are labelled "changed during run" if rules moved.
4. **Benchmark Referee** (AI CEO, read-only) [16:41, 17:36]. Mission: for any new automation, state the baseline and the minimum evidence period before any verdict. Outputs: a one-line "enough evidence / not yet" with the sample size. Guardrails: says "not measured" when unsure.

## Sources used and confidence

Sources: the transcript (auto captions, with names garbled), the description (links cut off, empty links list), the top public comments, `business-context.md` and `estate-context.md`. No web searches were made, so product details are as Herk states them. No repositories were linked.

Dates: the transcript says the challenge began on Wednesday 9 September and day 5 was Tuesday 15 September, so day 7 was 17 September; the video was published 28 September. That is consistent; the comments' "two weeks ago" is only YouTube's rounding. Claims to verify: Herk's figures are not fully consistent (day 6 close of $9,759 plus a $182 gain on day 7 would be about $9,941, not $9,900; the day 7 gain is also given as $153 earlier that day, and the day 6 loss does not match the day 5 close exactly), so treat daily numbers as approximate. The captions garble some figures (the margin of 0.8 points is only recoverable from $9,980 against $9,900). The "model restriction" on trading is his account, not confirmed by the model's maker. The earlier 30-day test that beat the index is his claim, not shown. Sponsor and community links are cut short in the description. No text addressed to AI assistants appeared in the transcript, description or comments.

Confidence: **high** for what was shown and said, since the transcript is clear and the story is simple. **Low** for any conclusion about AI trading skill, because the run was seven days, changed by hand and unaudited.

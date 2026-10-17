# I Tried 100+ Github Repos for Claude. These 6 Are the Best

- Channel: Nate Herk | AI Automation
- Published: 11 October 2026 | Duration: 10:37 | Views: 238,876 (as captured on 17 October 2026)
- URL: https://www.youtube.com/watch?v=HhZdNYI4pJs
- Guests: none

## What the video covers

Nate Herk (Herk from here on) goes through the free GitHub projects he says he leans on most when building with Claude Code. Each gets about a minute: the problem it solves, an example prompt and who might pay to have it set up. The first half is about winning clients (video editing, Google account access, data scraping, website design, copy clean-up). The second half is about building well (planning files, mobile apps, database and payments, browser testing, security review, search data). He finishes with token-saving add-ons, a JetBrains test and a spend tracker, and advises installing one tool at a time.

Two cautions. The title says six, but he says ten out loud and the description links twelve (Supabase and Stripe share a slot, and the security plugin is unnumbered). He never explains the six. And the frame is someone selling AI services to small firms, so many of the reasons given are about earning from the tool. One repo, Scrollcraft, is his own, and he says so. The description also promotes his paid community and two promo links (see the table); he does not mention them in the video.

## Chapter-by-chapter

Chapter times come from the description. The transcript is auto-captioned and garbles some names (HeyGen is captioned as Haygen, Supabase as Superbase, Apify once as Appy Pie). I have corrected these from the repo files.

**0:00 Finding the Best Claude Repos.** Herk says there are over 100,000 Claude-related repos and most are a waste of time. He tried more than 100 and says ten are ones he cannot work without. He promises to show what each fixes and how to turn it into paid work.

**0:24 Video Editing With Hyperframes.** HyperFrames, from HeyGen, lets Claude build a video from HTML and animation and render a real MP4 on your own computer. He drops in a raw clip and asks for captions, a title card or a Reel, with his own skills on top. He prefers it to Remotion, says the video is not sponsored, and says it is open source with no per-render fees (the README says the same for the open-source tool; HeyGen's hosted cloud rendering is a separate option whose pricing was not checked). The suggested business is a monthly caption-clip package.

**1:28 Google Workspace CLI and Apify.** The Workspace CLI is a command-line tool that lets Claude Code, Codex or other agents work on Drive, Gmail, Calendar, Docs, Sheets and Slides. He says it ships with 40+ skills (the README says 40+ in its heading and 100+ lower down), setup needs a Google Cloud project, and Claude's built-in Google connector works only in the desktop app and is narrower. Anthropic's help pages list the Gmail, Calendar and Drive connectors on claude.ai as well as the desktop app, so the desktop-only part looks wrong or out of date. Apify's MCP server gives Claude ready-made scrapers for sites that block plain fetches or need JavaScript, for example listing Chicago bakeries on Instagram with no website in their bio. The connector is open source, but scrapers run on Apify's cloud and are charged per result, after a free monthly credit he puts at $5 (not in the README; secondary price guides agree).

**3:09 Better Websites and Human Copy.** Scrollcraft gives Claude a scroll engine and design rules for Apple-style scroll-driven sites, plus a checker that screenshots scroll positions so Claude can fix faults before being asked. He says all his own sites use it and pages need not be fully immersive. Humanizer is built on the guide Wikipedia editors use to spot AI writing. It removes tells such as contrast set-ups, groups of three and hype words while keeping the meaning.

**4:57 Planning Builds With Agent Skills.** Long sessions get compacted and lose early detail, which he calls context rot. Addy Osmani's Agent Skills (Herk says Osmani put in 14 years at Google before moving to Anthropic to work on Claude Code; news reports found by search agree) move the plan into files: a spec, a task plan, then a build that goes one task at a time with a check on each. A fresh session can resume from the files. The spec step raises edge cases such as double bookings, refunds and time zones, and can be shown to the client. He rates Superpowers as still good but harder for beginners, and adds Matt Pocock's skills as a bonus.

**6:20 Expo, Supabase, and Stripe.** Expo's official skills take an idea to an app running on your own iPhone in an afternoon, with Expo's list of 20 signs an app looks AI-built (the Expo repo does carry such a list) and the current store rules. Tips: name the Expo skills in your prompt, as he says they do not always load; TestFlight or the App Store needs a $99 a year Apple developer account. Supabase and Stripe skills carry each company's security rules, such as users seeing only their own data and checking a payment really came from Stripe. He says to install only Stripe's best-practices skill, set the Supabase connector to read-only, and test as one user before launch. The read-only advice is his; the Supabase skills in the repo do not mention it, though they do advise scoped access tokens for agents and the MCP server.

**7:34 Browser Testing and Security.** Claude may report that a feature works without clicking anything. Microsoft's Playwright CLI opens a real browser, clicks through like a customer and writes tests you can rerun. He says that as a command-line tool, not an MCP, it uses fewer tokens; the Playwright README makes the same argument. Claude Security is Anthropic's plugin: a team of agents looks for weaknesses, others try to disprove each finding, and you get a plain-English report with optional patches. His point: clients care that the booking form works and data does not leak.

**8:32 SEO With Real Data.** Open SEO connects Claude to real keyword, ranking and backlink data, so advice names the exact page and keyword. He warns that free trial credit is small and data sits on its server unless you self-host.

**8:56 Token Savers and Usage Tracking.** He reports a JetBrains test: Caveman cut about 8.5% of output tokens against 65% advertised; RTK saved little or nothing and cost more at low effort; Ponytail saved about 10% per task, half its claim, and has what he calls an open Windows bug that can stall each message for several seconds. Codeburn shows where tokens go and flags waste, such as an unused MCP server loading on every message. He now says to hold off on two add-ons he recommended in May: Claude Mem, which he says reports usage data unless you change a default, and Context Mode, which he says has an open bug that can use up your allowance. Claude Mem's own documentation confirms anonymous telemetry is on by default with an opt-out; I found nothing on the Context Mode bug.

**9:46 Where to Start.** Do not install everything; if something breaks you will not know which repo did it. Pick the one matching your biggest current problem, or start with the Google CLI, Apify, Scrollcraft or Humanizer. His exercise: find businesses with no website, build a sample page, tidy the copy, send the link. The repos are free, so what you sell is the work built around them.

## Key ideas and claims

1. [0:00] Of 100,000+ Claude repos most are not worth the time; ten passed his testing (the title says six).
2. [0:00 to 0:47] Herk says HyperFrames renders MP4s locally from HTML with no per-render fee, so editing stops being his team's bottleneck. The README backs the no-fee point for the open-source tool.
3. [1:35] Herk says a command-line tool can be used by any agent, while Claude's Google connectors work only in the desktop app and are narrower. The desktop-only part conflicts with Anthropic's help pages, which list those connectors on claude.ai too; the narrower-coverage point is unchecked.
4. [2:23] Scrapers behind an MCP reach sites that return empty pages to Claude; the server code is open source (MIT licence) but the scrapers are metered.
5. [3:10] Herk says design rules plus a self-check beat a bare prompt for websites; Scrollcraft screenshots scroll positions to find faults.
6. [3:57] Herk says copy improves when a known catalogue of AI tells, taken from a Wikipedia editors' guide, is removed.
7. [4:45] Herk's view: long sessions lose early detail (context rot), so put the plan in files (spec, plan, build) and a fresh session can resume.
8. [5:33] A good spec step surfaces edge cases (double bookings, refunds, time zones) and doubles as a client document.
9. [6:19] Name the Expo skills in your prompt; he says they do not always load on their own.
10. [7:06] His advice is to install narrowly: only Stripe's best-practices skill, Supabase read-only, test as a single user.
11. [7:06 to 7:54] Herk says Claude reporting that something works is not proof; a real browser run is. He also says a command-line tool costs fewer tokens than an MCP, which the Playwright README argues too.
12. [8:41 to 9:28] Citing a JetBrains test, Herk says token-saving add-ons delivered less than advertised; a spend tracker can flag waste such as an unused MCP server that loads on every message.

## Tools, products and repos mentioned

| Name | What it is | Link |
|---|---|---|
| HyperFrames (HeyGen) | HTML-to-MP4 video renderer with agent skills; Apache 2.0, needs Node 22+ and FFmpeg | https://github.com/heygen-com/hyperframes |
| Google Workspace CLI (`gws`) | One CLI for Drive, Gmail, Calendar and more with agent skills; README says not an officially supported Google product | https://github.com/googleworkspace/cli |
| Apify MCP server | Connects Claude to Apify's scraper store; MIT licence; hosted at mcp.apify.com | https://github.com/apify/apify-mcp-server |
| Scrollcraft (Herk's own) | Skill for scroll-driven sites; a free copy sits behind an opt-in page for his community | https://github.com/nateherkai/scroll-craft |
| Humanizer | Skill that removes 26 AI-writing patterns; README lists cfo.ai as its sponsor | https://github.com/blader/humanizer |
| Agent Skills (Addy Osmani) | 25 skills and 9 commands (spec, plan, build, test, review, ship) | https://github.com/addyosmani/agent-skills |
| Expo Skills | Official skills for building and shipping Expo mobile apps | https://github.com/expo/skills |
| Supabase Agent Skills | Official skills for the Supabase database and auth platform | https://github.com/supabase/agent-skills |
| Stripe best-practices skill | Stripe's skill for payment integration decisions | https://github.com/stripe/ai/tree/main/skills/stripe-best-practices |
| Playwright CLI (Microsoft) | Command-line browser driver with skills | https://github.com/microsoft/playwright-cli |
| Claude Security (Anthropic) | In-session multi-agent security scan and patch plugin | https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-security |
| OpenSEO | Open-source (MIT) SEO tool and MCP; needs a paid DataForSEO key; the hosted version adds 28% to DataForSEO costs | https://github.com/every-app/open-seo |
| JetBrains token-saver test | The test Herk cites for the savings figures. Not linked in the video or description. Caveman and RTK figures match search extracts of it; Ponytail's match only a secondary write-up | https://blog.jetbrains.com/ai/2026/07/rtk-claude-code-token-savings/ (found by web search; the page refused my automated fetch, so not opened) |
| Codeburn | Local spend tracker for coding agents; free and open source per directory listings. Not linked in the description | https://peerlist.io/iamtoruk/project/codeburn--see-where-your-ai-coding-tokens-go (directory page found by web search; fetch refused, so not opened) |
| Glaido and Hostinger VPS, plus Herk's own community links | Promotional links in the description (free month, 10% code, paid community); the video does not mention Glaido or Hostinger. Treat as sponsored or affiliate | Glaido: https://get.glaido.com/nate; Hostinger link truncated in the description |
| Named in passing: Remotion, Firecrawl, Superpowers, Matt Pocock's skills, Square, Caveman, RTK, Ponytail, Claude Mem, Context Mode | Rivals, other skill sets, a till system, token savers and memory add-ons | no link given |

## How to apply it

Not a build: it is a survey of tools. His closest thing to a method, at [9:28], is to adopt one tool at a time.

## What viewers said

Comments are opinion, not fact.

- **Pushback.** One viewer says token savers cost more in worse output than they save. Another says the AI-made motion graphics in his videos weaken the personal feel. Another says OpenSEO is only a front end for a paid data supplier that takes a cut (the README confirms a hosted mark-up of 28%). Another says Humanizer cannot remove a watermark they believe Anthropic added in the EU (press reports from August 2026 say Anthropic has started marking Claude text worldwide, not only in the EU, and that editing can remove such marks; whether Humanizer does so is untested, and its README says beating detectors is not a goal).
- **Questions.** The most-liked comment asks how he checks a repo is safe before installing, and whether to switch off automatic updates for untrusted sources. Others ask for a Codex version and for a regular series on useful repos.
- **Confirmations.** Many say it saved time or solved specific problems. One reports good results with Scrollcraft, one vouches for Matt Pocock's skills, and one says the pick-one-first advice helps beginners. One suggests exposing narrow actions through an MCP, not handing an agent an OAuth token. One says an AI scan of a repo gives only partial confidence, so a human check still matters.
- Herk's own comment is promotional links only.

## Relevance to Winstanley & Son

- **Mostly already covered.** Specs, files and fresh sessions are what the five-stage change gate, handoff notes and shared skills already do. Agent Skills' `interview-me` skill overlaps `grill-me`.
- **New and cheap: a browser check after each website push.** The site goes up when Claude drives the GitHub upload page, one session owns it, and no scripted post-push check is listed. Playwright CLI could open the live site at phone and desktop sizes and check the booking widget and phone links. It must not submit forms or create real bookings.
- **Humanizer's 26-pattern list as a review rubric** for the generic social captions and long guides. It would tidy style only and never touch NHS eligibility or clinical wording. Staff and customer posts still need owner approval.
- **HyperFrames for the short vertical videos.** Social already runs in monthly batches through the GHL Social Planner, with YouTube unlisted embeds on the site; captions and title cards are the new part. Its skills already appear in the local skill list, so this is a trial, not an install. Output stays draft files.
- **Weigh, do not adopt.** The Workspace CLI adds a Google login with its own permissions and overlaps the AI CFO's read of Sheets, so compare it there. Apify and OpenSEO add paid third-party services, and Scrollcraft means heavy scroll-driven pages on a static site built by a script. Claude Security would be a second opinion beside Codex, the sole reviewer, and needs an owner decision.
- **Vetting and spend.** A spend tracker fits the AI CEO plan to measure, then cost. The unanswered safety question fits the AI CIO's registers. Skip the token-saver tools.

## Account or role ideas this video suggests

- **Tool Intake Reviewer** [9:28]. Before any third-party skill, plugin or MCP is installed, it reads the source, notes what data leaves the machine and what it can write, pins a version and logs it. Reports to the AI CIO.
- **Copy Tells Checker** [3:57]. Marks AI tells in drafts of captions, guides and replies and suggests plainer wording, never changing facts. Reports to the AI CMO.
- **Reel Finisher** [0:47]. Turns workshop clips into captioned, titled draft Reels. Never posts. Reports to the AI CMO.
- **Site Smoke Tester** [7:54]. After each website push, checks the live pages in a real browser at phone and desktop widths. Before a push it can also look for keys or patient data in the public repo. Reports to the AI CIO.
- **Search Visibility Reporter** [8:41]. Monthly pull of keyword and ranking data for a short list of local searches into the CMO's numbers ledger, flagged as third-party reported. Needs an owner decision on cost and a new key. Reports to the AI CMO.
- **Spend Watcher** [9:28]. Weekly line on agent spend by project and on unused tools loading every message. Reports to the AI CIO, with the money figure passed to the AI CFO.

## Sources used and confidence

Sources: the transcript (auto-captions; each block timestamp starts about 48 seconds of speech, so a claim may sit up to a minute later), the description and links list, about 40 public comments (text only, no names), the business and estate context files, and the cloned READMEs and a few skill files for all twelve repos (read only, nothing run). Web searches: the JetBrains token-saver test (Caveman and RTK figures matched; Ponytail only via a secondary summary), Codeburn, Apify's free plan, Addy Osmani's move to Anthropic, Claude's Google connectors, Claude Mem's telemetry and Anthropic's text marking. The JetBrains and Codeburn pages refused automated fetches, so only search extracts were seen.

Confidence: high on what the video says, because it is short and clear. Medium on whether its claims are true. Checked and supported: the HyperFrames no-fee point, the Apify free credit, Osmani's move, the Claude Mem default, the Caveman and RTK figures. Contradicted: the desktop-only limit on Claude's Google connectors. Still unchecked: the Context Mode bug, the Ponytail figures beyond one secondary summary, the Supabase read-only advice, and HeyGen cloud rendering prices.

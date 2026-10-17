# Handoff: Nate Herk's last 10 videos -> AI accounts + md files

Started in a Claude Code cloud session on 17 October 2026, moved to local at the user's request.
Branch: `claude/pensive-ride-e880xu`. Continue locally from a clean checkout of this repo with:

```
claude --teleport session_01N57o8nGapzJHPSEgPFw9pH
```

(or claude.ai/code -> this session -> Open in -> Terminal). Teleport loads the full conversation history.

## The request

"Use 10 agents to look at the last 10 YouTube videos of Nate Nurk [= Nate Herk, @nateherk, 'Nate Herk | AI Automation'],
use the transcripts to summarise, then use the data to structure out AI accounts and md files."

Working interpretation of "AI accounts": a structured roster of AI agent accounts (roles) for Winstanley & Son,
one markdown definition per account, derived from the patterns in the videos and mapped onto the practice's
real systems (GHL, VisionPMS, Make, Stannp, GitHub Pages site, social batches). Confirm with Gavin if a different
meaning was intended (e.g. AI OS setup, or AI-run social accounts).

## Why the cloud session stopped

- The cloud environment's network policy denies every youtube.com host (www, m, youtu.be, music, nocookie, googlevideo).
  The transcript/caption CDN lives there, so transcripts could not be fetched. `youtubei.googleapis.com` IS reachable,
  which is how the metadata below was collected. Remedy if the cloud route is ever wanted: environment settings ->
  Network access -> add `www.youtube.com` under Allowed domains.
- Everything else was gathered and is in this folder.

## The 10 videos (channel Videos tab, long-form only, as of 17 Oct 2026)

| # | Published | Length | Views | Title | ID |
|---|-----------|--------|-------|-------|----|
| 1 | 16 Oct 2026 | 44:51 | 62k | Matt Pocock: The Most Valuable AI Skill to Learn 2027 (interview) | Z8lf5oWKfj0 |
| 2 | 15 Oct 2026 | 22:24 | 76k | AI Agents Just Became Multiplayer. Here's How to Build Them. (Kylon, sponsored) | KZiF2J83zaY |
| 3 | 13 Oct 2026 | 14:59 | 173k | I Tested the Viral Reverse Engineer Anything Skill (github.com/morluto/rea) | rL5tw6h78zo |
| 4 | 12 Oct 2026 | 14:45 | 68k | This ONE Claude Skill Helps You Think Clearer Than 99% of People ("Roast Room" board of advisors) | nRXHWckVxoM |
| 5 | 11 Oct 2026 | 10:37 | 239k | I Tried 100+ Github Repos for Claude. These 6 Are the Best | HhZdNYI4pJs |
| 6 | 8 Oct 2026 | 9:11 | 122k | Grok Bot Just Got 2 Massive Upgrades. Do These Things Now. | MgvwZaDPCs4 |
| 7 | 8 Oct 2026 | 12:23 | 109k | Anthropic Engineers Just 10x'd Everyone's Claude Code (context engineering, /doctor) | oz2CwrPV2Rg |
| 8 | 5 Oct 2026 | 10:45 | 74k | I Built Another Andrej Karpathy Using Claude (expert clone from 700k words) | bvGptCLDhyo |
| 9 | 3 Oct 2026 | 34:34 | 81k | Master 96% of Codex in under 35 minutes | DFlELTiSPk8 |
| 10 | 2 Oct 2026 | 11:19 | 244k | Claude Code Mods Are Game Changers. Set Up These 5 NOW. | 9hetShMMp2s |

## What is in this folder

| File | Contents |
|------|----------|
| `videos.json`, `videos/NN.json` | Per video: title, date, duration, views, full description, chapter list with timestamps, cleaned resource links, guests, top ~40 comments (text, likes, replies, creator flag; commenter names removed). |
| `business-context.md` | Brief on Winstanley & Son's services, systems, workflows, constraints: the context the account-design agents need. |
| `repos.json` | The 13 public GitHub repos the videos link to (REA skill, Scroll Craft, Hyperframes, Google Workspace CLI, Apify MCP, Humanizer, Addy Osmani's agent-skills, Expo skills, Supabase agent-skills, Stripe AI skills, Playwright CLI, Anthropic claude-plugins-official, open-seo). Clone with `git clone --depth 1`. |
| `scripts/innertube_fetch.py` | Regenerates videos.json without an API key (works even where youtube.com is blocked). |
| `scripts/fetch_transcripts.py` | Fetches the transcripts (needs normal internet). Run this first locally. |
| `transcripts/` | Empty until fetch_transcripts.py has run. |

## Next steps for the local session

1. Fetch transcripts (see `transcripts/README.md`). Check the summary line: all 10 should succeed; video 1 and 9 are
   long and will be ~7k and ~5k words.
2. Run the 10-agent research phase (one agent per video, in parallel). Each agent reads `videos/NN.json` plus
   `transcripts/NN-<id>.md`, clones the repos the video links to if any, web-searches for third-party coverage, and
   writes `ai/videos/NN-<slug>.md` using the template below. Return structured JSON (key ideas, tools, patterns,
   role ideas, claims, confidence).
3. Verify each summary with a second agent (every claim traceable to transcript/description/comments/repo; no
   invented quotes; UK spelling), fix in place.
4. Synthesis (needs all 10): `ai/SYNTHESIS.md` with cross-video themes, Nate's current playbook (skills over prompts,
   context engineering, mods, multiplayer agents, expert clones, advisory councils, Codex vs Claude Code, tool
   landscape), and what a six-person optician should copy or ignore.
5. Design the account roster from the synthesis + `business-context.md`, then one agent per account writes
   `ai/accounts/<slug>.md` (template below). Likely roster: recall-and-reactivation, website-content, social-content,
   reviews, front-desk/bookings, data-hygiene, owner's advisory board ("roast room" style), plus a shared
   `ai/accounts/_shared/operating-rules.md` (GDPR, brand voice, secrets, approvals).
6. Write `ai/README.md`, `ai/videos/README.md` (index table), `ai/accounts/README.md` (roster + handoffs). Run a
   completeness critic over the whole `ai/` folder. Commit and push.

## Per-video template (`ai/videos/NN-slug.md`)

Title; channel, date, duration, views; URL; guests. Then: What the video covers (summary) / Chapter-by-chapter /
Key ideas and claims / Tools, products and repos mentioned (links) / How to apply it (steps, if a build) /
What viewers said (top comments: pushback, questions, confirmations) / Relevance to Winstanley & Son (3-6 bullets) /
Account or role ideas this video suggests / Sources used and confidence.

## Per-account template (`ai/accounts/slug.md`)

YAML frontmatter (name, description, tools, model) so the file drops into `.claude/agents/`. Then: Mission /
Responsibilities / Inputs and outputs / Systems it touches (GHL, VisionPMS, Make, Stannp, repo, social) / Skills it
needs (with the video or repo the idea came from) / System prompt / Guardrails (patient data, approvals, spend) /
Handoffs to other accounts and to humans / KPIs / Example tasks / Source videos.

## Notes

- Gavin is "Frame maker", never "optician". UK spelling. Plain English, no hype.
- This folder is inside a GitHub Pages site, so it is publicly readable once pushed (same as `tools/`). Keep patient data out.
- Comments in videos.json are public YouTube comments with author names stripped; they are context, not facts.

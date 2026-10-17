# AI accounts research

This folder holds research on the ten newest videos from the Nate Herk | AI Automation channel, published between 2 and 16 October 2026, and the roster of AI accounts that research produced for Winstanley & Son, a frame maker in Dingle, Liverpool.

The aim is practical. Each video was read for ideas the practice could use, tested against what is already running, and turned into either a recommendation or a defined role. Nothing here replaces a live system. Every account collects, checks, flags and drafts; the owner approves, signs and presses.

## How it was made

The work was done on 17 October 2026 in four stages.

1. One agent per video read the transcript, comments and any linked material, and wrote a summary. A second agent checked each summary against the source.
2. A synthesis pulled the ten summaries together: what the videos agree on, where they conflict, and which ideas suit a small practice.
3. A roster design turned the synthesis candidates into twelve accounts, merged overlaps, and set reporting lines and three build waves.
4. One writer per account produced its file, each checked against the shared operating rules.

## How to use an account file

Each file in `accounts/` is both a role brief and a working agent definition.

- To run it as an agent, copy the file into `.claude/agents/` in the project where it will work. The front matter sets the name, model and tools.
- To use it as a plain role brief, read it from the top: purpose, inputs, outputs, limits, and what it must never do.

Start with `accounts/README.md` for the roster at a glance, then read the shared rules in `accounts/_shared/operating-rules.md` before using any account. Every account inherits them.

## Folder map

| Path | What it holds |
|---|---|
| `research/nate-herk/` | Working material: business and estate context, the per-video template in `HANDOFF.md`, the video list, and fetch scripts |
| `videos/` | The ten video summaries, with an index in `videos/README.md` |
| `SYNTHESIS.md` | Cross-video synthesis, with candidate accounts in section 6 |
| `accounts/` | The roster, the shared operating rules and one file per account |

## What is deliberately absent

- Transcripts. Summaries paraphrase; they do not reproduce the videos.
- Internal reports and the owner's private notes. Where an account depends on one, its file says so without quoting it.
- Patient data of any kind, staff names, trading figures, prices, identifiers, webhook addresses and tokens.
- Anything that lets an account act without the owner. None of the accounts sends, posts, pays or changes a live system.

This is a public site, so those exclusions are part of the design, not an oversight.

## Adding new videos

Five older videos, numbered 11 to 15, are queued. To add them:

1. Run `fetch_transcripts.py` in `research/nate-herk/scripts/` to collect the transcripts and comments.
2. Write one summary per video using the template in `research/nate-herk/HANDOFF.md`, and have a second agent verify it.
3. Add the new rows to the table in `videos/README.md`.
4. Add an addendum to `SYNTHESIS.md` covering only what the new videos change.
5. Re-check the roster: does any video suggest a new account, a changed mission, or a reason to move an account between waves? Update `accounts/ROSTER.md` and the affected account files.

The summaries record auto-caption errors and the confidence of each claim. Keep doing that, and keep the rule that claims from a video are reported, not proven, until tested here.

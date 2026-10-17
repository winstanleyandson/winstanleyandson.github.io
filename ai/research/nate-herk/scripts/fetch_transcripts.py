#!/usr/bin/env python3
"""Download English transcripts for the videos listed in videos.json.

Run this on a machine with normal internet access (it needs www.youtube.com).
Requires: pip install youtube-transcript-api yt-dlp

Usage:
  python3 fetch_transcripts.py --meta ai/research/nate-herk/videos.json --out ai/research/nate-herk/transcripts

Writes, per video:  NN-<videoId>.json  (segments with start/duration/text)
                    NN-<videoId>.md    (readable transcript, one paragraph per ~45 seconds, with timestamps)
Tries youtube-transcript-api first (manual captions, then auto-generated), then falls back to
yt-dlp's auto-subtitles (json3). Prints a summary table and exits non-zero if any video has no transcript.
"""
import argparse, glob, json, os, re, shutil, subprocess, sys, tempfile

LANGS = ["en", "en-GB", "en-US"]


def via_transcript_api(video_id):
    from youtube_transcript_api import YouTubeTranscriptApi
    try:  # v1.x API
        api = YouTubeTranscriptApi()
        try:
            fetched = api.fetch(video_id, languages=LANGS)
        except Exception:
            tl = api.list(video_id)
            try:
                fetched = tl.find_manually_created_transcript(LANGS).fetch()
            except Exception:
                fetched = tl.find_generated_transcript(LANGS).fetch()
        return [{"start": s.start, "duration": s.duration, "text": s.text} for s in fetched], "youtube-transcript-api"
    except AttributeError:  # pre-1.0 API
        data = YouTubeTranscriptApi.get_transcript(video_id, languages=LANGS)
        return [{"start": d["start"], "duration": d["duration"], "text": d["text"]} for d in data], "youtube-transcript-api (legacy)"


def via_ytdlp(video_id):
    tmp = tempfile.mkdtemp(prefix="yt-subs-")
    try:
        cmd = ["yt-dlp", "--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", "en.*,en",
               "--sub-format", "json3", "-o", os.path.join(tmp, "%(id)s.%(ext)s"), f"https://www.youtube.com/watch?v={video_id}"]
        subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=300)
        files = sorted(glob.glob(os.path.join(tmp, "*.json3")))
        if not files:
            raise RuntimeError("yt-dlp produced no subtitle file")
        with open(files[0], encoding="utf-8") as f:
            data = json.load(f)
        segs = []
        for ev in data.get("events", []):
            text = "".join(s.get("utf8", "") for s in ev.get("segs", [])).replace("\n", " ").strip()
            if text:
                segs.append({"start": ev.get("tStartMs", 0) / 1000, "duration": ev.get("dDurationMs", 0) / 1000, "text": text})
        return segs, "yt-dlp auto-subs"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def stamp(sec):
    sec = int(sec)
    h, m, s = sec // 3600, (sec % 3600) // 60, sec % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def to_markdown(v, segs, source, para_seconds=45):
    out = [f"# Transcript: {v['title']}", "",
           f"- Video: {v['url']}", f"- Published: {v.get('published', '')} | Duration: {v.get('duration', '')}",
           f"- Source: {source} (auto-generated captions may contain recognition errors)", ""]
    para, para_start = [], None
    for s in segs:
        if para_start is None:
            para_start = s["start"]
        para.append(re.sub(r"\s+", " ", s["text"]).strip())
        if s["start"] - para_start >= para_seconds:
            out.append(f"**[{stamp(para_start)}]** " + " ".join(para))
            out.append("")
            para, para_start = [], None
    if para:
        out.append(f"**[{stamp(para_start)}]** " + " ".join(para))
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--only", help="comma-separated ranks to fetch, e.g. 1,2,3")
    a = ap.parse_args()
    with open(a.meta, encoding="utf-8") as f:
        videos = json.load(f)["videos"]
    only = {int(x) for x in a.only.split(",")} if a.only else None
    os.makedirs(a.out, exist_ok=True)
    failures = []
    for v in videos:
        if only and v["rank"] not in only:
            continue
        base = os.path.join(a.out, f"{v['rank']:02d}-{v['id']}")
        if os.path.exists(base + ".md"):
            print(f"{v['rank']:2d}. {v['id']} already fetched, skipping")
            continue
        segs, source, err = None, None, []
        for fn in (via_transcript_api, via_ytdlp):
            try:
                segs, source = fn(v["id"])
                if segs:
                    break
            except Exception as e:  # noqa: BLE001
                err.append(f"{fn.__name__}: {e.__class__.__name__}: {str(e)[:120]}")
        if not segs:
            failures.append(v["id"])
            print(f"{v['rank']:2d}. {v['id']} FAILED: " + " | ".join(err))
            continue
        with open(base + ".json", "w", encoding="utf-8") as f:
            json.dump({"id": v["id"], "title": v["title"], "source": source, "segments": segs}, f, ensure_ascii=False)
        with open(base + ".md", "w", encoding="utf-8") as f:
            f.write(to_markdown(v, segs, source))
        words = sum(len(s["text"].split()) for s in segs)
        print(f"{v['rank']:2d}. {v['id']} ok via {source}: {len(segs)} segments, ~{words} words -> {base}.md")
    if failures:
        print(f"\n{len(failures)} video(s) without transcript: {', '.join(failures)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Fetch a YouTube channel's latest long-form uploads plus per-video metadata, chapters,
description links and top comments, using YouTube's InnerTube API via youtubei.googleapis.com.

Works without an API key and without touching www.youtube.com (useful behind restrictive
proxies). It cannot fetch transcripts: use fetch_transcripts.py for that.

Usage:
  python3 innertube_fetch.py --handle @nateherk --count 10 --out ai/research/nate-herk
"""
import argparse, json, os, re, ssl, sys, urllib.error, urllib.parse, urllib.request

BASE = "https://youtubei.googleapis.com/youtubei/v1/"
KEY = "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"  # public key embedded in the YouTube web client
CLIENT = {"clientName": "WEB", "clientVersion": "2.20251001.00.00", "hl": "en", "gl": "US"}
CA = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE")
CTX = ssl.create_default_context(cafile=CA) if CA else ssl.create_default_context()


def post(endpoint, body):
    data = json.dumps({"context": {"client": CLIENT}, **body}).encode()
    req = urllib.request.Request(
        BASE + endpoint + "?key=" + KEY + "&prettyPrint=false", data=data,
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0",
                 "X-Youtube-Client-Name": "1", "X-Youtube-Client-Version": CLIENT["clientVersion"],
                 "Origin": "https://www.youtube.com"})
    with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
        return json.loads(r.read())


def walk(o, key, acc):
    if isinstance(o, dict):
        if key in o:
            acc.append(o[key])
        for v in o.values():
            walk(v, key, acc)
    elif isinstance(o, list):
        for v in o:
            walk(v, key, acc)
    return acc


def runs(o):
    o = o or {}
    return "".join(x.get("text", "") for x in o.get("runs", [])) or o.get("simpleText", "") or o.get("content", "")


def texts(o, acc):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "content" and isinstance(v, str):
                acc.append(v)
            else:
                texts(v, acc)
    elif isinstance(o, list):
        for v in o:
            texts(v, acc)
    return acc


def unwrap(u):
    if "youtube.com/redirect" in u:
        return urllib.parse.parse_qs(urllib.parse.urlparse(u).query).get("q", [u])[0]
    return u


TRACKING = ("googlevideo.com", "linkedin.com/in/", "instagram.com", "get.glaido.com", "hostinger.com",
            "smoothmedia", "skool.com", "aiautomationsociety.ai/optin", "x.com/nateherk")


def list_videos(handle, count):
    r = post("navigation/resolve_url", {"url": f"https://www.youtube.com/{handle}"})
    chan = walk(r, "browseId", [])[0]
    r = post("browse", {"browseId": chan, "params": "EgZ2aWRlb3PyBgQKAjoA"})  # Videos tab, latest first
    out = []
    for lv in walk(r, "lockupViewModel", []):
        vid = lv.get("contentId")
        if not vid:
            m = re.search(r"/vi/([A-Za-z0-9_-]{11})/", json.dumps(lv.get("contentImage", {})))
            vid = m.group(1) if m else None
        meta = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
        badges = walk(lv.get("contentImage", {}), "thumbnailBadgeViewModel", [])
        dur = next((b.get("text") for b in badges if re.match(r"^\d+:\d\d", b.get("text", ""))), "")
        rows = [x for x in texts(meta.get("metadata", {}), []) if x]
        out.append({"id": vid, "title": meta.get("title", {}).get("content", ""), "duration": dur, "meta_rows": rows})
        if len(out) >= count:
            break
    return chan, out


def video_details(v, max_comments):
    r = post("next", {"videoId": v["id"]})
    prim = (walk(r, "videoPrimaryInfoRenderer", []) or [{}])[0]
    v["published"] = runs(prim.get("dateText")) or runs(prim.get("relativeDateText"))
    v["views"] = runs(prim.get("viewCount", {}).get("videoViewCountRenderer", {}).get("viewCount"))
    desc, links = "", []
    for d in walk(r, "attributedDescriptionBodyText", []):
        desc = d.get("content", "") or desc
        for cr in d.get("commandRuns", []):
            for u in walk(cr, "url", []):
                u = unwrap(u)
                if u.startswith("http") and u not in links:
                    links.append(u)
    v["description"] = desc
    v["links"] = [u for u in links if not any(t in u for t in TRACKING)]
    chapters = []
    for ch in walk(r, "macroMarkersListItemRenderer", []):
        t, ts = runs(ch.get("title")), runs(ch.get("timeDescription"))
        if t and ts and {"title": t, "time": ts} not in chapters:
            chapters.append({"title": t, "time": ts})
    if not chapters:
        chapters = [{"title": m.group(2).strip(), "time": m.group(1)}
                    for m in re.finditer(r"(\d{1,2}:\d\d(?::\d\d)?)\s*[-–—:]?\s*(.+)", desc)]
    v["chapters"] = chapters
    v["guests"] = [m for m in v.pop("meta_rows", []) if " and " in m]
    token = None
    for sec in walk(r, "itemSectionRenderer", []):
        if sec.get("sectionIdentifier") == "comment-item-section":
            toks = walk(sec, "token", [])
            token = toks[0] if toks else None
    comments, pages = [], 0
    while token and pages < 2 and len(comments) < max_comments:
        cr = post("next", {"continuation": token})
        pages += 1
        for p in walk(cr, "commentEntityPayload", []):
            props, tb = p.get("properties", {}), p.get("toolbar", {})
            comments.append({"creator": bool(p.get("author", {}).get("isCreator")),
                             "likes": tb.get("likeCountNotliked", "") or tb.get("likeCountLiked", ""),
                             "replies": tb.get("replyCount", ""),
                             "text": props.get("content", {}).get("content", "")[:700],
                             "published": props.get("publishedTime", "")})
        nxt = None
        for c in walk(cr, "continuationItemRenderer", []):
            for t in walk(c, "token", []):
                if t and t != token:
                    nxt = t
        token = nxt
    seen, uniq = set(), []
    for c in comments:
        if c["text"] and c["text"] not in seen:
            seen.add(c["text"])
            uniq.append(c)
    uniq.sort(key=lambda c: int(re.sub(r"\D", "", str(c["likes"])) or 0), reverse=True)
    v["top_comments"] = uniq[:max_comments]
    return v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--handle", default="@nateherk")
    ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--max-comments", type=int, default=40)
    ap.add_argument("--out", required=True, help="output folder; writes videos.json and videos/NN.json")
    a = ap.parse_args()
    chan, videos = list_videos(a.handle, a.count)
    os.makedirs(os.path.join(a.out, "videos"), exist_ok=True)
    for i, v in enumerate(videos, 1):
        v["rank"] = i
        v["url"] = f"https://www.youtube.com/watch?v={v['id']}"
        video_details(v, a.max_comments)
        v["slug"] = f"{i:02d}-" + re.sub(r"[^a-z0-9]+", "-", v["title"].lower()).strip("-")[:60]
        with open(os.path.join(a.out, "videos", f"{i:02d}.json"), "w") as f:
            json.dump(v, f, indent=1, ensure_ascii=False)
        print(f"{i:2d}. {v['id']} | {v['published']:>13} | {v['duration']:>7} | {v['views']:>14} | {v['title']}", file=sys.stderr)
    with open(os.path.join(a.out, "videos.json"), "w") as f:
        json.dump({"channel_handle": a.handle, "channel_id": chan, "videos": videos}, f, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()

# Transcripts

Empty on purpose. The cloud session could not reach youtube.com (environment network policy), so
transcripts must be fetched from a machine with normal internet access:

```
python3 -m venv .venv && . .venv/bin/activate
pip install youtube-transcript-api yt-dlp
python3 ai/research/nate-herk/scripts/fetch_transcripts.py --meta ai/research/nate-herk/videos.json --out ai/research/nate-herk/transcripts
```

Each video gets `NN-<videoId>.md` (readable, timestamped paragraphs) and `NN-<videoId>.json` (raw segments).

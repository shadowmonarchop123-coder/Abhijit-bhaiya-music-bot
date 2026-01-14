import asyncio
import yt_dlp

PREFETCH = {}   # chat_id: data

ydl_opts = {
    "quiet": True,
    "no_warnings": True,
    "cookiefile": "cookies.txt",
    "skip_download": True,
    "nocheckcertificate": True,
    "geo_bypass": True,
    "format": "bestaudio/best",
    "extractor_args": {
        "youtube": {
            "player_client": ["android", "web"],
            "player_skip": ["configs", "webpage"]
        }
    }
}


def _pick_audio(info):
    formats = info.get("formats", [])

    # 1️⃣ first try: real audio only
    for f in formats:
        if f.get("acodec") != "none" and f.get("vcodec") == "none" and f.get("url"):
            return f["url"]

    # 2️⃣ fallback: any format with audio
    for f in formats:
        if f.get("acodec") != "none" and f.get("url"):
            return f["url"]

    return None


def _extract(query: str):
    if not query.startswith("http"):
        query = f"ytsearch1:{query}"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)

        if "entries" in info:
            info = info["entries"][0]

        audio_url = _pick_audio(info)
        if not audio_url:
            raise Exception("No playable audio stream found")

        return {
            "title": info.get("title", "Unknown"),
            "url": audio_url
        }


# ⚡ turbo extractor
async def extract_async(query: str):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _extract, query)


# 🔥 preload next song
async def prefetch(chat_id, query):
    loop = asyncio.get_event_loop()
    try:
        data = await loop.run_in_executor(None, _extract, query)
        PREFETCH[chat_id] = data
    except:
        PREFETCH.pop(chat_id, None)


def get_prefetch(chat_id):
    return PREFETCH.pop(chat_id, None)

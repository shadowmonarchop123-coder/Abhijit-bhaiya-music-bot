import asyncio
import yt_dlp

PREFETCH = {}   # chat_id: data

ydl_opts = {
    "quiet": True,
    "no_warnings": True,
    "cookiefile": "cookies.txt",
    "format": "bestaudio/best",
    "skip_download": True,
    "nocheckcertificate": True,
    "geo_bypass": True,
    "extractor_args": {
        "youtube": {
            "player_client": ["android"],
            "player_skip": ["configs"]
        }
    }
}


def _extract(query: str):
    # 🔥 direct ytsearch + extract (one hit only)
    if not query.startswith("http"):
        query = f"ytsearch1:{query}"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)

        if "entries" in info:
            info = info["entries"][0]

        return {
            "title": info.get("title", "Unknown"),
            "url": info["url"]
        }


# ⚡ TURBO main extractor (used in /play)
async def extract_async(query: str):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _extract, query)


# 🔥 BACKGROUND preload for next song
async def prefetch(chat_id, query):
    loop = asyncio.get_event_loop()
    try:
        data = await loop.run_in_executor(None, _extract, query)
        PREFETCH[chat_id] = data
    except:
        PREFETCH.pop(chat_id, None)


def get_prefetch(chat_id):
    return PREFETCH.pop(chat_id, None)

import asyncio
import yt_dlp

PREFETCH = {}

ydl_opts = {
    "quiet": True,
    "no_warnings": True,
    "cookiefile": "cookies.txt",
    "skip_download": True,
    "nocheckcertificate": True,
    "geo_bypass": True,
    "extractor_args": {
        "youtube": {
            "player_client": ["android", "web", "tv_embedded"],
            "player_skip": ["configs", "webpage"]
        }
    }
}

def _extract(query: str):
    if not query.startswith("http"):
        query = f"ytsearch1:{query}"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)

        if "entries" in info:
            info = info["entries"][0]

        # yt-dlp already gives best playable url here
        url = info.get("url")

        if not url:
            raise Exception("Stream URL not found")

        return {
            "title": info.get("title", "Unknown"),
            "url": url
        }

async def extract_async(query: str):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _extract, query)

async def prefetch(chat_id, query):
    loop = asyncio.get_event_loop()
    try:
        data = await loop.run_in_executor(None, _extract, query)
        PREFETCH[chat_id] = data
    except:
        PREFETCH.pop(chat_id, None)

def get_prefetch(chat_id):
    return PREFETCH.pop(chat_id, None)

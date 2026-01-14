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
    "geo_bypass": True
}

def _extract(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        if "entries" in info:
            info = info["entries"][0]

        return {
            "title": info.get("title", "Unknown"),
            "url": info["url"]
        }

async def prefetch(chat_id, link):
    loop = asyncio.get_event_loop()
    try:
        data = await loop.run_in_executor(None, _extract, link)
        PREFETCH[chat_id] = data
    except:
        PREFETCH.pop(chat_id, None)

def get_prefetch(chat_id):
    return PREFETCH.pop(chat_id, None)

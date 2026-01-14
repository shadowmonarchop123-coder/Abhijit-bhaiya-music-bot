import asyncio
import yt_dlp
import os

PREFETCH = {}

# Absolute path use karna behtar hota hai
COOKIE_FILE = os.path.join(os.getcwd(), "cookies.txt")

ydl_opts = {
    "format": "bestaudio/best",
    "quiet": True,
    "no_warnings": True,
    "cookiefile": COOKIE_FILE if os.path.exists(COOKIE_FILE) else None,
    "skip_download": True,
    "nocheckcertificate": True,
    "geo_bypass": True,
    "extractor_args": {
        "youtube": {
            "player_client": ["android", "ios", "web"],
            "player_skip": ["configs", "webpage"]
        }
    }
}

def _extract(query: str):
    if not query.startswith(("http://", "https://")):
        query = f"ytsearch1:{query}"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(query, download=False)
            if "entries" in info:
                info = info["entries"][0]

            # 1. Pehle direct url check karo
            url = info.get("url")
            
            # 2. Agar direct nahi hai, toh formats list me best audio dhoondo
            if not url or "manifest_url" in url:
                if "formats" in info:
                    # Filter only audio formats
                    audio_formats = [f for f in info['formats'] if f.get('vcodec') == 'none']
                    if audio_formats:
                        # Best quality audio format
                        url = audio_formats[-1]['url']

            if not url:
                raise Exception("Requested format is not available. Try updating cookies.")

            return {
                "title": info.get("title", "Unknown"),
                "url": url
            }
        except Exception as e:
            raise Exception(f"YouTube Error: {str(e)}")

async def extract_async(query: str):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _extract, query)

async def prefetch(chat_id, query):
    loop = asyncio.get_event_loop()
    try:
        data = await loop.run_in_executor(None, _extract, query)
        PREFETCH[chat_id] = data
    except Exception:
        PREFETCH.pop(chat_id, None)

def get_prefetch(chat_id):
    return PREFETCH.pop(chat_id, None)

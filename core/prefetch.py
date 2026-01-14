import asyncio
import yt_dlp

PREFETCH = {}

# Updated options with format and stable clients
ydl_opts = {
    "format": "bestaudio/best",
    "quiet": True,
    "no_warnings": True,
    "cookiefile": "cookies.txt",
    "skip_download": True,
    "nocheckcertificate": True,
    "geo_bypass": True,
    "extractor_args": {
        "youtube": {
            "player_client": ["android", "web"],
            "player_skip": ["configs", "webpage"]
        }
    },
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
}

def _extract(query: str):
    if not query.startswith(("http://", "https://")):
        query = f"ytsearch1:{query}"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(query, download=False)
            
            if "entries" in info:
                # Search results se pehla video uthayein
                info = info["entries"][0]

            # Direct URL nikalne ki koshish
            url = info.get("url")
            
            # Agar direct URL nahi milta (mostly YouTube issues), toh formats mein se best audio uthayein
            if not url and "formats" in info:
                for f in info['formats']:
                    if f.get('vcodec') == 'none' and f.get('ext') in ['m4a', 'webm']:
                        url = f.get('url')
                        break
            
            if not url:
                raise Exception("Stream URL not found")

            return {
                "title": info.get("title", "Unknown"),
                "url": url,
                "duration": info.get("duration", 0),
                "thumbnail": info.get("thumbnail", None)
            }
        except Exception as e:
            print(f"Extraction Error: {e}")
            raise e

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

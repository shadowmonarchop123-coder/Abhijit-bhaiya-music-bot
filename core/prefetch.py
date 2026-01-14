import asyncio
import yt_dlp

PREFETCH = {}

# Yahan 'format' specify karna zaruri hai taaki 'Requested format' wala error na aaye
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
            "player_client": ["android", "web"], # 'tv_embedded' hata diya hai kyunki wo fail ho raha hai
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

            # Direct URL nikalne ka logic
            url = info.get("url")
            
            # Agar direct URL nahi milta toh formats list se best audio uthayega
            if not url and "formats" in info:
                for f in info['formats']:
                    if f.get('vcodec') == 'none':
                        url = f.get('url')
                        break
            
            if not url:
                raise Exception("Stream URL not found")

            return {
                "title": info.get("title", "Unknown"),
                "url": url
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

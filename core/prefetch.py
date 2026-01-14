import asyncio
import yt_dlp
import os

PREFETCH = {}

# Cookies file path check
cookie_path = "cookies.txt"
if not os.path.exists(cookie_path):
    print("⚠️ WARNING: cookies.txt not found! YouTube might block you.")

ydl_opts = {
    "format": "bestaudio/best",
    "quiet": True,
    "no_warnings": True,
    "cookiefile": cookie_path if os.path.exists(cookie_path) else None,
    "skip_download": True,
    "nocheckcertificate": True,
    "geo_bypass": True,
    "extractor_args": {
        "youtube": {
            "player_client": ["ios", "web"], # iOS client sabse zyada stable hai abhi
            "player_skip": ["configs", "webpage"]
        }
    },
    "headers": {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
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

            # Sabse stable audio link extraction
            url = None
            if "formats" in info:
                for f in info['formats']:
                    # Sirf audio stream dhoondhna
                    if f.get('vcodec') == 'none' and f.get('acodec') != 'none':
                        url = f.get('url')
                        break
            
            if not url:
                url = info.get("url")

            if not url:
                raise Exception("YouTube ne link dene se mana kar diya. Please update cookies.txt")

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

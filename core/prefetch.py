import asyncio
import yt_dlp

PREFETCH = {}

# In options mein naye format aur clients add kiye hain jo block nahi hote
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
    }
}

def _extract(query: str):
    # Agar link nahi hai toh search karega
    if not query.startswith(("http://", "https://")):
        query = f"ytsearch1:{query}"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(query, download=False)
            if "entries" in info:
                info = info["entries"][0]

            # Direct link nikalne ki koshish
            url = info.get("url")
            
            # Agar direct link nahi hai, toh available formats se audio link dhundega
            if not url and "formats" in info:
                for f in info['formats']:
                    if f.get('vcodec') == 'none' and f.get('acodec') != 'none':
                        url = f.get('url')
                        break
            
            if not url:
                raise Exception("Koyi bhi audio stream format nahi mila.")

            return {
                "title": info.get("title", "Unknown"),
                "url": url
            }
        except Exception as e:
            # Error log karega taaki aapko terminal mein dikhe
            print(f"Extraction Error: {str(e)}")
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

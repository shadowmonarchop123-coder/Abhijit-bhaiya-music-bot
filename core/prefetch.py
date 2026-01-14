import asyncio
import yt_dlp

PREFETCH = {}

ydl_opts = {
    "format": "bestaudio/best",
    "quiet": True,
    "no_warnings": True,
    "cookiefile": "cookies.txt",
    "skip_download": True,
    "nocheckcertificate": True,
    "geo_bypass": True,
    # FFmpeg ki settings yahan add ki hain
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
    "ffmpeg_location": "/usr/bin/ffmpeg", # Linux server ka default path
    "extractor_args": {
        "youtube": {
            "player_client": ["android", "web"],
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

            # Sabse stable audio link nikalne ka logic
            url = None
            if "formats" in info:
                for f in info['formats']:
                    # Sirf audio stream dhoondhna (vcodec='none')
                    if f.get('vcodec') == 'none' and f.get('acodec') != 'none':
                        url = f.get('url')
                        break
            
            if not url:
                url = info.get("url")

            if not url:
                raise Exception("Koyi valid stream nahi mila. FFmpeg ya Cookies check karein.")

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

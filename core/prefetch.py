import yt_dlp

def turbo_extract(url: str):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "format": "bestaudio/best",
        "skip_download": True,
        "nocheckcertificate": True,
        "geo_bypass": True,
        "cookiefile": "cookies.txt",   # 🍪 MUST
        "socket_timeout": 8
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        if "entries" in info:
            info = info["entries"][0]

        for f in info.get("formats", []):
            if f.get("acodec") != "none" and f.get("url"):
                return {
                    "title": info.get("title", "Unknown"),
                    "url": f["url"]
                }

        return {
            "title": info.get("title", "Unknown"),
            "url": info["url"]
        }

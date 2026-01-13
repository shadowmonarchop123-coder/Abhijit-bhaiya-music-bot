import asyncio
from pyrogram import filters
from pyrogram.types import Message

from core.client import app
from core.call import call_py
from core.queues import add, get, is_empty, clear

from pytgcalls.types.input_stream import AudioPiped
from pytgcalls import StreamType
from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall

from youtubesearchpython import VideosSearch
import yt_dlp


# ---------------- FAST YT SEARCH ----------------
def yt_search(query: str):
    search = VideosSearch(query, limit=1)
    result = search.result()
    if not result["result"]:
        return None
    return result["result"][0]["link"]


# ---------------- ERROR-PROOF DIRECT STREAM ----------------
def yt_stream(url: str):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "cookiefile": "cookies.txt",
        "nocheckcertificate": True,
        "geo_bypass": True,
        "force-ipv4": True,
        "extract_flat": False,
        "extractor_args": {
            "youtube": {
                "player_client": ["android", "web", "tv_embedded"]
            }
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if "entries" in info:
            info = info["entries"][0]

        formats = info.get("formats", [])
        audio_url = None

        # first try: audio only
        for f in formats:
            if f.get("acodec") != "none" and f.get("vcodec") == "none":
                audio_url = f.get("url")
                if audio_url:
                    break

        # second try: any audio
        if not audio_url:
            for f in formats:
                if f.get("acodec") != "none":
                    audio_url = f.get("url")
                    if audio_url:
                        break

        # last fallback
        if not audio_url:
            audio_url = info.get("url")

        if not audio_url:
            raise Exception("No playable audio stream found.")

        return {
            "title": info.get("title", "Unknown"),
            "url": audio_url
        }


# ---------------- VC PLAYER ----------------
async def play_next(chat_id: int):
    if is_empty(chat_id):
        return

    song = get(chat_id)

    try:
        await call_py.join_group_call(
            chat_id,
            AudioPiped(song["url"]),
            stream_type=StreamType().pulse_stream
        )
    except Exception:
        await call_py.change_stream(
            chat_id,
            AudioPiped(song["url"])
        )


# ---------------- PLAY COMMAND ----------------
@app.on_message(filters.command(["play", "p"]) & filters.group)
async def play_cmd(_, message: Message):
    chat_id = message.chat.id

    if len(message.command) < 2:
        return await message.reply("❌ Usage: /play song name")

    query = message.text.split(None, 1)[1]
    m = await message.reply("⚡ Processing...")

    try:
        loop = asyncio.get_event_loop()

        if not query.startswith("http"):
            link = await loop.run_in_executor(None, yt_search, query)
            if not link:
                return await m.edit("❌ No results found.")
        else:
            link = query

        data = await loop.run_in_executor(None, yt_stream, link)

    except Exception as e:
        return await m.edit(f"❌ Stream error\n<code>{e}</code>")

    song = {
        "title": data["title"],
        "url": data["url"]
    }

    first_song = is_empty(chat_id)
    add(chat_id, song)

    if first_song:
        try:
            await play_next(chat_id)
            await m.edit(f"▶️ <b>Now Playing:</b> {data['title']}")
        except (GroupCallNotFound, NoActiveGroupCall):
            clear(chat_id)
            await m.edit("❌ Pehle voice chat start karo aur assistant add karo.")
    else:
        await m.edit(f"➕ <b>Queued:</b> {data['title']}")

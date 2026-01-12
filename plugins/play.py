from pyrogram import filters
from youtubesearchpython import VideosSearch
from core.client import app
from core.downloader import download_audio
from core.queues import add, get, is_empty
from core.streamer import start_stream
from core.call import call_py

@app.on_message(filters.command("play") & filters.group)
async def play(_, message):
    if len(message.command) < 2:
        return await message.reply("❌ Song name ya link do.")

    query = " ".join(message.command[1:])

    msg = await message.reply("🔎 Searching...")

    if not query.startswith("http"):
        search = VideosSearch(query, limit=1)
        result = (await search.next())["result"]
        if not result:
            return await msg.edit("❌ Song nahi mila.")
        url = result[0]["link"]
        title = result[0]["title"]
    else:
        url = query
        title = "Unknown"

    file_path, info = download_audio(url)

    data = {"title": title, "file": file_path}
    add(message.chat.id, data)

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0 or False:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(message.chat.id.__str__()) == 0:
        pass

    if len(messa

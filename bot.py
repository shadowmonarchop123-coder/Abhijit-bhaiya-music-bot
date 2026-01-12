import asyncio
from core.client import app, user
from core.call import call_py
from pyrogram import idle

async def main():
    await app.start()
    await user.start()
    await call_py.start()
    print("🎵 AO Music Bot Started Successfully!")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

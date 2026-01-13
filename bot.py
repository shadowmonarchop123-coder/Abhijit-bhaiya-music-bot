import asyncio
import glob
import logging
from core.client import app, user
from core.call import call_py
from pyrogram import idle

# 1. Logging Setup: Isse terminal mein har ek activity aur error show hoga
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("AO_Music")

# 🔥 AUTO LOAD ALL PLUGINS
for file in glob.glob("plugins/*.py"):
    try:
        __import__(file.replace("/", ".").replace(".py", ""))
        logger.info(f"Loaded plugin: {file}")
    except Exception as e:
        logger.error(f"Failed to load plugin {file}: {e}")

async def main():
    try:
        await app.start()
        logger.info("Bot Client Started")
        
        await user.start()
        logger.info("Assistant Client Started")
        
        await call_py.start() # 🔥 Assistant ko VC connection ke liye active karna
        logger.info("PyTgCalls Started")
        
        print("🎵 AO Music Bot Started Successfully!")
        await idle()
    except Exception as e:
        logger.error(f"Fatal Error during startup: {e}")
    finally:
        await app.stop()
        await user.stop()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

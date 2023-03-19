import logging
import os


from pyrogram import Client

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO)


API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
SESSION = os.environ.get("SESSION", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
OWNER_ID = os.environ.get("OWNER_ID", None)



print ("[Vexera]: Pyrogram Starting")

BOT = Client(
    name="Vexera",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Vexera"))


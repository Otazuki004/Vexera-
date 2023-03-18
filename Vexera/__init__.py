import logging
import os
import time


from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import MemorySession, StringSession

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

# bot =  [uptime,starttime,endtime]

StartTime = time.time()


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
#toon_linkz

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
SESSION = os.environ.get("SESSION", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
OWNER_ID = os.environ.get("OWNER_ID", None)



print ("[Vexera] Pyrogram Starting")
BOT = Client(
    "Vexera",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Vexera/modules"),
)
#bot
print ("[Vexera] UserBot Starting..")

UBOT = Client(session_string=SESSION, api_id=API_ID, api_hash=API_HASH, name="UBOT")
#userbot

print("[Vexera]: TELETHON CLIENT STARTING")
TBOT = TelegramClient(MemorySession(), API_ID, API_HASH)

#telethonbot

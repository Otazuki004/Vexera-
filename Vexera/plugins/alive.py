import time 
import random 
import asyncio
from pyrogram import filters, __version__ as pyrover
from Vexera import get_readable_time, StartTime
from Vexera import BOT as HS


load = "Lᴏᴀᴅɪɴɢ..."


@HS.on_message(filters.command("alive"))
async def alive(_, message):
    name = (await HS.get_me()).first_name
    otha = await HS.send_photo(message.chat.id, "https://telegra.ph/file/01bbb33d37c1f4f12c55e.jpg")
    await otha.edit_caption(load)
    await asyncio.sleep(3)
    await otha.edit_caption(f"""Hᴇʏ Usᴇʀ,\n ɪ ᴀᴍ ᴀʟɪᴠᴇ

★━━━━━━━━━━━━━━━━━★

» ᴍʏ Dᴇᴠʟᴏᴘᴇʀ : Oᴛᴀᴢᴜᴋɪ

» ᴘʏʀᴏɢʀᴀᴍ ᴠɪʀsᴏɴ : {pyrover}

» ᴏᴡɴᴇʀ : 𝗛ʏᴘᴇʀ 𝗦ᴘᴇᴇᴅ™

» ʀᴇᴘᴏ : [Here](http://github.com/Otazuki004/Vexera-)

★━━━━━━━━━━━━━━━━━★""")


@HS.on_message(filters.command("ping"))
async def ping(_, message):
     start_time = time.time()
     end_time = time.time()
     ping_time = round((end_time - start_time) * 1000, 3)
     uptime = get_readable_time((time.time() - StartTime))
     await HS.send_message(message.chat.id, f"👾 **System Uptime & Ping**\n=> 🔔 **Ping**: {ping_time}\n=> ⬆️ **Uptime**: {uptime}")


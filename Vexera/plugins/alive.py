import time 
import random 
import asyncio
from pyrogram import filters, __version__ as pyrover
from Vexera.__init__ import get_readable_time, StartTime
from Vexera.__init__ import BOT as HS


load = "Lᴏᴀᴅɪɴɢ..."


@HS.on_message(filters.command("alive"))
async def alive(_, message):
    name = (await HS.get_me()).first_name
    otha = await HS.send_photo(message.chat.id, "https://telegra.ph/file/01bbb33d37c1f4f12c55e.jpg")
    await otha.edit_caption(load)
    await asyncio.sleep(3)
    await otha.edit_caption(f"""Hᴇʏ Usᴇʀ, ɪ ᴀᴍ ᴀʟɪᴠᴇ

» **About Me**

» 𝐌ʏ 𝐃ᴇᴠʟᴏᴘᴇʀ : 𝐎ᴛᴀᴢᴜᴋɪ
» 𝐀ʙᴏᴜᴛ : A Pᴏᴡᴇʀғᴜʟʟ Tᴇʟᴇɢʀᴀᴍ ʙᴏᴛ Mᴀᴅᴇ Usɪɴɢ Pʏʀᴏɢʀᴀᴍ
» 𝐏ʏʀᴏɢʀᴀᴍ 𝐕ᴇʀsɪᴏɴ : 2.0.106
» 𝐎ᴡɴᴇʀ : 𝗛ʏᴘᴇʀ 𝗦ᴘᴇᴇᴅ™
» 𝐆ɪᴛʜᴜʙ Pᴀɢᴇ : https://Github.com/Otazuki004/
» 𝐑ᴇᴘᴏ : http://github.com/Otazuki004/Vexera-

- 𝗛ʏᴘᴇʀ 𝗦ᴘᴇᴇᴅ™""")


@HS.on_message(filters.command("ping"))
async def ping(_, message):
     start_time = time.time()
     end_time = time.time()
     ping_time = round((end_time - start_time) * 1000, 3)
     uptime = get_readable_time((time.time() - StartTime))
     await HS.send_message(message.chat.id, f"👾 **System Uptime & Ping**\n=> 🔔 **Ping**: {ping_time}\n=> ⬆️ **Uptime**: {uptime}")



from Vexera import TBOT as tbot
from Vexera.events import register
from telethon import Button

VV = "https://graph.org//file/3650014818cd34600f408.jpg"

@register(pattern=("/start"))
async def awake(event):
    START = f"""
────「 [Vexera] 」────
Hᴇʏ, {event.sender.first_name}.
I ᴀᴍ Vᴇxᴇʀᴀ I Hᴀᴠᴇ Cᴏᴏʟ Fᴇᴡᴛᴜʀᴇs
➖➖➖➖➖➖➖➖➖➖➖➖➖
[Pᴀᴛᴄʜ Uᴘᴅᴀᴛᴇ Dᴇᴛᴀɪʟs]
➖➖➖➖➖➖➖➖➖➖
Lᴀsᴛ Uᴘᴅᴀᴛᴇ : 18:3:23
Pᴀᴛᴄʜ Nᴀᴍᴇ : Bᴇᴛᴀ
➖➖➖➖➖➖➖➖➖➖➖➖➖
Nᴇxᴛ Pᴀᴛᴄʜ Dᴀᴛᴇ : 30:4:23
Nᴇxᴛ Pᴀᴛᴄʜ Nᴀᴍᴇ : Ultra

Try The Help Button To Lnow My Powers⚡
"""
    buttons = [
    [
        Button.url(
            text=f"[► Add Hydra To Your Group ◄]",
            url=f"https://telegram.dog/vexera_50_bot?startgroup=true",
        )
    ],
    [
        
        Button.url(
            text="𓆩𝗧ᴏᴏɴ 𝗟ɪɴᴋᴢ𓆪", url="https://telegram.dog/Toon_LinkZ"
        ),
    ],
    [
        Button.url(
            text="[► Support ◄]", url=f"https://telegram.dog/FutureCity005"
        ),
        Button.url(text="📢 Updates", url="https://telegram.dog/Updates004"),
    ],
]
    await tbot.send_file(event.chat_id, VV, caption=START, buttons=buttons)
    


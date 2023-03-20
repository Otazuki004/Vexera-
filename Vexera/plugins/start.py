from Vexera import BOT as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


START = f"""
────「 [Vexera](https://graph.org//file/3650014818cd34600f408.jpg) 」────
Hᴇʏ, User!!
I ᴀᴍ Vᴇxᴇʀᴀ I Hᴀᴠᴇ Cᴏᴏʟ Fᴇᴡᴛᴜʀᴇs
➖➖➖➖➖➖➖➖➖➖➖➖➖
[Pᴀᴛᴄʜ Uᴘᴅᴀᴛᴇ Dᴇᴛᴀɪʟs]
➖➖➖➖➖➖➖➖➖➖
Lᴀsᴛ Uᴘᴅᴀᴛᴇ : 18:3:23
Pᴀᴛᴄʜ Nᴀᴍᴇ : Bᴇᴛᴀ
➖➖➖➖➖➖➖➖➖➖➖➖➖
Nᴇxᴛ Pᴀᴛᴄʜ Dᴀᴛᴇ : 30:4:23
Nᴇxᴛ Pᴀᴛᴄʜ Nᴀᴍᴇ : Ultra

Send Help To know My Ultra Powers⚡
"""
buttons = [
    [
        InlineKeyboardButton(
            text=f"[► Add Vexera To Your Group ◄]",
            url=f"https://telegram.dog/Vexera_50_bot?startgroup=true",
        )
    ],
    [
        
        InlineKeyboardButton(
            text="𓆩𝗧ᴏᴏɴ 𝗟ɪɴᴋᴢ𓆪", url="https://telegram.dog/Toon_LinkZ"
        ),
    ],
    [
        InlineKeyboardButton(
            text="[► Support ◄]", url=f"https://telegram.dog/FutureCity005"
        ),
        InlineKeyboardButton(text="📢 Updates", url="https://telegram.dog/Updates004"),
    ],
]


@bot.on_message(filters.command("start") & filters.private)
def start(bot, message):
    text = START
    reply_markup = InlineKeyboardMarkup (buttons)
    message.reply(
    text=text,
    reply_markup=reply_markup,
    disable_web_page_preview=False
)

from pyrogram import filters
import random 
from Vexera import BOT as Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

STA1= f"""**
── 𝙑𝙚𝙭𝙚𝙧𝙖 ──

۞ I'ᴍ ᴀɴɪᴍᴇ ʙᴀsᴇᴅ Pᴏᴡᴇʀғᴜʟ Bᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ Tᴏᴏɴ LɪɴᴋZ.
۞ I'ᴍ Aʟᴡᴀʏs Wᴏʀᴋ & Uʟᴛʀᴀ Sᴘᴇᴇᴅ & Hᴇʟᴘ Tᴏ ᴍᴀɴɢᴇ Yᴏᴜʀ ɢʀᴏᴜᴘ ♡
۞ Usᴇ ɴᴏᴡ!
"""
PIC = (
 "https://telegra.ph/file/c4b5257049c672290306e.jpg", "https://telegra.ph/file/4135682365c0754618cf5.jpg", "https://telegra.ph/file/1dcfff90307b6f45de00e.jpg"

)

@Client.on_message(filters.command("start") & filters.group)
def start(bot, message):
	P = random.choice(PIC)
	Client.send_photo(message.chat.id, photo=P, caption=STA1, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("📚 Help", callback_data="help")]]
        ),
    )

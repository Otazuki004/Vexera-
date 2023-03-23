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
            [[InlineKeyboardButton("📚 Help", callback_data="ghelp")]]
        ),
    )
    
    
othaa = [
    [
InlineKeyboardButton("Back 🔙", 
callback_data="gsta"),
    ],
    [
        
InlineKeyboardButton("DEV COMMANDS", 
callback_data="gdhelp"),
    ],
    [
    
InlineKeyboardButton("ADMIN COMMANDS ", 
callback_data="admin"),
	],
]

@Client.on_callback_query(filters.regex("gdhelp"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**
♡︎𝗗𝗲𝘃 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀♡︎

/eval - To run A Code
/logs - Get A Bot Logs
/sh - To Install packages
**
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="ghelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("ghelp"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**
♡︎𝗛𝗲𝗹𝗽 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀♡︎

/id - Get a User Id/Chat ID💖
/tm - Reply a media To Get telegra.ph link
**
""",
        reply_markup=InlineKeyboardMarkup(othaa),
        )
        
@Client.on_callback_query(filters.regex("gsta"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(photo=P, caption=STA1, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("📚 Help", callback_data="ghelp")]]
        ),
    )
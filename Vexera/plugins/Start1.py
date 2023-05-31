from pyrogram import filters
from Vexera import BOT as Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

punda = [
    [
InlineKeyboardButton("DEV COMMANDS", 
callback_data="dhelp"),
    ],
    [
        
InlineKeyboardButton("ADMIN COMMANDS ", 
callback_data="adminp"),
    ],
]

@Client.on_callback_query(filters.regex("dhelp"))
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
            [[InlineKeyboardButton("🔙 Go Back", callback_data="help")]]
        ),
    )


@Client.on_callback_query(filters.regex("help"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**
♡︎𝗡𝗼𝗿𝗺𝗮𝗹 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀♡︎

/song - To Get what song you want 
/video - To Get What Video you Want 
/alive - To Check bot alive or not
/id - Get a User Id/Chat ID💖
/help - To Check a Bot Commands
/tm - Reply a media To Get telegra.ph link
/dice - Bot send you random dice
/ping - To Check Bot ping
/hack - To Hack Someone (JFF)
/love - To get A love Story (18+)
**
""",
        reply_markup=InlineKeyboardMarkup (punda),
    )

ADM = f"""**
/admins - To Get Admin list in your group 
/ban - Reply to ban Anyone (Admin)
/unban - Reply to Unban Anyone (Admin)
/pin - To Pin a any message (Admin)
/unpin - To unpin a any message (Admin)
/purge - Reply to any message To purge (Admin)
/del - To Delete a any message (admin)
/promote - To promote Anyone (Admin)
/setgtitle - To Change Group Title (Admin)
/setgpic - To Change Group pic (Admin)
"""

START = f"""**
────「 [Vexera](https://graph.org//file/3650014818cd34600f408.jpg) 」────
Hᴇʏ, User!!
I ᴀᴍ Vᴇxᴇʀᴀ I Hᴀᴠᴇ Cᴏᴏʟ Fᴇᴡᴛᴜʀᴇs
➖➖➖➖➖➖➖➖➖➖➖➖➖
[Pᴀᴛᴄʜ Uᴘᴅᴀᴛᴇ Dᴇᴛᴀɪʟs]
➖➖➖➖➖➖➖➖➖➖
Lᴀsᴛ Uᴘᴅᴀᴛᴇ : 31:5:23
Pᴀᴛᴄʜ Nᴀᴍᴇ : Project Admin (V-1.3)
➖➖➖➖➖➖➖➖➖➖➖➖➖
Nᴇxᴛ Pᴀᴛᴄʜ Dᴀᴛᴇ : 16:6:23
Nᴇxᴛ Pᴀᴛᴄʜ Nᴀᴍᴇ : Project VC (V-2)

Click Help To know My Ultra Powers⚡**
"""
buttons = [
    [
        InlineKeyboardButton(
            text=f"[► Add Vexera To Your Group ◄]",
            url=f"https://telegram.dog/Vexera_50_bot?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton("📚 Help 📚", 
callback_data="help"),
    ],
    [
        InlineKeyboardButton(
            text="[► Support ◄]", url=f"https://telegram.dog/FutureCity005"
        ),
        InlineKeyboardButton(text="📢 Updates", url="https://telegram.dog/Hyper_Speed0"),
    ],
]


@Client.on_message(filters.command("start") & filters.private)
def start(bot, message):
    text = START
    reply_markup = InlineKeyboardMarkup (buttons)
    message.reply(
    text=text,
    reply_markup=reply_markup,
    disable_web_page_preview=False
)

@Client.on_callback_query(filters.regex("adminp"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
    text = ADM,
    reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="help")]]
        ),
    )
        

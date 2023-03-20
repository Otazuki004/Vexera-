from pyrogram import filters
from Vexera import BOT as Bot


@Bot.on_message(filters.command("start") & filters.group)
async def start(_, message):
     await message.reply_text("Pyro Client is Alive!")

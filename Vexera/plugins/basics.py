from pyrogram import filters
from Vexera import Bot


@Bot.on_message(filters.command("start"))
async def start(_, message):
     await message.reply_text("Pyro Client is Alive!")

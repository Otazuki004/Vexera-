from Vexera import BOT as bot
from pyrogram.types import *
import os, io, time
from Vexera import badword as badd


@bot.on_message(filters.command("{badd}"))
async def delete(_, m):


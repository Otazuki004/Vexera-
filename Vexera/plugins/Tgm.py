import os
from Vexera import BOT as bot
from pyrogram import filters, Client
from telegraph import upload_file

@bot.on_message(filters.command(["tm", "pl", "tgm"]))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to Video or Image")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Oops! Not Supported bruh")
        return
    location1 = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(location1)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            f"""
**Yᴏᴜʀ Lɪɴᴋ👉 ' https://telegra.ph{response[0]} '♡︎♡︎♡︎

Jᴏɪɴ Us♡︎

𝐒𝐮𝐩𝐩𝐨𝐫𝐭 : @FutureCity005
𝐔𝐩𝐝𝐚𝐭𝐞𝐬 : @Hyper_Speed0
**
""",
            disable_web_page_preview=True,
        )
    finally:
        os.remove(location1)
#Toon_LinkZzzzz

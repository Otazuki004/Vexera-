from Vexera import BOT
from pyrogram import __version__ as uuu

PHOTO = "https://graph.org//file/44772fd4c942df289fb05.jpg"

START = f"""
────「 Vexera 」────
Hᴇʏ Usᴇʀs
Vᴇxᴇʀᴀ Տᴛᴀʀᴛᴇᴅ Տᴜᴄᴄᴇssғᴜʟʟʏ 
➖➖➖➖➖➖➖➖➖➖➖➖➖
❍ 𝗣ʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : {uuu}
➖➖➖➖➖➖➖➖➖➖➖➖➖
➛ Try Me I Have Cool Features 💖 ××
"""




if __name__ == "__main__":
    BOT.run()
    with BOT:
       BOT.send_message(-1001768984791, START)
        
 

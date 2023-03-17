from Vexera import BOT, UBOT, TBOT, BOT_TOKEN

if __name__ == "__main__":
    UBOT.start()
    BOT.run()
    with BOT:
        BOT.send_message("-1001768984791", "Pyrogram Client Started")
        
    TBOT.start(bot_token=BOT_TOKEN)
    TBOT.run()
    #start message 
    
    #ubot is Userbot
#tbot is Telethon client
#bot is pyrogram client 

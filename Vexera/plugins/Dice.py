from Vexera.__init__ import BOT as Client 
import random 
from pyrogram import filters

DICE = (
	"https://telegra.ph/file/8f9ed867773c4882abb8f.jpg", "https://telegra.ph/file/2bc88de446710c856fe05.jpg", "https://telegra.ph/file/34e4f49b488a2b1e53ac8.jpg", "https://telegra.ph/file/4bc13129792d67260bc66.jpg", "https://telegra.ph/file/32270be6809ee8e717703.jpg", "https://telegra.ph/file/f1959f34d7a0f8c428b07.jpg"

)


@Client.on_message(filters.command("dice"))
async def photo(bot, message):
	PH = random.choice(DICE)
	await Client.send_photo(message.chat.id, photo=PH, caption="Here is your Dice 🎲")

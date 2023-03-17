from Vexera import UBOT as Client 


@Client.on_message(filters.command(".start"))
async def fuck(_, message):
       if message.from_user.id == 1985665341:
             await Client.send_message(message.chat.id, "Oops i am still on devlopment")
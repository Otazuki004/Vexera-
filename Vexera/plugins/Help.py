from Vexera import TBOT
from Hydra.events import register

@register(pattern=("/help"))
async def awake(event):
  await event.reply("Oops i am still in devlopment")
import requests
from pyrogram import Client as Bot

from Bhadwa.config import API_HASH
from Bhadwa.config import API_ID
from Bhadwa.config import BG_IMAGE
from Bhadwa.config import BOT_TOKEN
from Bhadwa.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Bhadwa.modules"),
)

bot.start()
run()

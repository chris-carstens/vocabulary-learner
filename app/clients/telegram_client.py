import os
from telegram import Bot

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

class TelegramClient:
    def __init__(self):
        self.token = BOT_TOKEN
        self.bot = Bot(token=self.token)

    async def send_message(self, text):
        await self.bot.send_message(chat_id=CHANNEL_ID, text=text)

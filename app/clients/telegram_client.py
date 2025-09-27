from telegram import Bot
from app.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID

class TelegramClient:
    def __init__(self):
        self.token = TELEGRAM_BOT_TOKEN
        self.bot = Bot(token=self.token)

    async def send_message(self, text):
        await self.bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=text)

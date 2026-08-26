import os
import asyncio
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

MESSAGE = """🔔 NHẮC NHỞ

Mọi người chú ý kiểm tra công việc nhé!"""

async def main():
    bot = Bot(token=TOKEN)

    while True:
        await bot.send_message(
            chat_id=CHAT_ID,
            text=MESSAGE
        )

        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())

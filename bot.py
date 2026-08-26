import asyncio
import os
from telegram import Bot

TOKEN = "8819201392:AAHJxmFT4ybbqIXsxDym8IZQ9Q7iwBg7_yo"
CHAT_ID = -5234645026

MESSAGE = """🔔 NHẮC NHỞ @all

CHECK LINK MỌI NGƯỜI ƠI"""


async def main():
    bot = Bot(token=TOKEN)
    # Khởi tạo session cho bot
    async with bot:
        while True:
            await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)
            await asyncio.sleep(3600)  # Chờ 1 tiếng (3600 giây)


if __name__ == "__main__":
    asyncio.run(main())

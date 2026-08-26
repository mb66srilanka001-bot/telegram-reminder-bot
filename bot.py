import asyncio
from datetime import datetime, timedelta
from telegram import Bot

TOKEN = "8819201392:AAHJxmFT4ybbqIXsxDym8IZQ9Q7iwBg7_yo"
CHAT_ID = -5423366197

MESSAGE = """🔔 NHẮC NHỞ @all

CHECK LINK MỌI NGƯỜI ƠI"""


async def main():
    bot = Bot(token=TOKEN)
    async with bot:
        while True:
            now = datetime.now()
            # Tính thời gian đến đầu giờ tiếp theo (:00 phút)
            next_hour = (now + timedelta(hours=1)).replace(
                minute=0, second=0, microsecond=0
            )
            wait_seconds = (next_hour - now).total_seconds()

            # Chờ đúng đến phút :00 của giờ sau
            await asyncio.sleep(wait_seconds)

            # Gửi tin nhắn nhắc nhở đúng đầu giờ
            await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)


if __name__ == "__main__":
    asyncio.run(main())

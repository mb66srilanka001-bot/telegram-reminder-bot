import asyncio
from datetime import datetime, timedelta
import zoneinfo
from telegram import Bot

TOKEN = "8819201392:AAHJxmFT4ybbqIXsxDym8IZQ9Q7iwBg7_yo"
CHAT_ID = -5423366197

MESSAGE = """🔔 NHẮC NHỞ @ivyy_mb @Postmb66 @Emiemoi @yumim_b6 @jayramb66 @lussiambb @eira_day_ne @cloo_ii

CHECK LINK MỌI NGƯỜI ƠI"""


async def main():
    bot = Bot(token=TOKEN)
    tz = zoneinfo.ZoneInfo("Asia/Ho_Chi_Minh")  # Cố định giờ GMT+7

    async with bot:
        while True:
            now = datetime.now(tz)
            # Tính thời gian tới đúng phút :00 của giờ tiếp theo theo giờ GMT+7
            next_hour = (now + timedelta(hours=1)).replace(
                minute=0, second=0, microsecond=0
            )
            wait_seconds = (next_hour - now).total_seconds()

            # Chờ đến đúng 00 phút giờ GMT+7
            await asyncio.sleep(wait_seconds)

            # Gửi tin nhắn đúng đầu giờ
            await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)


if __name__ == "__main__":
    asyncio.run(main())

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
    tz = zoneinfo.ZoneInfo("Asia/Ho_Chi_Minh")

    async with bot:
        # Gửi ngay 1 tin test ban đầu
        await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)

        while True:
            now = datetime.now(tz)
            # Xác định mốc phút 30 tiếp theo chuẩn xác
            target = now.replace(minute=30, second=0, microsecond=0)
            if now >= target:
                target += timedelta(hours=1)

            wait_seconds = (target - now).total_seconds()
            await asyncio.sleep(wait_seconds)
            await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)


if __name__ == "__main__":
    asyncio.run(main())

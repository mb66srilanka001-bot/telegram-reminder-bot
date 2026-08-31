import asyncio
from datetime import datetime
import zoneinfo
from telegram import Bot

TOKEN = "8819201392:AAHJxmFT4ybbqIXsxDym8IZQ9Q7iwBg7_yo"
CHAT_ID = -5423366197

# Định nghĩa nội dung thông báo cho từng khung giờ
SCHEDULE = {
    # Nhóm 1: 09:30, 11:30, 14:30
    ("09:15", "11:15", "14:15"): "check link đi mấy ní @ivyy_mb @jayramb66 @lussiambb",
    
    # Nhóm 2: 16:30, 20:30, 21:30, 23:30
    ("16:15", "20:15", "21:15", "23:15"): "check link đi mấy ní @Emiemoi @DL_MB66 @yumim_b6",
    
    # Nhóm 3: 00:30, 03:30, 06:30
    ("00:15", "03:15", "06:15"): "check link đi mấy ní @cloo_ii",
    
    # Nhóm 4: 02:30, 05:30
    ("02:15", "05:15"): "check link đi mấy ní @eira_day_ne",
    
    # Nhóm 5: 01:30, 04:30
    ("01:15", "04:15"): "check link đi mấy ní @cskh_chiko"
    
}

async def main():
    bot = Bot(token=TOKEN)
    tz = zoneinfo.ZoneInfo("Asia/Ho_Chi_Minh")  # Cố định giờ Việt Nam (GMT+7)

    async with bot:
        while True:
            now = datetime.now(tz)
            current_time = now.strftime("%H:%M")

            # Kiểm tra xem giờ hiện tại có trùng với khung giờ hẹn không
            for times, message in SCHEDULE.items():
                if current_time in times:
                    await bot.send_message(chat_id=CHAT_ID, text=message)
                    # Sau khi gửi xong, chờ 60s để tránh gửi trùng lặp trong cùng 1 phút
                    await asyncio.sleep(60)
                    break
            
            # Vòng lặp kiểm tra lại sau mỗi 10 giây
            await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())

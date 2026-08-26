CHECK LINK MỌI NGƯỜI ƠI"""


async def main():
    bot = Bot(token=TOKEN)
    async with bot:
        # Gửi ngay 1 tin nhắn để kiểm tra bot có hoạt động trong nhóm không
        await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)

        # Vòng lặp duy trì bot luôn chạy và nhắc đúng đầu giờ (:00)
        while True:
            now = datetime.now()
            next_hour = (now + timedelta(hours=1)).replace(
                minute=0, second=0, microsecond=0
            )
            wait_seconds = (next_hour - now).total_seconds()

            # Chờ tới đúng phút :00 của giờ tiếp theo
            await asyncio.sleep(wait_seconds)
            await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from aiogram import Bot

BOT_TOKEN = "8572041803:AAHLyAMDLTqQqHriai8Z_d1k82z9RKo0zwo"
CHANNEL_ID = "@zerikma_filmlar"
USER_ID = 1142512399 # this seems to be user's telegram id based on previous errors/tests
MESSAGE_ID = 223

async def main():
    bot = Bot(token=BOT_TOKEN)
    try:
        # First test if bot can read from channel at all
        chat = await bot.get_chat(CHANNEL_ID)
        print(f"Botingiz u kanalda bormi? -> Ha, kanal nomi: {chat.title}")
        
    except Exception as e:
        print(f"Kanalni o'qib bo'lmadi: {e}")
        return

    try:
        # Test copy message
        await bot.copy_message(
            chat_id=USER_ID,
            from_chat_id=CHANNEL_ID,
            message_id=MESSAGE_ID,
            caption="Test movie"
        )
        print("Xabar muvaffaqiyatli yuborildi!")
    except Exception as e:
        print(f"Xabarni ko'chirishda xato: {e}")

if __name__ == "__main__":
    asyncio.run(main())


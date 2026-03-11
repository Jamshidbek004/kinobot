import asyncio
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from aiogram import Bot
from bot_app.models import Movie
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

async def main():
    bot = Bot(token=BOT_TOKEN)
    m = Movie.objects.get(code=12)
    print(f"Bazada 12 kodli kino: {m.title}")
    print(f"Uning kanaldagi IDsi (message_id): {m.message_id}")
    print(f"Kanal usernamesi (.env da): {CHANNEL_ID}")

    try:
        # Check if bot can get chat info (needs no rights, just to be public)
        chat = await bot.get_chat(CHANNEL_ID)
        print(f"Kanal topildi: {chat.title} ({chat.id})")
        
        # Check bot's status in the chat
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=bot.id)
        print(f"Botning kanaldagi maqomi: {member.status}")
        if member.status != 'administrator':
            print("DIQQAT: Bot administrator emas!")
            
    except Exception as e:
        print(f"Kanal ma'lumotlarini olishda xato: {e}")

    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())

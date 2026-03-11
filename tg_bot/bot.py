import os
import sys
import django
import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# Load env variables
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Import handlers after django setup
from tg_bot.handlers import router

async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

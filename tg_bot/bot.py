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

from aiogram.client.session.aiohttp import AiohttpSession

# Initialize bot and dispatcher
session = AiohttpSession(proxy="http://proxy.server:3128")
bot = Bot(token=BOT_TOKEN, session=session)
dp = Dispatcher()

# Import handlers after django setup
from tg_bot.handlers import router

# Setup dispatcher unconditionally for the webhook
dp.include_router(router)

# We no longer need the polling main() function here, 
# as Django will handle incoming requests via the webhook.

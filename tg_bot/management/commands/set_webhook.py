import os
import asyncio
from django.core.management.base import BaseCommand
from aiogram import Bot
from dotenv import load_dotenv

class Command(BaseCommand):
    help = 'Sets the Telegram Webhook URL'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='The webhook URL (e.g., https://kinobot2026.pythonanywhere.com/webhook/)')

    def handle(self, *args, **kwargs):
        webhook_url = kwargs['url']
        
        load_dotenv()
        bot_token = os.getenv('BOT_TOKEN')
        
        if not bot_token:
            self.stdout.write(self.style.ERROR('BOT_TOKEN not found in .env file'))
            return
            
        bot = Bot(token=bot_token)
        
        async def set_webhook():
            # Drop pending updates to avoid processing old messages
            await bot.delete_webhook(drop_pending_updates=True)
            # Set the new webhook
            result = await bot.set_webhook(url=webhook_url)
            await bot.session.close()
            return result
            
        self.stdout.write(self.style.WARNING(f'Setting webhook to: {webhook_url}...'))
        
        result = asyncio.run(set_webhook())
        
        if result:
            self.stdout.write(self.style.SUCCESS('Successfully set webhook!'))
        else:
            self.stdout.write(self.style.ERROR('Failed to set webhook.'))

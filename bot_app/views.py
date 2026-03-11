from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from aiogram.types import Update
from tg_bot.bot import bot, dp

@csrf_exempt
async def telegram_webhook(request):
    if request.method == 'POST':
        try:
            # Re-import dispatcher router to ensure it's loaded
            from tg_bot.handlers import router
            
            # Setup dispatcher if it's not setup yet
            try:
                dp.include_router(router)
            except ValueError:
                pass
                
            json_str = request.body.decode('UTF-8')
            update_data = json.loads(json_str)
            update = Update(**update_data)
            
            # Process update via dispatcher asynchronously
            await dp.feed_update(bot=bot, update=update)
            
        except Exception as e:
            print(f"Webhook Error: {e}")
            
    return JsonResponse({"status": "ok"})

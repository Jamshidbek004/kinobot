from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from aiogram.types import Update
from tg_bot.bot import bot, dp

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        try:
            # Re-import dispatcher router to ensure it's loaded
            from tg_bot.handlers import router
            from asgiref.sync import async_to_sync
            
            # Setup dispatcher if it's not setup yet
            try:
                dp.include_router(router)
            except ValueError:
                pass
                
            json_str = request.body.decode('UTF-8')
            update_data = json.loads(json_str)
            update = Update(**update_data)
            
            # Process update via dispatcher synchronously for WSGI
            async_to_sync(dp.feed_update)(bot=bot, update=update)
            
        except Exception as e:
            import traceback
            error_msg = traceback.format_exc()
            print(f"Webhook Error: {e}")
            return JsonResponse({"status": "error", "message": str(e), "traceback": error_msg})
            
    return JsonResponse({"status": "ok"})

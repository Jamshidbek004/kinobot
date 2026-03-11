from django.contrib import admin
from .models import User, Movie, Task, Transaction

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'username', 'coins', 'referrer', 'last_bonus_date')
    search_fields = ('telegram_id', 'username')
    list_filter = ('last_bonus_date',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'movie_link', 'views', 'created_at')
    search_fields = ('code', 'title', 'movie_link')
    list_filter = ('created_at',)
    exclude = ('message_id',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform', 'reward', 'is_active')
    list_filter = ('platform', 'is_active')
    search_fields = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'type', 'created_at')
    list_filter = ('type', 'created_at')
    search_fields = ('user__telegram_id', 'user__username')

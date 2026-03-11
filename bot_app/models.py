from django.db import models

class User(models.Model):
    telegram_id = models.BigIntegerField(unique=True, verbose_name="Telegram ID")
    username = models.CharField(max_length=255, null=True, blank=True, verbose_name="Username")
    coins = models.IntegerField(default=0, verbose_name="Tangalar")
    referrer = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals', verbose_name="Taklif qilgan")
    last_bonus_date = models.DateField(null=True, blank=True, verbose_name="Oxirgi bonus sanasi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")

    def __str__(self):
        return f"{self.telegram_id} - {self.username or 'No Username'}"

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"


class Movie(models.Model):
    code = models.IntegerField(unique=True, verbose_name="Kino Kodi")
    title = models.CharField(max_length=255, verbose_name="Kino Nomi")
    movie_link = models.URLField(
        verbose_name="Kanal xabari havolasi (Link)",
        help_text="Masalan: https://t.me/zerikma_filmlar/223",
        default="https://t.me/zerikma_filmlar/"
    )
    message_id = models.IntegerField(verbose_name="Xabar ID (Kanalda)", null=True, blank=True, help_text="Avtomatik to'ldiriladi")
    channel_id = models.BigIntegerField(null=True, blank=True, verbose_name="Kanal ID (Agar alohida bo'lsa)")
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")

    def save(self, *args, **kwargs):
        if self.movie_link:
            try:
                # Extracts the last integer part of the telegram url (e.g. 223 from https://t.me/kanal/223)
                self.message_id = int(self.movie_link.strip('/').split('/')[-1])
            except ValueError:
                pass
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.title}"

    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kinolar"


class Task(models.Model):
    PLATFORM_CHOICES = [
        ('telegram', 'Telegram'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('other', 'Boshqa'),
    ]
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, default='telegram', verbose_name="Platforma")
    name = models.CharField(max_length=255, verbose_name="Vazifa nomi")
    url = models.URLField(verbose_name="Havola (URL)")
    chat_id = models.CharField(max_length=255, null=True, blank=True, help_text="Telegram obunani tekshirish uchun kanal username yoki ID (Masalan: @kanal_nomi yoki -100...)", verbose_name="Kanal ID/Username")
    reward = models.IntegerField(default=1, verbose_name="Mukofot (Tanga)")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    def __str__(self):
        return f"{self.name} (+{self.reward})"

    class Meta:
        verbose_name = "Vazifa"
        verbose_name_plural = "Vazifalar"


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('earn', 'Yig\'ildi (Vazifa)'),
        ('spend', 'Saruflandi (Kino)'),
        ('buy', 'Sotib olindi'),
        ('bonus', 'Bonus'),
        ('referral', 'Referal'),
        ('admin', 'Admin tomonidan'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions', verbose_name="Foydalanuvchi")
    amount = models.IntegerField(verbose_name="Miqdor")
    type = models.CharField(max_length=50, choices=TRANSACTION_TYPES, verbose_name="Turi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Sana")

    def __str__(self):
        return f"{self.user.telegram_id} - {self.amount} ({self.get_type_display()})"

    class Meta:
        verbose_name = "Tranzaksiya"
        verbose_name_plural = "Tranzaksiyalar"

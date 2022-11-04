from django.db import models
from django.conf import settings
# from phone_field import PhoneField

class Telegram(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # phone_number = PhoneField(blank=True, help_text='Telegram phone number') # for 2fa in the future
    session_token = models.TextField(default=False)
    class Meta:
        db_table = 'telegram_tokens'

    def __str__(self):
        return f"User {self.user}"

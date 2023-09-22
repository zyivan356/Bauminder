from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, verbose_name='Аватар')
    bio = models.TextField(blank=True, verbose_name='О себе')
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='Возраст')
    GENDER_CHOICES = (
        ('М', 'Студент'),
        ('Ж', 'Студентка'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    tag = models.CharField(max_length=16, blank=True, verbose_name='Тег в телеграмме')
class Like(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes_sent', on_delete=models.CASCADE, null=True, blank=True)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes_received', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.from_user} лайкнул {self.to_user}"


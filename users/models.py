from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Модель пользователя с авторизацией по email"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователей'

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователя с авторизацией по email"""
    pass

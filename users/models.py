from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoles(models.TextChoices):
    """Роли пользователя:
    member - может просматривать обучающие материалы, но не может удалять или изменять что-либо кроме своего профиля
    moderator - может просматривать, удалять или изменять любые обучающие материалы кроме профиля пользователя
    """
    MEMBER = 'member'
    MODERATOR = 'moderator'


class User(AbstractUser):
    """Модель пользователя с авторизацией по email"""
    role = models.CharField(max_length=15, verbose_name='роль',
                            choices=UserRoles.choices, default=UserRoles.MEMBER)

    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

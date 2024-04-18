from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели пользователя"""

    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра профиля пользователя,
       включает поле успешно пройденных тестов"""
    completed_tests = ...

    class Meta:
        model = User
        exclude = ['password']


class UserListSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра списка пользователей"""

    class Meta:
        model = User
        fields = ('id', 'email', 'role')
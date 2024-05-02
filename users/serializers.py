from rest_framework import serializers

from materials.serializers import PassedTestingSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели пользователя"""

    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра профиля пользователя,
       включает поле успешно пройденных тестов"""
    completed_tests = PassedTestingSerializer(source='passedtesting_set', many=True)

    class Meta:
        model = User
        fields = ('email', 'role', 'last_login', 'completed_tests')


class UserListSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра списка пользователей"""

    class Meta:
        model = User
        fields = ('id', 'email', 'role')

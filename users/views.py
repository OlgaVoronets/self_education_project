from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from users.models import User
from users.permissions import IsModerator, IsOwner
from users.serializers import UserSerializer, UserDetailSerializer, UserListSerializer


class UserCreateView(generics.CreateAPIView):
    """Регистрация нового пользователя, доступна для всех"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """Переопределение метода для сохранения хешированного пароля в бд (если пароль не хешируется -
        пользователь не считается активным и токен авторизации не создается)"""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserDetailView(generics.RetrieveAPIView):
    """Просмотр профиля пользователя, доступно авторизованным пользователям"""
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


class UserUpdateView(generics.UpdateAPIView):
    """Редактирование профиля пользователя, доступно только пользователю"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwner]


class UserDeleteView(generics.DestroyAPIView):
    """Удаление профиля пользователя, доступно только пользователю"""
    queryset = User.objects.all()
    permission_classes = [IsOwner]


class UserListView(generics.ListAPIView):
    """Просмотр списка зарегистрированных пользователей, доступно администраторам платформы"""
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [IsModerator]

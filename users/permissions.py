from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = "Доступно модераторам"

    def has_permission(self, request, view):
        return request.user.role == UserRoles.MODERATOR


class IsOwner(BasePermission):
    """Проверка для объекта ответа на тестовое задание"""
    message = "Доступно владельцу"

    def has_object_permission(self, request, view, obj):
        return request.user.email == obj.email

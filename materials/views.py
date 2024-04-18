from rest_framework import generics

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, CourseDetailSerializer, LessonSerializer, LessonDetailSerializer
from users.permissions import IsModerator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


"""CRUD для модели курса"""


class CourseCreateView(generics.CreateAPIView):
    """Контроллер создания курса, доступно администраторам платформы"""
    serializer_class = CourseSerializer
    permission_classes = [IsModerator]


class CourseDetailView(generics.RetrieveAPIView):
    """Контроллер просмотра курса, доступно авторизованным пользователям платформы"""
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()


class CourseUpdateView(generics.UpdateAPIView):
    """Контроллер редактирования курса, доступно администраторам платформы"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsModerator]


class CourseDeleteView(generics.DestroyAPIView):
    """Контроллер удаления курса, доступно администраторам платформы"""
    queryset = Course.objects.all()
    permission_classes = [IsModerator]


class CourseListView(generics.ListAPIView):
    """Контроллер для просмотра списка курсов, доступно авторизованным пользователям"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsModerator]


"""CRUD для модели урока"""


class LessonCreateView(generics.CreateAPIView):
    """Контроллер создания урока, доступно администраторам платформы"""
    serializer_class = LessonSerializer
    permission_classes = [IsModerator]


class LessonDetailView(generics.RetrieveAPIView):
    """Контроллер просмотра урока, доступно авторизованным пользователям платформы"""
    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(generics.UpdateAPIView):
    """Контроллер редактирования урока, доступно администраторам платформы"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]


class LessonDeleteView(generics.DestroyAPIView):
    """Контроллер удаления урока, доступно администраторам платформы"""
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]


class LessonListView(generics.ListAPIView):
    """Контроллер для просмотра списка курсов, доступно авторизованным пользователям"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course',)
    ordering_fields = ('title',)

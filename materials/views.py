
from rest_framework import generics
from rest_framework.views import APIView

from materials.models import Course, Lesson, Testing, Answer
from materials.serializers import CourseSerializer, CourseDetailSerializer, LessonSerializer, LessonDetailSerializer, \
    TestingSerializer, TestingDetailSerializer, AnswerSerializer, LessonTestingSerializer
from materials.services import testing_func
from users.permissions import IsModerator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response


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


"""CRUD для модели тестирования"""


class TestingListCreateView(generics.ListCreateAPIView):
    """Контроллер для создания и просмотра списка тестовых заданий, доступно администраторам платформы
    метод POST выполняет создание экземпляра
    метод GET выводит список экземпляров"""
    serializer_class = TestingSerializer
    queryset = Testing.objects.all()
    permission_classes = [IsModerator]


class TestingDetailDeleteView(generics.RetrieveDestroyAPIView):
    """Контроллер для просмотра и удаления тестового задания, доступно администраторам платформы
        метод DELETE выполняет удаление экземпляра
        метод GET выводит экземпляр для просмотра"""
    serializer_class = TestingDetailSerializer
    queryset = Testing.objects.all()
    permission_classes = [IsModerator]


"""CRUD для модели ответа"""


class AnswerListCreateView(generics.ListCreateAPIView):
    """Контроллер для создания и просмотра списка ответов, доступно администраторам платформы
    метод POST выполняет создание экземпляра
    метод GET выводит список экземпляров"""
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('testing',)
    ordering_fields = ('id',)
    permission_classes = [IsModerator]


class AnswerDetailDeleteView(generics.RetrieveDestroyAPIView):
    """Контроллер для просмотра и удаления ответа, доступно администраторам платформы
        метод DELETE выполняет удаление экземпляра
        метод GET выводит экземпляр для просмотра"""
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [IsModerator]


"""Тестовое задание"""


class LessonTestingView(APIView):
    """Контроллер прохождения тестового задания
       в запросе передаем id урока """
    serializer_class = LessonTestingSerializer
    def post(self, pk):
        lesson = Lesson.objects.get(pk=pk)  #  тут мне надо вернуть json для фронтенда, получить от пользователя ответ и дать обратную связь

# class LessonTestingView(generics.CreateAPIView):
#     """Контроллер прохождения тестового задания
#        в запросе передаем id урока """
#     serializer_class = LessonTestingSerializer
#
#     def post(self, request, pk):
#         lesson = Lesson.objects.get(id=pk)
#
#         return self.create(request)


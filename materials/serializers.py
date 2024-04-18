from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from materials.models import Course, Lesson, Testing, Answer


class CourseSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели курса"""

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели урока"""

    class Meta:
        model = Lesson
        fields = '__all__'


class TestingSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели тестирования"""

    class Meta:
        model = Testing
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели ответа"""
    class Meta:
        model = Answer
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра информации о курсе, включает в себя
    список уроков этого курса"""
    lessons_list = SerializerMethodField()

    @staticmethod
    def get_lessons_list(course):
        """Получаем список уроков для данного курса"""
        return LessonSerializer(Lesson.objects.filter(course=course),
                                many=True).data

    class Meta:
        model = Course
        fields = '__all__'


class LessonDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра информации об уроке,
       где для курса выводится его наименование"""
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'


class TestingDetailSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра информации о тестовом задании, включает в себя
    список ответов на тест"""
    answers_list = SerializerMethodField()

    @staticmethod
    def get_answers_list(testing):
        """Получаем список ответов для данного задания"""
        return AnswerSerializer(Answer.objects.filter(testing=testing),
                                many=True).data

    class Meta:
        model = Testing
        fields = '__all__'


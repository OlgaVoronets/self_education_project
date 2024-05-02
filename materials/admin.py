from django.contrib import admin

from materials.models import Course, Lesson, Testing, Answer


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    ordering = ('id',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'title')
    list_filter = ('course',)
    ordering = ('id',)


@admin.register(Testing)
class TestingAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'text')
    ordering = ('id',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('testing', 'text', 'is_correct')
    list_filter = ('testing',)
    ordering = ('id',)

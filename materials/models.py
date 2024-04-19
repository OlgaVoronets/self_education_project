from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    """Модель курса - тематический раздел обучения, например, Математика или Иностранный язык"""
    pass


class Lesson(models.Model):
    """Модель урока - теоретический материал, относится к одному конкретному курсу"""
    pass


class Question(models.Model):
    """Тестовое задание, относится к одному конкретному уроку, содержит задачу и
    поле с правильным ответом"""
    pass


class Answer(models.Model):
    """Ответ пользователя на тестовое задание, относится к конкретному объекту Task,
    присваивается пользователю"""
    pass

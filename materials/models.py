from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    """Модель курса - тематический раздел обучения, например, Математика или Иностранный язык"""
    title = models.CharField(max_length=255, verbose_name='Название', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """Модель урока - теоретический материал, относится к одному конкретному курсу"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    title = models.CharField(max_length=255, verbose_name='Название', **NULLABLE)
    content = models.TextField(verbose_name='Материал урока', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Testing(models.Model):
    """Тестовое задание, относится к одному конкретному уроку"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    title = models.TextField(default='Тестовое задание к уроку', verbose_name='Название')
    text = models.TextField(verbose_name='Текст задания', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Answer(models.Model):
    """Ответ на тестовое задание, относится к конкретному объекту Testing"""
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE, verbose_name='Тестирование', **NULLABLE)
    text = models.TextField(verbose_name='Текст ответа', **NULLABLE)
    is_correct = models.BooleanField(default=False, verbose_name='Признак правильного ответа')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class PassedTesting(models.Model):
    """Модель пройденного теста, экземпляр создается в случае правильного ответа на тестовый вопрос"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE, verbose_name='Тестирование')

    def __str__(self):
        return {self.testing}

    class Meta:
        verbose_name = 'Пройденный тест'
        verbose_name_plural = 'Пройденные тесты'

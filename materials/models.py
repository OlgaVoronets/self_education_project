from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    """Модель курса - тематический раздел обучения, например, Математика или Иностранный язык"""
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """Модель урока - теоретический материал, относится к одному конкретному курсу"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Материал урока')

    def __str__(self):
        return f'{self.title} из курса {self.course}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Testing(models.Model):
    """Тестовое задание, относится к одному конкретному уроку"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    text = models.TextField(verbose_name='Текст задания')

    def __str__(self):
        return f'Тестовое задание к уроку {self.lesson}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Answer(models.Model):
    """Ответ на тестовое задание, относится к конкретному объекту Testing"""
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE, verbose_name='Тестирование')
    text = models.TextField(verbose_name='Текст ответа')
    is_correct = models.BooleanField(default=False, verbose_name='Признак правильного ответа')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

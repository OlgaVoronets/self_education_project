from django.contrib import admin

from materials.models import Course, Lesson, Question, Answer

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Answer)


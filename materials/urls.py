from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import CourseCreateView, CourseListView, CourseDetailView, CourseUpdateView, CourseDeleteView, \
    LessonListView, LessonCreateView, LessonDetailView, LessonUpdateView, LessonDeleteView

app_name = MaterialsConfig.name

urlpatterns = [
    #  Модель курса
    path('course/', CourseListView.as_view(), name='course_list'),
    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    #  Модель урока
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
    #  Модель тестирования

]
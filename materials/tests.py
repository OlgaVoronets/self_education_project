from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse

from materials.models import Course, Lesson
from users.models import User


class MaterialsTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        """Создание и авторизация тестового пользователя"""
        self.user = User.objects.create(id=1, email='user@test.ru', password='12345', role='moderator')
        self.client.force_authenticate(user=self.user)
        """Создание тестовых курса и урока"""
        self.course = Course.objects.create(title='test_course', description='test_description')
        self.lesson = Lesson.objects.create(title='test_lesson', content='test_content',
                                            course=self.course)

    def test_create_course(self):
        """Тестирование создания курса"""

        data = {'title': 'creating_test', 'description': 'creating_test_description'}
        path = reverse('materials:course_create')
        response = self.client.post(path=path, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Course.objects.filter(title=data['title']).exists())

    def test_detail_course(self):
        """Тестирование просмотра информации о курсе"""
        path = reverse('materials:course_detail', [self.course.id])
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "title": "test_course",
            "description": "test_description",
            "lessons_list": [
                {"title": "test_lesson",
                 "content": "test_content"}
            ]
        })

    def test_update_course(self):
        """Тестирование редактирования курса"""
        path = reverse('materials:course_update', [self.course.id])
        data = {'title': 'Updating_test', 'description': 'Updating_test'}
        response = self.client.patch(path, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.course.refresh_from_db()
        self.assertEqual(self.course.title, data['title'])

    def test_delete_course(self):
        """Тестирование удаления курса"""
        path = reverse('materials:course_delete', [self.course.id])
        response = self.client.delete(path)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Course.objects.filter(id=self.course.id).exists())

    def test_create_lesson(self):
        """Тестирование создания урока"""

        data = {'title': 'creating_test', 'content': 'creating_test_content',
                'course': self.course.id}
        path = reverse('materials:lesson_create')
        response = self.client.post(path=path, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Lesson.objects.filter(title=data['title']).exists())

    def test_detail_lesson(self):
        """Тестирование просмотра информации об уроке"""
        path = reverse('materials:lesson_detail', [self.lesson.id])
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.lesson.title)

    def test_update_lesson(self):
        """Тестирование редактирования урока"""
        path = reverse('materials:lesson_update', [self.lesson.id])
        data = {'title': 'Updating_test', 'content': 'Updating_test'}
        response = self.client.patch(path, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, data['title'])

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        path = reverse('materials:lesson_delete', [self.lesson.id])
        response = self.client.delete(path)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())

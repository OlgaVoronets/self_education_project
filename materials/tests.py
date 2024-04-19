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
        """Asserts для успешного удаления урока"""
        path = reverse('materials:lesson_delete', [self.lesson.id])
        response = self.client.delete(path)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())

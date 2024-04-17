## Проект самообучения

# Задание:

Реализовать функционал самообучения для студентов. Для этого необходимо создать платформу, которая работает только с авторизованными пользователями. 
На платформе необходимо предусмотреть функционал разделов и материалов. Для каждого материала можно добавить тесты. Управление всеми сущностями необходимо реализовать через стандартный Django admin. 
Проверка ответа на тест осуществляется с помощью отдедльного запроса на бэкенд. Реализовать либо Rest API, либо SSR с использованием Bootstrap. 
Для реализации проекта использовать фреймворк Django.

# План работы:

1. Создать Django-проект и установить необходимые зависимости
2. Прописать настройки с использованием переменных окружения, документирование, CORS
3. Создать модели пользователя, курса, урока и тестового задания
4. Реализовать CRUD для каждой модели
5. Описать права доступа
6. Тестирование функционала проекта

# Описание:



# Инструкция по установке:

В файле .env.default необходимо внести SECRET_KEY , переменные окружения заданы по умолчанию, их можно изменить для дальнейшей работы с проектом
Для установки зависимостей необходимо активировать виртуальное окружение командой  venv\Scripts\activate
и выполнить pip install requirements.txt
Затем применить миграции командой python manage.py migrate  и запустить сервер python manage.py runserver
Для доступа к административной странице используется команда создания суперпользователя python manage.py csu  (по умолчанию заданы логин 'admin' и пароль '12345')

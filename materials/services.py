from materials.models import Testing, Answer, PassedTesting


# def testing_func(user, lesson):
#     """Функция тестирования"""
#     data = {}
#     #  Получаем тест(экземпляр класса Testing) и набор ответов (Queryset)
#     testing = Testing.objects.get(lesson=lesson)
#     answers = Answer.objects.filter(testing=testing)
#
#     # Выводим текст задания
#     print("Прочитайте условие задачи и выберите правильный ответ из предложенных вариантов")
#     print(testing.text)
#
#     #  Выводим вопросы с нумерацией от 1
#     for i in range(len(answers)):
#         print(f'{i + 1} - {answers[i]}')
#
#     #  Запрашиваем ответ пользователя
#     user_answer = int(input('Введите номер ответа  '))
#
#     data['testing'] = testing
#     data['answers'] = answers
#     data['user_answer'] = user_answer
#
#     #  Проверяем правильность ответа
#     if answers[user_answer - 1].is_correct:
#         print("Верно!")
#         data['result'] = "Верно!"
#         #  Создаем объект класса "пройденный тест", если тест пройден повторно - не создаем
#         if not PassedTesting.objects.filter(user=user, testing=testing).exists():
#             PassedTesting.objects.create(user=user, testing=testing)
#     else:
#         print('Неверно! Изучите материал урока повторно и попробуйте еще раз')
#         data['result'] = 'Неверно! Изучите материал урока повторно и попробуйте еще раз'


def testing_func(user, lesson):
    """Функция тестирования"""
    data = []
    #  Получаем тест(экземпляр класса Testing) и набор ответов (Queryset)
    testing = Testing.objects.get(lesson=lesson)
    answers = Answer.objects.filter(testing=testing)

    #  Запрашиваем ответ пользователя
    user_answer = int(input('Введите номер ответа  '))

    data.append(testing)
    data.append(answers)
    data.append(user_answer)

    #  Проверяем правильность ответа
    if answers[user_answer - 1].is_correct:

        data.append({"result": "Верно!"})
        #  Создаем объект класса "пройденный тест", если тест пройден повторно - не создаем
        if not PassedTesting.objects.filter(user=user, testing=testing).exists():
            PassedTesting.objects.create(user=user, testing=testing)
    else:

        data.append({"result": 'Неверно! Изучите материал урока повторно и попробуйте еще раз'})
    return data

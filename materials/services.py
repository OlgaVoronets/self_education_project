from materials.models import Testing, Answer, PassedTesting


def testing_func(user, lesson):
    """Функция тестирования"""

    #  Получаем тест(экземпляр класса Testing) и набор ответов (Queryset)
    testing = Testing.objects.get(lesson=lesson)
    answers = Answer.objects.filter(testing=testing)

    # Выводим текст задания
    print("Прочитайте условие задачи и выберите правильный ответ из предложенных вариантов")
    print(testing.text)

    #  Выводим вопросы с нумерацией от 1
    for i in range(len(answers)):
        print(f'{i + 1} - {answers[i]}')

    #  Запрашиваем ответ пользователя
    user_answer = int(input('Введите номер ответа  '))

    #  Проверяем правильность ответа
    if answers[user_answer - 1].is_correct:
        print("Верно!")
        #  Создаем объект класса "пройденный тест", если тест пройден повторно - не создаем
        if not PassedTesting.objects.filter(user=user, testing=testing).exists():
            PassedTesting.objects.create(user=user, testing=testing)
    else:
        print('Неверно! Изучите материал урока повторно и попробуйте еще раз')

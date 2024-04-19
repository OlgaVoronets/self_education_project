from materials.models import Testing, Answer


def testing_func(lesson):
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

    #  Проверяем правильность ответа и сообщаем пользователю результат
    if answers[user_answer - 1].is_correct:
        print("Верно!")
    else:
        print('Неверно! Изучите материал урока повторно и попробуйте еще раз')

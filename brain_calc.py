from datetime import date
import random
import time

today = date.today()


yes_answers = ["да", "yes", "ага", "верно", "так точно",
               "lf", "l", "д", "давай", "давайте", "y", "д "]
no_answers = ["no", "нет", "неа", "не", "н", "n", "ytn", "н "]
insults = ["иди на хуй", "иди нахуй", "пошел на хуй", "пошел ты",
           "отъебись", "сука", "чмо", "иди нах", "иди нах"]
greenings = ['Приветствую! Я наумнейший калькулятор от Алексея! Помогу сложить тебе любые два числа! ', 'Привет, Амиго. ', 'Hello, my friend! ',
             'Рад приветствовать тебя! ', 'Наиумнейшая программа по сложению двух цифр приветствует тебя! ', 'Привет! ']
count_answers = ["По моим подсчетам выходит ", "Да, это была сложная задача, но я подсчитал ", "Так-так-так... дайте подумать... по моему получается ",
                 "Ух! Какие большие числа ты ввел, без меня ты бы не справился! Итак, правильный ответ ", "Ну это уж вообще легкотня - "]
насмешка = ["Ахахахахаха! Ты реально не можешь сам сосчитать такие маленькие цифры?",
            "Арррррхххх!!! Я великий складыватель цифр!!! Как ты посмел тратить мое время на такие пустяки?!?!?!"]
список_фраз_усложняющих_пример = ["Давай усложним задачу!", "Пожалуй мы сделаем чуточку потяжелее!",
                                  "Предлагаю слегка изменить условия задачи!", "Шутки прочь, считаем взрослую задачку!!!"]


def sleep():  # функция спящий режим
    text = 'Буду нужен - пиши! '
    for letter in text:
        time.sleep(0.1)
        print(letter, end='', flush=True)
    print('')
    text = 'Введи текст: '
    for letter in text:
        time.sleep(0.1)
        print(letter, end='', flush=True)
    input("")
    text = 'Хорошо поспал! Давай продолжим! '
    for letter in text:
        time.sleep(0.1)
        print(letter, end='', flush=True)
    calc()


def calc():  # основная функция калькулятора
    a = int(input('Введи 1-е число: '))
    b = int(input('Введи 2-е число: '))
    d = int(today.day)
    y = int(today.year)
    m = int(today.month)

    if a <= 10 and b <= 10:
        print(f'{random.choice(насмешка)}')

        def усложнение_задачи():
            список_сложных_задач = [1, 2, 3, 4]
            рандомный_список_сложных_задач = random.choice(
                список_сложных_задач)
            if рандомный_список_сложных_задач == 1:
                print(f'{random.choice(список_фраз_усложняющих_пример)}')
                print(
                    f'Возьмем твой возраст, вычтем из него какой сегодня день, прибавим год и умножим на сумму твоих чисел!!!')
                print(f'Получается вот такой пример:')
                print(f'({age} - {d} + {y}) * ({a} + {b})')
                print(f'Ответ: {(age - d + y) * (a + b)}. ')
                print(f'Все элементарно!')
                print('')
                print(f'Ну а что ты просил сосчитать {
                      name}, получается - {a + b}.')

            elif рандомный_список_сложных_задач == 2:
                print(f'Легче легкого, {name}, правильный ответ -  {a + b}')

            elif рандомный_список_сложных_задач == 3:
                print(f'Что бы не было так легко,')
                print('Я придумал новую задачку!')
                print(f'Берем твой возраст - {age}')
                print(
                    f'Умножаем на порядковый номер месяца, который сейчас - {m}')
                print(f'Вычитаем сегодняшнее число - {d}')
                print(f'Получаем: {age * m - d}')
                print('')
                print(f'Ты реально сам не можешь сосчитать {a} + {b}?')
                print(f'Ну это же {a + b}.')

            else:
                print(f'Ответ: {a + b}.')
                print('Я создан для более сложных примеров...')

        усложнение_задачи()

        question = input(f'Ну что? Еще разок? (Напиши "Да" или "Нет"): ')

        if question in yes_answers:
            calc()

        elif question in no_answers:
            print('Хорошо поработали, до новых встреч, Амиго!')
            sleep()

        else:
            print(f'Я пока не понимаю, что ты имеешь ввиду говоря "{
                  question}"')
            restart()
            question = input(f'Ну что? еще разок? (Напиши "Да" или "Нет"): ')

    elif a < 1000000 and b < 1000000:
        print(f'{random.choice(count_answers)}{a + b}!')
        question = input(f'Ну что? Еще разок? (Напиши "Да" или "Нет"): ')
        if question in yes_answers:
            calc()

        elif question in no_answers:
            print('Не плохо поработали, до новых встреч, Стажер!')
            sleep()

        elif question in insults:
            print("Ну ты и урод! Ты добавлен в черный список!!!")

        else:
            print(f'Я пока не понимаю, что ты имеешь ввиду говоря "{
                  question}"')
            restart()

    else:
        print('Давай что нибудь попроще!!!')
        calc()


def restart():  # функция начать занова, если что-то не понятно
    question = input('Давайте попробуем еще раз? (Введи "Да" или "Нет"): ')
    if question in yes_answers:
        print('Отлично!')
        calc()

    elif question in no_answers:
        print(f'Так бы сразу и сказал! Пока, {name}!')
        sleep()

    elif question in insults:
        print("Ну ты и урод! Ты добавлен в черный список!!!")

    else:
        print(f'Я пока не понимаю что означает "{question}"')
        restart()


def name():  # узнаем имя
    text = 'Давай познакомимся, как тебя зовут?'
    for letter in text:
        time.sleep(0.1)
        print(letter, end='', flush=True)

    name = input(' ')
    return name.capitalize()


def age():  # возраст
    text = 'Сколько тебе лет?'
    for letter in text:
        time.sleep(0.1)
        print(letter, end='', flush=True)

    age = input(' ')
    return age


hello = random.choice(greenings)  # тело приложения
for letter in hello:
    time.sleep(0.1)
    print(letter, end='', flush=True)

name = name()
text = 'Приятно познакомиться, '
for letter in text:
    time.sleep(0.1)
    print(letter, end='', flush=True)
text = name
for letter in text:
    time.sleep(0.1)
    print(letter, end='', flush=True)
print('. ')


age = age()
text = 'Ого! '
for letter in text:
    time.sleep(0.1)
    print(letter, end='', flush=True)
text = age
for letter in text:
    time.sleep(0.1)
    print(letter, end='', flush=True)
print('. ')
text = 'Это весьма солидный возраст! Ты наверное уже хорошо считаешь:) А я на много моложе, мне еще всего лишь несколько дней'
for letter in text:
    time.sleep(0.1)
    print(letter, end='', flush=True)
print(':)')


def start():  # функция начального включения

    text = 'Ну что, ты готов к сложению чисел? (Напиши "Да" или "Нет"): '
    for letter in text:
        time.sleep(0.1)
        print(letter, end='', flush=True)

    question = input(' ')

    if question.lower() in yes_answers:
        calc()

    elif question.lower() in no_answers:
        text = 'Ну как знаешь, зачем только меня включал... '
        for letter in text:
            time.sleep(0.1)
            print(letter, end='', flush=True)
        sleep()

    elif question.lower() in insults:
        print(f'Ну ты и урод, {
              name}! Ты добавлен в черный список!!! Сам, {question}!')

    else:
        print(f'Я пока не понимаю что означает "{question}"')
        restart()


start()

print('version 3.0')
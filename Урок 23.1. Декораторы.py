def func(*args, **kwargs):
    print(f'{args=}')
    print(f'{kwargs=}')

func(1,2, 56,56)


"""def decorator_with_args(func):
    print('Декоратор с аргументами...')
    def decorated(a, b):
        print('Началось оформление покупки', func.__name__)
        ret = func(a, b)
        print(' sent message to admin:Оформлена доставка', func.__name__)
        return ret

    return decorated

@decorator_with_args
def sub(a, b):
    print('Функция 1')
    return a - b

@decorator_with_args
def add(a, b):
    print('Функция 2')
    return a + b

print('start')
r = add(10, 5)
print('r:', r)
g = sub(10, 5)
print('g:', g)
print('Конец')


"""















"""class Decorator:
    def __init__(self, func):
        print('> Класс decorator метод __init__')
        self.func = func

    def __call__(self):
        print('> юзер начал заполнять заявку...<', self.func.__name__)
        self.func()
        print('> оплата <')

@Decorator
def sort():
    emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
              'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
              'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
              'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
              'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
              'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
    print(*sorted({i + '@' + k for k, v in emails.items() for i in v}), sep='\n')

print('>> start')
sort()

print('>> конец')

"""
"""
Методические указания
Урок 23.1. Декораторы
Задачи урока:
Декораторы

0. Подготовка к уроку

До начала урока преподавателю необходимо:
Просмотреть, как ученики справились с домашним заданием
Прочитать методичку

1. Декораторы

Учитель:  Ну что ж, давайте продолжим знакомство с декораторами. На прошлом занятии мы уже познакомились немного с ними. Декоратор, как мы помним - функция-обертка. Но можно создать и класс декоратор. Давайте рассмотрим это на примере.

Добавив метод __call__ в класс, его можно превратить в вызываемый объект. А поскольку декоратор — это всего лишь функция, то есть, вызываемый объект, класс можно превратить в декоратор с помощью функции __call__.

class Decorator:
    def __init__(self, func):
        print('> Класс Decorator метод __init__')
        self.func = func

    def __call__(self):
        print('> перед вызовом класса...', self.func.__name__)
        self.func()
        print('> после вызова класса')

@Decorator
def wrapped():
    print('функция wrapped')

print('>> старт')
wrapped()
print('>> конец')




Результат

> Класс Decorator метод __init__
>> старт
> перед вызовом класса... wrapped
функция wrapped
> после вызова класса
>> конец


Отличие в том, что класс инициализируется при объявлении. Он должен получить функцию в качестве аргумента для метода __init__. Это и будет декорируемая функция.

При вызове декорируемой функции на самом деле вызывается экземпляр класса. А поскольку объект вызываемый, то вызывается функция __call__.

Учитель:  А что если функция, которую требуется декорировать, должна получать аргументы? Для этого нужно вернуть функцию с той же сигнатурой, что и у декорируемой.


def decorator_with_args(func):
    print('> декоратор с аргументами...')
    def decorated(a, b):
        print('до вызова функции', func.__name__)
        ret = func(a, b)
        print('после вызова функции', func.__name__)
        return ret
    return decorated

@decorator_with_args
def add(a, b):
    print('функция 1')
    return a + b

@decorator_with_args
def sub(a, b):
    print('функция 2')
    return a - b

print('>> старт')
r = add(10, 5)
print('r:', r)
g = sub(10, 5)
print('g:', g)
print('>> конец')


Результат
> декоратор с аргументами...
> декоратор с аргументами...
>> старт
до вызова функции add
функция 1
после вызова функции add
r: 15
до вызова функции sub
функция 2
после вызова функции sub
g: 5
>> конец

С классом тот же принцип. Нужно лишь добавить желаемую сигнатуру в функцию __call__.

class Decorator:
    def __init__(self, func):
        print('> Класс Decorator метод __init__')
        self.func = func

    def __call__(self, a, b):
        print('> до вызова из класса...', self.func.__name__)
        self.func(a, b)
        print('> после вызова из класса')

@Decorator
def wrapped(a, b):
    print('функция wrapped:', a, b)

print('>> старт')
wrapped(10, 20)
print('>> конец')


Результат
> Класс Decorator метод __init__
>> старт
> до вызова из класса... wrapped
функция wrapped: 10 20
> после вызова из класса
>> конец

Можно использовать *args и **kwargs и для функции wrapper, если сигнатура заранее неизвестна, или будут приниматься разные типы функций.

args и kwargs используются, когда мы не знаем заранее сколько аргументов передаст пользователь. args - обычные аргументы, переданные через запятую, а kwargs - именованные аргументы. Давайте рассмотрим на примере обычной функции.

def func(*args, **kwargs):
    print(f'{args=}')
    print(f'{kwargs=}')

func(1, 2, 3, a=5, b=1)




Результат
args=(1, 2, 3)
kwargs={'a': 5, 'b': 1}

Давайте для практики реализуем декоратор, который замеряет сколько занимает в памяти объект возвращаемый функцией .

import sys
import time
def get_size(func):
   def wrapper(a, b, delay=0):
       result = sys.getsizeof(func(a, b, delay))
       print(f'>> функция {func.__name__} занимает в памяти: {result} байт')
   return wrapper

@get_size
def add_with_delay(a, b, delay=0):
   print('сложить', a, b, delay)
   time.sleep(delay)
   return a * b

print('старт программы')
add_with_delay(10000, 200000)
add_with_delay(10, 20, 1)
print('конец программы')




Результат
старт программы
сложить 10000 200000 0
>> функция add_with_delay занимает в памяти: 32 байт
сложить 10 20 1
>> функция add_with_delay занимает в памяти: 28 байт
конец программы

2. Решение задач
Задача 1
Написать функцию, которая возвращает сумму двух чисел 4 и 5, также написать декоратор get_type, который выводит тип данных возвращаемый декорируемой функцией.

Решение
def get_type(func):
   def wrapper(*args, **kwargs):
       print('Вызываем функцию')
       result = func()
       print(result)
       print(f'Тип данных, возвращаемых функцией {type(result)}')
   return wrapper


@get_type
def func():
   return 4 + 5


func()





Дополнительно
Если на уроке остается время, то ученикам можно предложить начать прорешивать домашнее задание.

Домашняя работа
Задача 1
Создать декоратор, измеряющий время выполнения функции. Для расчета времени ознакомьтесь с модулем datetime

Решение
"""
import time
# определяем декоратор с именем timer
def timer(func):

    def wrapper(*args, **kwargs):    # определеяем функцию обертку, которая будет изменять исходную функцию
        start_time = time.time()
        print(start_time)# запоминаем текущее время перед выполнением функции
        result = func(*args, *kwargs)        # выполняем исходную функцию и сохраняем ее результат
        print(result)
        end_time = time.time()# запоминаем текущее время после выполнения функци
        print(end_time)
        print(f"Время выполнения функции{func.__name__} : {end_time - start_time} секунд")
        return result #возвращаем результат исходной функцию
    return wrapper # возвращаем функцию обертки в качестве резульата декоратора

@timer # применяем декоратор к основной функции
def example_function(duration):
    time.sleep(duration)

example_function(2)


"""import time # импортируем время

# декоратор для измерения времени выполнения функц
def timer_decorator(func): # принимает в качестве аргумента функцию, которую нужно обернуть
    # внутри декоратора определяется функция - обертка, которая будет заменять оригинал функцию
    def wrapper(*args, **kwargs):# принимает все аргументы, которые передаются оригинал функии
        start_time = time.time() # время перед вызовом функ
        result = result = func(*args, **kwargs)
        end_time = time.time() # время после вызовом функции
        print(f"Функция {func.__name__} выполнилась за{end_time - start_time:.5f} секунд") # рассчитываем и выводим время выполнения функции
        return result  # возвращаем результат ориг функции
    return wrapper # возвращаем функ обертку вместо оригинал функии

# с помощью синтаксиса @ применяем декоратор к функции
@timer_decorator # говорим пайтон, что функ example нужно обернуть с помощью timer decorator
def example_function(): # same func
    time.sleep(2)
    print("Сработала основная функция")

example_function()#вызываем функцию которая теперь обернута декоратором




Методические указания
Урок 22.1. Декораторы
Задачи урока:
Декораторы

0. Подготовка к уроку

До начала урока преподавателю необходимо:
Просмотреть, как ученики справились с домашним заданием
Прочитать методичку

1. Декораторы

Учитель:  Сегодня мы начнем погружаться в тему декораторов в Python. Давайте разберем, что такое декоратор.
Итак, что же это такое? Для того, чтобы понять, как работают декораторы, в первую очередь следует вспомнить, что функции в python являются объектами, соответственно, их можно возвращать из другой функции или передавать в качестве аргумента. Также следует помнить, что функция в python может быть определена и внутри другой функции.
Вспомнив это, можно смело переходить к декораторам. Декораторы — это, по сути, "обёртки", которые дают нам возможность изменить поведение функции, не изменяя её код.

По сути декоратор — это функция, которая принимает функцию, делает что-то и возвращает другую функцию.

def decorator(func):
    def wrapper():
        print('функция-оболочка')
        func()
    return wrapper

def basic():
    print('основная функция')

wrapped = decorator(basic)
print('старт программы')
basic()
wrapped()
print('конец программы')



Результат
старт программы
основная функция
функция-оболочка
основная функция
конец программы

Разберемся с тем, что здесь произошло. Функция decorator — это, как можно понять по названию, декоратор. Она принимает в качестве параметра функцию func. Крайне оригинальные имена. Внутри функции объявляется другая под названием wrapper. Объявлять ее внутри не обязательно, но так проще работать.

В этом примере функция wrapper просто вызывает оригинальную функцию, которая была передана в декоратор в качестве аргумента, но это может быть любая другая функциональность.
В конце возвращается функция wrapper. Напомним, что нам все еще нужен вызываемый объект. Теперь результат можно вызывать с оригинальным набором возможностей, а также новым включенным кодом.
Но в Python есть синтаксис для упрощения такого объявления. Чтобы декорировать функции, используется символ @ рядом с именем декоратора. Он размещается над функцией, которую требуется декорировать

def decorator(func):
    '''Основная функция'''
    print('декоратор')
    def wrapper():
        print('-- до функции', func.__name__)
        func()
        print('-- после функции', func.__name__)
    return wrapper

@decorator
def wrapped():
    print('--- обернутая функция')

print('- старт программы...')
wrapped()
print('- конец программы')


Результат
декоратор
- старт программы...
-- до функции wrapped
--- обернутая функция
-- после функции wrapped
- конец программы

Можно использовать тот же декоратор с любым количеством функций, а также — декорировать функцию любым декоратором.

def decorator_1(func):
    print('декоратор 1')
    def wrapper():
        print('перед функцией')
        func()
    return wrapper

def decorator_2(func):
    print('декоратор 2')
    def wrapper():
        print('перед функцией')
        func()
    return wrapper

@decorator_1
@decorator_2
def basic_1():
    print('basic_1')

@decorator_1
def basic_2():
    print('basic_2')

print('>> старт')
basic_1()
basic_2()
print('>> конец')


Результат
декоратор 2
декоратор 1
декоратор 1
>> старт
перед функцией
перед функцией
basic_1
перед функцией
basic_2
>> конец

Когда у функции несколько декораторов, они вызываются в обратном порядке относительно того, как были вызваны. То есть, такой вызов:

@decorator_1
@decorator_2
def wrapped():
    pass


аналогичен

a = decorator_1(decorator_2(wrapped))

Если декорированная функция возвращает значение, и его нужно сохранить, то нужно сделать так, чтобы его возвращала и функция-обертка.

2. Решение задач
Задача 1
Написать простой декоратор добавляющий текст начало функции и конец функции к функции, которая выводит Привет мир!

Решение

def decor(func):
    def wrapper():
        print('Начало функции')
        func()
        print('Конец функции')
    return wrapper

@decor
def func():
    print('Привет мир!')

func()


Дополнительно
Если на уроке остается время, то ученикам можно предложить начать прорешивать домашнее задание.

Домашняя работа
Задача 1














#Файл где  функции
####################################################
#1 файл импортируемый calc1.py
def mul():
    pass


####################################################
#2 Файл основной программы
from calc1 import mul






"""
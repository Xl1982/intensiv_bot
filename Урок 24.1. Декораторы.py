class DecoratorArgs:
    def __init__(self, name):
        print('> декоратор с аргументами __init__: ', name)
        self.name = name

    def __call__(self, func):
        def wrapper(a, b):
            print(' до обернутой функции ')
            func(a, b)
            print("после обернутой функции")
        return wrapper

@DecoratorArgs('test')
def add(a, b):
    print('функция add', a, b)

print(' >>> start')
add(10, 20)
print('>> конец')






















user_permissoins = ['user', 'admin']
def check_permission(permission):
    def wrapper_permission(func):
        def wrapperd_check():

            if permission not in user_permissoins:
                raise ValueError("НЕДОСТАТОЧНО ПРАВ")

            return func()
        return wrapperd_check
    return wrapper_permission

@check_permission('user')
def check_value():
    return 'значение'

@check_permission('admin')
def do_something():
    return  'только админ'
print('старт программы')

check_value()
do_something()
print('конец программы')








"""from functools import wraps

def decorator(func):
    '''Декоратор'''
    @wraps(func)
    def decorated():
        func()
    return decorated

@decorator
def wrapped():
    print('функция wrapped')


print('старт программы...')
print(wrapped.__name__) # имя функции
print(wrapped.__doc__) # выводит то что закоментированно в три ковычки
print('конец программы')



"""













"""class DecoratorArgs: # opredelenie classa decoratora kotoryi budet prinimat argument
    def __init__(self, name): # konstruktor classa
        print('> decorator s argumentami ', name)
        self.name = name # sohranyaem ima v peremennyu

    def __call__(self, func): # Магический метод __call__ позволяет обрабатывать вызов экземпляра класса как функцию
        # в нашем случае это позволяет использовать экземпляр класса как декоратор
        def wrapper(a, b): # внутренняя функция - обертка которая будет выполняться вместо декорируемой функции
            print('>>> do obernutoy funkci start time')
            func(a, b)
            print(' posle obernutoi funkcii end time')
        return wrapper

@DecoratorArgs('test')
def add(a, b):
    print('funkcii add:', a, b)

print('>>>start')
add(10, 20)
print('konec')"""

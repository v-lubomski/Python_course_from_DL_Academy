from random import randint


def foo():
    """Выводит последовательность чисел от 1 до случайного числа"""
    for el in range(1, randint(1, 10)):
        print(el)


foo()

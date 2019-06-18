# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def segment_fib(n: int, m: int) -> list:  # Решение с помощью рекурсии
    """
    Return list of Fibonacci numbers in a sequence from n to m inclusively
    :param n: start point of numbers sequence
    :param m: end point of numbers sequence
    :return: dict of Fibonacci numbers in a sequence from n to m
    """
    dict_fib = {1: 1, 2: 1}  # Создаём словарь из начальных элементов

    def fib(x):  # Будем строить рекурсию до максимального значения, добавляя вычисленные значения в словарь
        if x in dict_fib:  # Проверяю, вычислено ли уже значение
            return dict_fib[x]  # и если вычислено - возвращаю его
        dict_fib[x] = fib(x - 1) + fib(x - 2)  # Если не вычислено - вычисляю
        return dict_fib[x]  # И добавляю в словарь, чтобы не вычислять заново

    fib(m)  # Получаю словарь, где значения - числа Фибоначчи от 1-го до m
    list_fib = sorted(list(dict_fib.values()))  # Конвертирую значения словаря в отсортированный список чисел
    return list_fib[n-1:m]  # Делаю срез необходимых значений


print('Задача 1. Числа Фибоначчи:', segment_fib(9, 15))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

from random import choice, randint


def sort_to_max(origin_list: list) -> list:
    """
    Sorting numbers in "origin_list" from less to more using "quick sort" algorithm
    :param origin_list: unsorted list of numbers
    :return: sorted origin_list
    """
    if len(origin_list) <= 1:
        return origin_list
    else:
        pivot = choice(origin_list)
        less = [x for x in origin_list if x < pivot]
        equal = [x for x in origin_list if x == pivot]
        grater = [x for x in origin_list if x > pivot]
        return sort_to_max(less) + equal + sort_to_max(grater)


my_list = [randint(1, 1000) for x in range(20)]
print('Задача 2. Несортированный список:', my_list)
print('Задача 2. Отсортированный список:', sort_to_max(my_list))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, sequence):
    """
    Filter "sequence" with "func" function
    :param func: function
    :param sequence: sequence (list or other types sequences)
    :return:
    """
    return (el for el in sequence if func(el))


print('Задача 3. Отфильтрованный список из предыдущей задачи, с числами больше 500:',
      list(my_filter(lambda x: True if x > 500 else False, my_list)))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def input_to_dict(input_string):
    list_of_values = input_string.split(',')
    coordinates_dict = dict()
    coordinates_dict['x'] = int(list_of_values[0])
    coordinates_dict['y'] = int(list_of_values[1])
    return coordinates_dict


a1 = input_to_dict(input('Введите через запятую без пробелов координаты x,y точки A1 (пример: 345,14): '))
a2 = input_to_dict(input('Введите через запятую без пробелов координаты x,y точки A2 (пример: 345,14): '))
a3 = input_to_dict(input('Введите через запятую без пробелов координаты x,y точки A3 (пример: 345,14): '))
a4 = input_to_dict(input('Введите через запятую без пробелов координаты x,y точки A4 (пример: 345,14): '))

x1, y1 = a1['x'], a1['y']
x2, y2 = a2['x'], a2['y']
x3, y3 = a3['x'], a3['y']
x4, y4 = a4['x'], a4['y']

if x3 - x2 == x4 - x1 and y2 - y1 == y3 - y4:
    print('Введённые точки - вершины паралеллограмма')
else:
    print('Введённые точки - не вершины паралеллограмма')

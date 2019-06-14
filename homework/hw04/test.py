# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import re
# Подзадача 1 - парсинг дробей

# equation = input('Калькулятор дробей поддерживает сложение и вычитание положительных и отрицательных дробей '
#                       'с целой частью или без.\n'
#                       'Уравнение записывается в виде: n x/y + n2 x2/y2, '
#                       'где n - целая часть, x - числитель, у - знаменатель.\n'
#                       'Двойкой в примере выше обозначается лишь принадлежность ко второй дроби.\n'
#                       'Пример с числами: 45 5/6 - 4/7\n\n'
#                       'Введите свой пример: ')

equation = '-2 3/334545 + 3/334545'  # строка - пример с дробью для экспериментов

first_fraction_str = re.findall(r'^-?\d*\s?-?\d*/?\d*', equation)[0].strip()  # получаю строку с первой дробью
second_fraction_srt = re.findall(r'-?\d*\s?-?\d*/?\d*$', equation)[0].strip()  # получаю строку со второй дробью


def convert(fraction_str):
    fraction_str = re.split(r' ', fraction_str)  # создаю из строки список с целой (если есть) и дробной частью
    # надо ещё разбить по слешу
    return fraction_str


print(convert(first_fraction_str))
print(convert(second_fraction_srt))

# first_fraction = {'num': 0, 'den': 0, 'div': 0}
# second_fraction = {'num': 0, 'den': 0, 'div': 0}
#
# if len(equation_list) == 5:
#     first_fraction['num'] = equation_list[0]
#     first_fraction['den'] = equation_list[1][0]
#     first_fraction['div'] = equation_list[1][2]
#     second_fraction['num'] = equation_list[3]
#     second_fraction['den'] = equation_list[4][0]
#     second_fraction['div'] = equation_list[4][2]
#     sign = equation_list[2]
# elif len(equation_list) == 3:
#     first_fraction['den'] = equation_list[0][0]
#     first_fraction['div'] = equation_list[0][2]
#     second_fraction['den'] = equation_list[2][0]
#     second_fraction['div'] = equation_list[2][2]
#     sign = equation_list[1]
#
# print(first_fraction, second_fraction)


def gcd(x: int, y: int) -> int:
    """
    Находит наибольший общий делитель у "x" и "y"
    """
    while y != 0:
        (x, y) = (y, x % y)
    return x


def add_or_sub(den1: int, div1: int, sign: str, den2: int, div2: int) -> (int, int, int):
    """
    Складывает две дроби, упрощает, выделяет целую часть
    :param den1: знаменатель первого числа
    :param div1: делитель первого числа
    :param sign: знак ("+" или "-")
    :param den2: знаменатель второго числа
    :param div2: делитель второго числа
    :return: кортеж: целая часть, делитель, знаменатель (int, int, int)
    """

    if sign == '+':
        total_den = den1 * div2 + div1 * den2  # приводим знаменатели к общему делителю и складываем
    if sign == '-':
        total_den = den1 * div2 - div1 * den2  # приводим знаменатели к общему делителю и вычитаем
    com_div = div1 * div2  # вычисляем общий делитель

    gr_com_div = gcd(total_den, com_div)  # находим наибольший общий делитель
    den = total_den//gr_com_div  # сокращаем знаменатель
    div = com_div//gr_com_div  # сокращаем делитель
    if den < 0:  # находим целую часть и знаменатель
        num = (abs(den) // div) * -1
        den = (abs(den) % div) * -1
    else:
        num = den // div
        den = den % div
    if den == 0:  # если знаменатель сократился
        div = 0  # сокращаем и делитель
    return num, den, div




print(add_or_sub(-198, 7, '-', -33, 152))


# Задачи:
# 1) Реализовать вычитание
# 2) Реализовать работу с отрицательными числами (приводить к отрицательному знаменателю)
# 3) Реализовать парсинг уравнения и приведение целого к дроби

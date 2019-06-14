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


equation = input('Калькулятор дробей поддерживает сложение и вычитание положительных и отрицательных дробей '
                 'с целой частью или без.\n'
                 'Уравнение записывается в виде: n x/y + n2 x2/y2, '
                 'где n - целая часть, x - числитель, у - знаменатель.\n'
                 'Двойкой в примере выше обозначается лишь принадлежность ко второй дроби.\n'
                 'Пример с числами: 45 5/6 - 4/7\n\n'
                 'Введите свой пример: ')

fractions = []
sign = ''

if ' + ' in equation:
    fractions = equation.split(' + ')
    sign = '+'
if ' - ' in equation:
    fractions = equation.split(' - ')
    sign = '-'


def convert(fraction_str):
    fraction = {'num': 0, 'den': 0, 'div': 0}
    if '/' not in fraction_str:
        fraction['num'] = int(fraction_str)
    elif ' ' in fraction_str:
        fraction['num'] = int(fraction_str.split(' ')[0])
        fraction['den'] = int(re.findall(r'^\d+', fraction_str.split(' ')[1])[0])
        fraction['div'] = int(re.findall(r'\d+$', fraction_str.split(' ')[1])[0])
    else:
        fraction['den'] = int(re.findall(r'^-?\d+', fraction_str)[0])
        fraction['div'] = int(re.findall(r'\d+$', fraction_str)[0])
    return fraction


first_fraction = convert(fractions[0])
second_fraction = convert(fractions[1])

print(first_fraction, second_fraction)


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



# Задачи:
# 2) Реализовать работу с отрицательными числами (приводить к отрицательному знаменателю)
# 3) Реализовать парсинг дроби приведение целого к дроби

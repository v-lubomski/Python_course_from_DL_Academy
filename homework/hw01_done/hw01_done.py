__author__ = 'Любомский Владислав Байрамгельдыевич'
import math

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.


name = input('Пожалуйста, введите ваше имя: ')
age = int(input('Пожалуйста, введите ваш возраст: '))
res = age - 18

if res > 0:
    compare = 'больше'
elif res < 0:
    compare = 'меньше'
    res = res * -1
else:
    compare = 'равен'

if res % 10 == 1:
    years = 'год'
elif res % 10 < 5:
    years = 'года'
else:
    years = 'лет'

print('Возраст', name, 'на', res, years, compare, '18')


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input('Введите значение переменной a: '))
b = int(input('Введит значение переменной b: '))
a = a + b
b = a - b
a = a - b
print('a = ', a, ', b = ', b, sep='')

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = int(input('Введите коэффициент a: '))
b = int(input('Введите коэффициент b: '))
c = int(input('Введите коэффициент c: '))

disc = b**2 - 4 * a * c
if disc > 0:
    x1 = int((-b + math.sqrt(disc)) / (2 * a))
    x2 = int((-b - math.sqrt(disc)) / (2 * a))
    print('Корни уравнения: ', x1, ',', x2)
elif disc == 0:
    x = int((-b + math.sqrt(disc)) / (2 * a))
    print('Корень уравнения: ', x)
else:
    print('Корни отсутствуют :(')
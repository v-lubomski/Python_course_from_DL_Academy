# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили


def convert(km):
    miles = km * 1.609
    print(miles, 'миль')


print('Задача 1. Мили: ', end='')
convert(23)

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number: float, ndigits: int) -> float:
    """
    Rounds number "number" to "ndigits" digits after point
    :param number: floating point number
    :param ndigits: to how many digits after the point we want to round "number"
    :return:
    """
    number = number * 10**ndigits  # Сдвигаем точку вправо на ndigits знаков
    if number - int(number) > 0.5:  # Если первая цифра после точки больше 5
        number = number // 1 + 1  # Округляем число вверх, обрубая знаки после точки и прибавляя 1
    else:
        number = number // 1  # Если нет - просто обрубаем число до точки (целочисленное деление всегда округляет вниз)
    return number / 10**ndigits  # Сдвигаем точку на ndigits знаков влево


print('Задача 2. Округляем 2.1234567:', my_round(2.1234567, 5))
print('Задача 2. Округляем 2.1999967:', my_round(2.1999967, 5))
print('Задача 2. Округляем 2.9999967:', my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# либо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number: int) -> bool:
    """
    Checks six-digit number "ticket_number": if first three nums equal last three nums - return True, else - False
    :param ticket_number: six-digit integer
    :return: Boolean
    """
    nums_list = list(map(int, str(ticket_number)))  # Превращаем переданное число в список чисел
    if sum(nums_list[:3]) == sum(nums_list[3:]):  # Выясняем, равны ли суммы первой и второй половины чисел списка
        return True
    else:
        return False


print('Задача 3. Счастливый ли билет с номером 123006:', lucky_ticket(123006))
print('Задача 3. Счастливый ли билет с номером 12321:', lucky_ticket(12321))
print('Задача 3. Счастливый ли билет с номером 436751:', lucky_ticket(436751))

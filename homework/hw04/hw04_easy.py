# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили


def convert(km):
    miles = km * 1.609
    print(miles, 'миль')


print('Задача 1: ', end='')
convert(23)

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    left_sum = ticket_number[0] + ticket_number[1] + ticket_number[2]
    right_sum = ticket_number[3] + ticket_number[4] + ticket_number[5]
    if left_sum == right_sum:
        return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

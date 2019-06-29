from random import randint
import re

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# решение с помощью re
print('-------------------\nЗадание 1:\n'
      'Вывести символы в нижнем регистре, которые находятся вокруг 1 или более символов в верхнем регистре.\n'
      '\nРешение с помощью re:')
print(re.findall(r'[a-z]+', line))


# решение без re
def without_re_1(string: str) -> list:
    lowercase = []  # список, куда будем добавлять строчные буквы
    switch = 1  # переключатель - индикатор партии строчных (0) или заглавных (1) букв
    list_i = 0  # индекс для создания вложенных списков с партиями строчных букв
    for id_ch, ch in enumerate(string):
        if ch.islower() and switch == 1:  # если буква строчная и перед ней была заглавная -
            lowercase.append([])  # создаём новый вложенный список
            lowercase[list_i].append(ch)  # добавляем туда эту букву
            switch = 0  # переключатель в положение "строчные"
        elif ch.islower() and switch == 0:  # если строчная и перед ней были строчные
            lowercase[list_i].append(ch)  # просто добавляем в последний вложенный список
        elif ch.isupper() and id_ch < len(line) - 1 and line[id_ch + 1].islower():
            # если же буква заглавная, и не последняя в списке, а так же следующая буква - строчная
            list_i += 1  # индекс списка увеличиваем на один, чтобы следующая строчная попала в новый вложенный список
            switch = 1  # свитч устанавливаем в положение "заглавные"
        else:  # если же буква заглавная, без других условий
            switch = 1  # свитч устанавливаем в положение "заглавные"

    return [''.join(x) for x in lowercase]


print('Решение без re:')
print(without_re_1(line), '\n')


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# решение с помощью re
print('-------------------'
      '\nЗадание 2: Вывести символы в верхнем регистре, слева от которых находятся два символа в нижнем регистре,'
      'а справа - два символа в верхнем регистре.\n'
      '\nРешение с помощью re:')
print(re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2))


# решение без re
def without_re_2(string: str) -> list:
    result_list = []  # список, куда будем добавлять списки с нужными совпадениями
    list_i = 0  # итератор - индекс для обращения к спискам совпадений внутри основного списка
    switch_up = 0  # индикатор совпадения - серии букв, которые подходят под условия
    for index in range(2, len(string) - 3):  # отбрасываем 2 первые и последние буквы, чтобы не выйти за пределы списка
        if string[index].isupper():  # проходясь по строке, определяем, является ли буква заглавной
            if switch_up == 0:  # и если индикатор совпадения был на нуле - проверяем совпадение (строка кода ниже)
                if string[index - 2: index].islower() and string[index + 1: index + 3].isupper():
                    result_list.append([])  # если совпадение возникло - создаем новый список
                    result_list[list_i].append(string[index])  # добавляем букву в этот список
                    list_i += 1  # увеличиваем индекс списков совпадений
                    switch_up = 1  # переводим индикатор совпадения во "вкл"
            elif string[index + 1: index + 3].isupper():  # если нет признака того, что заглавные буквы закончатся
                result_list[list_i - 1].append(string[index])  # добавляем их в последний список-совпадение
            else:
                switch_up = 0  # если же через 2 буквы есть строчная буква - индикатор совпадения "выкл"
        else:
            switch_up = 0  # если буква строчная - индикатор совпадения "выкл"

    result_list = [''.join(x) for x in result_list]  # объединяем списки списков в строки, получая в итоге список строк

    return result_list


print('Решение без re:')
print(without_re_2(line_2), '\n')


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

with open('file.txt', 'w') as f:  # открываем файл на запись и записываем туда произвольное 2500-значное число
    f.write(str(randint(10**2499, 10**2500 - 1)))

with open('file.txt', 'r') as f:  # открываем файл на чтение
    number = f.readline()  # читаем первую строку - строку с записанным ранее числом
    nums_list = list()  # создаём список, в котором будем хранить все последовательности одинаковых цифр
    for i in range(0, 10):  # для каждой цифры в десятичном исчислении
        long_num = re.findall('{}+'.format(int(i)), str(number))  # находим её последовательности
        for el in long_num:  # каждую последовательность из списка последовательностей
            nums_list.append(int(el))  # добавляем в общий список последовательностей

print('--------------------\nЗадание 3:\nНапишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)'
      '\nпроизвольными целыми цифрами, в результате в файле должно быть 2500-значное произвольное число.\n'
      'Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле.\n')
print('Самая длинная последовательность:', max(nums_list))  # выводим максимально длинное и самое большое число

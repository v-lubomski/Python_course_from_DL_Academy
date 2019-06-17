import os
import sys
import shutil
import re

# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:


def avg(a, b):
    """
    Вернуть среднее геометрическое чисел 'a' и 'b'.
    :param a: int или float
    :param b: int или float
    :return: float
    """
    return (a * b) ** 0.5


try:
    a = float(input("a = "))
    b = float(input("b = "))
except ValueError as err:
    print('Ошибка: {}. Проверьте введенные числа.'.format(err))
except Exception as err:
    print('Ошибка: {}'.format(err))
else:
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))


# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Создаём в текущей директории папки dir_1 - dir_9'
for i in range(1, 10):
    d = 'dir_{}'.format(i)
    if not os.path.isdir(d):
        os.mkdir(d)
    else:
        print('Папка {} не может быть создана, так как уже существует в текущем каталоге'.format(d))

# Удаляем созданные папки
for i in range(1, 10):
    d = 'dir_{}'.format(i)
    if os.path.isdir(d):
        os.rmdir(d)
    else:
        print('Папка {} не может быть удалена, так как  отсутствует в текущем каталоге'.format(d))


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

for each in os.listdir(os.getcwd()):
    if os.path.isdir(each):
        print(each)


# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

my_file = sys.argv[0]
my_file_ext = re.findall(r'.\w+$', sys.argv[0])[0]
my_file_name = my_file.replace(my_file_ext, '')
shutil.copyfile(my_file, '{}_copy{}'.format(my_file_name, my_file_ext))

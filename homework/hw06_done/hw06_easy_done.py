import os
import sys
import shutil
import re

if __name__ == '__main__':
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


    print('----------\nЗадача 1.')
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

    print('----------\nЗадача 2.\nСоздаём в текущей директории папки dir_1 - dir_9')
    for i in range(1, 10):
        d = 'dir_{}'.format(i)
        if not os.path.isdir(d):
            os.mkdir(d)
        else:
            print('Папка {} не может быть создана, так как уже существует в текущем каталоге'.format(d))

    print('Удаляем созданные папки')
    for i in range(1, 10):
        d = 'dir_{}'.format(i)
        if os.path.isdir(d):
            os.rmdir(d)
        else:
            print('Папка {} не может быть удалена, так как  отсутствует в текущем каталоге'.format(d))

    # Задача-3:
    # Напишите скрипт, отображающий папки текущей директории.
    def show_folders():
        number_of_dirs = 0
        for each in os.listdir(os.getcwd()):
            if os.path.isdir(each):
                print(each)
                number_of_dirs += 1
        if number_of_dirs == 0:
            print('Нет папок в текущей директории')


    print('----------\nЗадача 3.\nПапки текущей директории:')
    show_folders()

    # Задача-4:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
    print('----------\nЗадача 4.\nСоздаём копию файла, из которого запущен данный скрипт.')
    my_file = sys.argv[0]
    my_file_ext = re.findall(r'.\w+$', sys.argv[0])[0]
    my_file_name = my_file.replace(my_file_ext, '')
    shutil.copyfile(my_file, '{}_copy{}'.format(my_file_name, my_file_ext))


# ----------------------------------------------------------------------------------- #
# функции для hw06_easy

# 1. Перейти в папку
def go_to_folder(folder_name):
    """
    Переходит в указанную в виде аргумента папку
    :param folder_name: название папки
    :return:
    """
    if os.path.isdir(folder_name):
        os.chdir(folder_name)
        print('Теперь ты в папке {}'.format(folder_name))
    else:
        print('Невозможно перейти в папку {}, так как она отсутствует в текущей директории'.format(folder_name))


# 2. Просмотреть содержимое текущей папки
def show_all():
    """
    Выводит содержимое текущей директории через print
    """
    for each in os.listdir(os.getcwd()):
        print(each)
    if not os.listdir(os.getcwd()):
        print('Текущая директория пуста')


# 3. Удалить папку
def del_folder(folder_name):
    """
    Удаляет указанную в виде аргумента папку
    :param folder_name: название папки
    :return:
    """
    if os.path.isdir(folder_name):
        shutil.rmtree(folder_name)
        print('Папка {} удалена'.format(folder_name))
    else:
        print('Невозможно удалить папку {}, так как она отсутствует в текущей директории'.format(folder_name))


# 4. Создать папку
def create_folder(folder_name):
    """
    Создаёт указанную в виде аргумента папку
    :param folder_name: название папки
    :return:
    """
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
        print('Папка {} создана'.format(folder_name))
    else:
        print('Невозможно создать папку {}, так как она уже присутствует в текущей директории'.format(folder_name))

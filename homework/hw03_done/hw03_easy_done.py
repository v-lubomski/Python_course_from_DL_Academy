# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['apple', 'banana', 'kiwi', 'watermelon', 'Dattelpflaume']
most_len_word = len(max(fruits, key=lambda f: len(f)))

for fruit in fruits:
    print('{}. {:>{most_len_word}}'.format(fruits.index(fruit) + 1, fruit, most_len_word=most_len_word))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

for el in list2:
    if el in list1:
        list1.remove(el)

print(list1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list_of_num = [1, 22, 345, 5, 6, 778, 453, 221, 3]
new_list = []

for i in list_of_num:
    if i % 2 == 0:
        new_list.append(i/4)
    else:
        new_list.append(i * 2)

print(new_list)

from random import randint
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

my_list = [1, 2, 4, 0]
print('Задание 1.\nПервый список: ', my_list)
squared_list = [x ** 2 for x in my_list]
print('Второй список, элементы которого - квадраты элементов первого списка: ', squared_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ['apple', 'tangerine', 'orange', 'papaya', 'mango']
fruits2 = ['orange', 'pear', 'lemon', 'papaya', 'mango', 'apricot', 'banana']
print('\nЗадание 2. Даны два списка фруктов:\nПервый: {}\nВторой: {}'.format(fruits1, fruits2))
common_fruits = [f for f in fruits1 if f in fruits2]
print('Находим список фруктов, присутствующих в обоих исходных списках:\n{}\n'.format(common_fruits))

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

nums = [randint(-1000, 1000) for x in range(15)]
print('Задание 3.\nДан список, заполненный произвольными числами:\n{}'.format(nums))
nums2 = [x for x in nums if x > 0 and x % 3 == 0 and x % 4 != 0]
print('Получаем список из элементов исходного, удовлетворяющих следующим условиям:\n'
      '1) Элемент кратен 3\n'
      '2) Элемент положительный\n'
      '3) Элемент не кратен 4\n{}'.format(nums2))

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
from random import randint
nums = [randint(-1000, 1000) for x in range(15)]
print(nums)
nums2 = [x for x in nums if x > 0 and x % 3 == 0 and x % 4 != 0]
print(nums2)

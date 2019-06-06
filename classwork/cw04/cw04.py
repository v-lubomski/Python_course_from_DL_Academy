
def amount(param1, param2):
    """
    Считает сумму двух параметров
    :param param1: может быть int или str
    :param param2: может быть int или str
    :return: возврачает число - сумму param1 и param2
    """
    if not isinstance(param1, int):
        param1 = int(param1)
    if not isinstance(param2, int):
        param2 = int(param2)
    return param1 + param2


my_list = ['1', '2,', '3', 4, 5, '6']
my_list2 = []
for i in range(len(my_list), 2):
    my_list2.append(amount(my_list[i], my_list[i + 1]))
print(my_list2)

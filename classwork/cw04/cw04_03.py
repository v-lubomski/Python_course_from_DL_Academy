def average(*args):
    amount = 0
    print(args)
    for el in args:
        amount += el
    return amount / len(args)


print(average(1, 2, 3, 4, 5, 6, 7))

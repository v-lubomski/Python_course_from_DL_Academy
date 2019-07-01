doc = {'first_name': 'Vasily',
       'last_name': 'Petrov',
       'age': 23}

for key, val in doc.items():
    print('{} - {}'.format(key, val))

doc['is_archived'] = False

print(doc)

# почитать про односвязные списки
# проверить время выполнения перебора очень большой последовательности через for и while
# print писать чаще с помощью format
# почитать про распаковку (кортежа) a, b = b, a
# посмотреть слайд про множества

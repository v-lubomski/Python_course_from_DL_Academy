def helloer(**kwargs):
    age = kwargs.get('age', None)
    if age:
        print('Hello, {} {}, которому {}'.format(kwargs['first_name'], kwargs['last_name'], kwargs['age']))
    else:
        print('Hello, {} {}'.format(kwargs['first_name'], kwargs['last_name']))


man = {'first_name': 'Vasya', 'last_name': 'Pupkin', 'age': 43}
helloer(**man)

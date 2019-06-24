# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class People:
    def __init__(self, name):
        self.name = name


class Student(People):
    def __init__(self, name, classroom, *parents):
        super().__init__(name)
        self.__parents = parents
        self.classroom = classroom

    @property
    def short_name(self):
        name_list = self.name.split(' ')
        return name_list[0] + ' {}.'.format(name_list[1][0]) + '{}.'.format(name_list[2][0])

    @property
    def objects(self):
        return [x.subject for x in self.classroom.teachers]

    @property
    def parents(self):
        return [x.name for x in self.__parents]


class Teacher(People):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


class ClassRoom:
    def __init__(self, name, *teachers):
        self.name = name
        self.teachers = teachers


class School:
    def __init__(self, classrooms_dir):
        self.__classrooms = classrooms_dir

    @property
    def classrooms(self):
        return [x.name for x in self.__classrooms.values()]


teachers = {'Оклахомов ИЖ': Teacher('Оклахомов Ильнур Жогбехметович', 'Математика'),
            'Шлюпов ТФ': Teacher('Шлюпов Теодор Франклович', 'ОБЖ'),
            'Теслов НВ': Teacher('Теслов Никола Васильевич', 'Литература')}

classrooms = {'2A': ClassRoom('2А', teachers['Оклахомов ИЖ'], teachers['Шлюпов ТФ'], teachers['Теслов НВ']),
           '3Б': ClassRoom('3Б', teachers['Шлюпов ТФ'], teachers['Теслов НВ']),
           '4В': ClassRoom('4В', teachers['Теслов НВ'])}

school = School(classrooms)

parents = {'Иванов ИИ': People('Иванов Иван Иванович'),
           'Иванова НА': People('Иванова Надежда Алексеевна'),
           'Надеждина НН': People('Надеждина Надежда Надеждовна'),
           'Романов РР': People('Романов Роман Романович'),
           'Романова ОА': People('Романова Ольга Александровна')}

students = {'Иванов ИИ': Student('Иванов Илья Иванович', classrooms['4В'], parents['Иванов ИИ'], parents['Иванова НА']),
            'Надеждин СИ': Student('Надеждин Сурат Ибрагимович', classrooms['2A'], parents['Надеждина НН']),
            'Романов ЦЦ': Student('Романов Царь Царевич', classrooms['3Б'], parents['Романов РР'], parents['Романова ОА'])}


# 1. Получить полный список всех классов школы
print(school.classrooms)

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
print([st.short_name for st in students.values() if st.classroom.name == '2А'])

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
print(students['Романов ЦЦ'].objects)

# 4. Узнать ФИО родителей указанного ученика
print(students['Надеждин СИ'].parents)

# 5. Получить список всех Учителей, преподающих в указанном классе
print([x.name for x in classrooms['3Б'].teachers])

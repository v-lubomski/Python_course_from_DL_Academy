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
        """
        :param name: имя студента
        :param classroom: класс, в котором он учится
        :param parents: родители студента (может не быть, или может быть несколько)
        """
        super().__init__(name)
        self.__parents = parents
        self.classroom = classroom

    def get_short_name(self):
        """
        Получаем ФИО студента в сокращённом виде
        :return: строка вида "Фамилия И.О"
        """
        name_list = self.name.split(' ')
        return name_list[0] + ' {}.'.format(name_list[1][0]) + '{}.'.format(name_list[2][0])

    @property
    def subjects(self):
        """
        Достаём названия предметов класса в котором учится студент
        :return: список названий предметов студента
        """
        return [x.name for x in self.classroom.subjects]

    @property
    def parents(self):
        """
        Достаём из экземпляров родителей студента их имена
        :return: список имён родителей студента
        """
        return [x.name for x in self.__parents]


class Teacher(People):
    def __init__(self, name):
        super().__init__(name)


class Subject:
    """Класс предмета"""
    def __init__(self, name, teacher):
        """
        :param name: название предмета
        :param teacher: экземпляр учителя, который ведёт предмет
        """
        self.name = name
        self.teacher = teacher


class ClassRoom:
    def __init__(self, name, *subjects):
        """
        Класс (школьный)
        :param name: название ("10А")
        :param subjects: экземпляры предметов, которые преподаются в классе
        """
        self.name = name
        self.subjects = subjects


class School:
    def __init__(self, classrooms_dict):
        """
        :param classrooms_dict: словарь с классами, которые существуют в школе
        """
        self.__classrooms = classrooms_dict

    @property
    def classrooms(self):
        """
        достаём названия классов из списка значений словаря классов
        :return: список названий классов
        """
        return [x.name for x in self.__classrooms.values()]


subjects = {'math': Subject('Математика', Teacher('Оклахомов Ильнур Жогбехметович')),
            'obzh': Subject('ОБЖ', Teacher('Шлюпов Теодор Франклович')),
            'lit': Subject('Литература', Teacher('Теслов Никола Васильевич'))}

teachers = {'Оклахомов ИЖ': Teacher('Оклахомов Ильнур Жогбехметович'),
            'Шлюпов ТФ': Teacher('Шлюпов Теодор Франклович'),
            'Теслов НВ': Teacher('Теслов Никола Васильевич')}

classrooms = {'2A': ClassRoom('2А', subjects['math'], subjects['obzh'], subjects['lit']),
              '3Б': ClassRoom('3Б', subjects['obzh'], subjects['math']),
              '4В': ClassRoom('4В', subjects['lit'])}

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
print([st.get_short_name() for st in students.values() if st.classroom.name == '2А'])

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
print(students['Романов ЦЦ'].subjects)

# 4. Узнать ФИО родителей указанного ученика
print(students['Надеждин СИ'].parents)

# 5. Получить список всех Учителей, преподающих в указанном классе
print([x.teacher.name for x in classrooms['3Б'].subjects])

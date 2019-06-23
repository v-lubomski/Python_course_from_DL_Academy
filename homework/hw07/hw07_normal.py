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
    def __init__(self, name, father_name, surname):
        self.name = name
        self.surname = surname
        self.patronymic = father_name

    @property
    def full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname

    @property
    def short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())


class Student(People):
    def __init__(self, name, father_name, surname, mom, dad, school_class):
        People.__init__(self, name, father_name, surname)
        self.mom = mom
        self.dad = dad
        self.school_class = school_class


class Teacher(People):
    def __init__(self, name, father_name, surname, subject):
        People.__init__(self, name, father_name, surname)
        self.subject = subject


class ClassRooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachers_dict = {t.subject: t for t in teachers}


teachers = [Teacher('Иван', 'Иванович', 'Иванов', 'Математика'),
            Teacher('Петр', 'Петрович', 'Петров', 'Литература'),
            Teacher('Сидор', 'Сидорович', 'Сидоров', 'Физика'),
            Teacher('Дмитрий', 'Дмитриевич', 'Дмитриев', 'История'),
            Teacher('Никита', 'Никитиевич', 'Никишин', 'Биология')]
classes = [ClassRooms('11 А', [teachers[0], teachers[1], teachers[2]]),
           ClassRooms('11 Б', [teachers[1], teachers[3], teachers[4]]),
           ClassRooms('10 А', [teachers[3], teachers[1], teachers[0]])]
parents = [People('Семен', 'Семенович', 'Семенов'),
           People('Светлана', 'Савельевна', 'Семенова'),
           People('Роман', 'Романович', 'Романов'),
           People('Римма', 'Романовна', 'Романова'),
           People('Сергей', 'Сергеевич', 'Сергеев'),
           People('Юлия', 'Викторвна', 'Сергеева')]
students = [Student('Игорь', 'Cеменович', 'Семенов', parents[0], parents[1], classes[0]),
            Student('Ольга', 'Романова', 'Романова', parents[2], parents[3], classes[1]),
            Student('Александр', 'Сергеевич', 'Сергеев', parents[4], parents[5], classes[2])]
print('Список классов в школе: ')
for f in classes:
    print(f.class_room)

for f in classes:
    print('Учителя, преподающие в {} классе:'.format(f.class_room))
    for teacher in classes[0].teachers_dict.values():
        print(teacher.full_name)
for f in classes:
    print("Ученики в классе {}:".format(f.class_room))
    for st in students:
        print(st.short_name)

class Student:
    def init(self, name: str, group: int, progress: tuple):
        self.name = name
        self.group = group
        self.progress = progress
    def get_name(self):
        return self.name
    def get_group(self):
        return self.group
    def get_progress(self):
        return self.progress
    
    @staticmethod
    def show_list_of_students(st_list):
        st_list.sort()
        for person in st_list:
            print(person[0], person[1])


    @staticmethod
    def low_progressed_students(lst_of_stdnts):
            for i in lst_of_stdnts:
                if i[2] < 4:
                    print(f'{i[0]}, средний балл -  {i[2]}')



count_of_students = int(input('Сколькоих студентов хотите внести в базу? '))
names = []
groups = []
progresses = []


def count_prog(lst):
    sum = 0
    for i in lst:
        sum += i
    sum //= len(lst)
    return sum

i = 0
while i < count_of_students:
    n = input('Введите фамилию студента: ').capitalize()
    g = int(input('Введите номер группы: '))
    p = list(map(int, input('Введите оценки через пробел: ').split()))
    average_progress = count_prog(p)
    s = Student(n, g, average_progress)
    names.append(s.get_name())
    groups.append(s.get_group())
    progresses.append(s.get_progress())
    students = list(zip(names, groups, progresses))
    i += 1

print('Список студентов и номера групп: ')
Student.show_list_of_students(students)
print()
print('Список студентов с низкими оценками: ')
Student.low_progressed_students(students)
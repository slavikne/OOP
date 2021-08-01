# создание класса Student
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
#  метод добавление курса
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
 # метод выставление оценки лектору
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
# метод расчитывает среднюю оценку студента за домашнюю работу
    def average_rating(self, dict):
        summ = 0
        count = 0
        for grades_course in dict.values():
            for grade in grades_course:
                summ += int(grade)
                count += 1
        if count == 0:
            return 0
        else:
            average = summ/count
            return average

# Перегрузка метода __str__ для класса Student
    def __str__(self):
         res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задание: {self.average_rating(self.grades)}\n' \
               f'Курсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n'
         return res

# метод позволяет сравнивать студентов по их средним оценкам
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_rating(self.grades) < other.average_rating(other.grades)

# Создание класса Mentor
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
# метод выставления оценок студентам
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
# создание класса Lecturer::Mentor
class Lecturer(Mentor):
    def __init__(self,  name, surname):
        super().__init__(name, surname)
        self.grades = {}
# метод расчитывает средние оценки лектора за лекции
    def average_rating(self, dict):
        summ = 0
        count = 0
        for grades_course in dict.values():
            for grade in grades_course:
                summ += int(grade)
                count += 1
        if count == 0:
            return 0
        else:
            average = summ / count
            return average
# Перегрузка метода __str__ для класса Lecturer
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating(self.grades)}\n'
        return res
# метод позволяет сравнивать лекторов  по их средним оценкам за лекции
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_rating(self.grades) < other.average_rating(other.grades)
# создание класса Reviewer::Mentor
class Reviewer(Mentor):
# метод выставление оценок студентам :: Mentor
    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)
# Перегрузка метода __str__ для класса Reviewer
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return res


student_ruoy = Student('Ruoy', 'Eman', 'your_gender')
student_roy = Student('Roy', 'Join', 'your_gender')
student_ruoy.courses_in_progress += ['Python', 'GIT']
student_roy.courses_in_progress += ['Python', 'GIT']
student_ruoy.add_courses('Введение в программирование')
student_roy.add_courses('Введение в программирование')
reviewer_stanly = Reviewer('Stanly', 'Kubric')
reviewer_mike = Reviewer('Mike', 'Morovich')
lecturer_samanta = Lecturer('Samanta', 'Downy')
lecturer_barbara = Lecturer('Barbara', 'Harbara')
reviewer_stanly.courses_attached += ['Python',]
reviewer_mike.courses_attached += ['GIT']
lecturer_samanta.courses_attached += ['Python', 'GIT']
lecturer_barbara.courses_attached += ['GIT', 'Python']
student_ruoy.rate_lecturer(lecturer_samanta, 'Python', 9)
student_ruoy.rate_lecturer(lecturer_samanta, 'Python', 10)
student_ruoy.rate_lecturer(lecturer_samanta, 'Python', 8)
student_ruoy.rate_lecturer(lecturer_samanta, 'GIT', 9)
student_ruoy.rate_lecturer(lecturer_samanta, 'GIT', 10)
student_ruoy.rate_lecturer(lecturer_samanta, 'GIT', 8)
student_roy.rate_lecturer(lecturer_barbara, 'GIT', 7)
student_roy.rate_lecturer(lecturer_barbara, 'GIT', 8)
student_roy.rate_lecturer(lecturer_barbara, 'GIT', 6)
student_roy.rate_lecturer(lecturer_barbara, 'Python', 7)
student_roy.rate_lecturer(lecturer_barbara, 'Python', 8)
student_roy.rate_lecturer(lecturer_barbara, 'Python', 6)
reviewer_stanly.rate_hw(student_ruoy, 'Python', 10)
reviewer_stanly.rate_hw(student_ruoy, 'Python', 10)
reviewer_stanly.rate_hw(student_ruoy, 'Python', 10)
reviewer_mike.rate_hw(student_ruoy, 'GIT', 10)
reviewer_mike.rate_hw(student_ruoy, 'GIT', 9)
reviewer_mike.rate_hw(student_ruoy, 'GIT', 10)
reviewer_mike.rate_hw(student_roy, 'GIT', 8)
reviewer_mike.rate_hw(student_roy, 'GIT', 7)
reviewer_mike.rate_hw(student_roy, 'GIT', 7)
reviewer_stanly.rate_hw(student_roy, 'Python', 8)
reviewer_stanly.rate_hw(student_roy, 'Python', 9)
reviewer_stanly.rate_hw(student_roy, 'Python', 7)
if student_ruoy < student_roy:
    print(f'{student_roy.name} - лучший студент\n')
else:
    print(f'{student_ruoy.name} - лучший студент\n')

if lecturer_samanta < lecturer_barbara:
    print(f'{lecturer_samanta.name} - лучший лектор\n')
else:
    print(f'{lecturer_barbara.name} - лучший лектор\n')

print(student_ruoy)
print(student_roy)
print(lecturer_samanta)
print(reviewer_stanly)
print(reviewer_mike)
def average_rating_students(list_students, course):
    summ_rate = 0
    for student in list_students:
        summ_rate += sum(student.grades[course])/ len(student.grades[course])
    aver_rate = summ_rate/len(list_students)
    print(f'Средняя оценка по всем студентам в рамках курса {course}: {aver_rate}\n ')


def average_rating_lecturers(list_lecturers, course):
    summ_rate = 0
    for lecturer in list_lecturers:
        summ_rate += sum(lecturer.grades[course]) / len(lecturer.grades[course])
    aver_rate = summ_rate / len(list_lecturers)
    print(f'Средняя оценка за лекции всех лекторов в рамках курса {course}: {aver_rate}\n ')

students = [student_ruoy, student_roy]
average_rating_students(students,'Python')

lecturers = [lecturer_samanta, lecturer_barbara]
average_rating_lecturers(lecturers,'GIT')



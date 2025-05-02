class AverageGradeMixin:
    """
    Миксин для вычисления средней оценки.
    Этот класс предназначен для добавления функциональности вычисления средней оценки
    к другим классам, таким как Student и Lecturer.
    """
    def get_average_grade(self):
        """
        Вычисляет среднюю оценку.

        Returns:
            float: Средняя оценка или 0, если оценок нет.
        """
        total, count = 0, 0  # Инициализация переменных для хранения суммы оценок и их количества
        for grades in self.grades.values():
            total += sum(grades)  # Суммирование всех оценок из списка оценок
            count += len(grades)  # Подсчет количества оценок
        return total / count if count > 0 else 0  # Возвращает среднюю оценку, если есть оценки, иначе возвращает 0


class Student(AverageGradeMixin):
    """
    Класс, представляющий студента.
    Этот класс хранит информацию о студенте, его курсах и оценках.
    Он также наследует функциональность вычисления средней оценки из AverageGradeMixin.
    """
    all_students = []  # Атрибут класса для хранения всех студентов

    def __init__(self, name, surname, gender):
        """
        Инициализирует объект Student.

        Args:
            name (str): Имя студента.
            surname (str): Фамилия студента.
            gender (str): Пол студента.
        """
        self.name = name  # Имя студента
        self.surname = surname  # Фамилия студента
        self.gender = gender  # Пол студента
        self.finished_courses = []  # Список завершенных курсов
        self.courses_in_progress = []  # Список курсов в процессе изучения
        self.grades = {}  # Словарь для хранения оценок по курсам (ключ - название курса, значение - список оценок)
        Student.all_students.append(self)  # Добавляем каждого нового студента в список всех студентов

    def __str__(self):
        """
        Возвращает строковое представление студента.
        Определяет, что будет выведено при попытке напечатать объект Student.
        """
        completed_courses_str = ', '.join(self.finished_courses) if self.finished_courses else "Нет пройденных курсов"
        in_progress_str = ', '.join(self.courses_in_progress) if self.courses_in_progress else "Нет изучаемых курсов"
        average_grade = self.get_average_grade()  # Вычисление средней оценки с использованием метода из AverageGradeMixin
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Пол: {self.gender}\n" \
               f"Средняя оценка за домашние задания: {average_grade:.2f}\n" \
               f"Курсы в процессе изучения: {in_progress_str}\n" \
               f"Завершенные курсы: {completed_courses_str}"

    def add_course(self, course):
        """
        Добавляет курс в список изучаемых курсов.

        Args:
            course (str): Название курса.
        """
        self.courses_in_progress.append(course)  # Добавление курса в список courses_in_progress

    def finish_course(self, course):
        """
        Добавляет курс в список завершенных курсов.

        Args:
            course (str): Название курса.
        """
        self.finished_courses.append(course)  # Добавление курса в список finished_courses
        if course in self.courses_in_progress:  # Проверяем, есть ли курс в списке изучаемых
            self.courses_in_progress.remove(course)  # Удаляем курс из списка изучаемых, если он там есть

    def rate_lecturer(self, lecturer, course, grade):
        """
        Выставляет оценку лектору за лекцию.

        Args:
            lecturer (Lecturer): Лектор, которому выставляется оценка.
            course (str): Название курса.
            grade (int): Оценка (от 1 до 10).
        """
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            # Проверка, является ли lecturer объектом Lecturer, и есть ли курс в списках
            if not isinstance(grade, int):
                raise TypeError("Оценка должна быть целым числом.")  # Выброс исключения, если оценка не целое число
            if not 1 <= grade <= 10:
                raise ValueError("Оценка должна быть от 1 до 10.")  # Выброс исключения, если оценка не в диапазоне от 1 до 10
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]  # Добавление оценки в список оценок лектора по данному курсу
            else:
                lecturer.grades[course] = [grade]  # Создание нового списка оценок, если его еще нет
        else:
            return 'Ошибка'  # Возвращает 'Ошибка', если лектор или курс не соответствуют условиям

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Сравнивать можно только с другим Student")
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Сравнивать можно только с другим Student")
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Сравнивать можно только с другим Student")
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Сравнивать можно только с другим Student")
        return self.get_average_grade() != other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Сравнивать можно только с другим Student")
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Сравнивать можно только с другим Student")
        return self.get_average_grade() >= other.get_average_grade()


class Mentor:
    """
    Базовый класс для наставников (лекторов и проверяющих).
    Этот класс хранит общую информацию о наставниках.
    """
    def __init__(self, name, surname):
        """
        Инициализирует объект Mentor.

        Args:
            name (str): Имя наставника.
            surname (str): Фамилия наставника.
        """
        self.name = name  # Имя наставника
        self.surname = surname  # Фамилия наставника
        self.courses_attached = []  # Список курсов, к которым прикреплен наставник


class Lecturer(Mentor, AverageGradeMixin):
    """
    Класс, представляющий лектора.
    Этот класс наследует от Mentor и добавляет функциональность для хранения оценок лекций.
    Он также использует AverageGradeMixin для вычисления средней оценки.
    """
    all_lecturers = []  # Атрибут класса для хранения всех лекторов

    def __init__(self, name, surname):
        """
        Инициализирует объект Lecturer.

        Args:
            name (str): Имя лектора.
            surname (str): Фамилия лектора.
        """
        super().__init__(name, surname)  # Вызов конструктора родительского класса Mentor
        self.grades = {}  # Словарь для хранения оценок за лекции (ключ - название курса, значение - список оценок)
        Lecturer.all_lecturers.append(self)  # Добавляем каждого нового лектора в список всех лекторов

    def __str__(self):
        """
        Возвращает строковое представление лектора.
        Определяет, что будет выведено при попытке напечатать объект Lecturer.
        """
        courses_str = ', '.join(self.courses_attached) if self.courses_attached else "Не ведет курсов"
        average_grade = self.get_average_grade()  # Вычисление средней оценки с использованием метода из AverageGradeMixin
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Ведет курсы: {courses_str}\n" \
               f"Средняя оценка за лекции: {average_grade:.2f}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнивать можно только с другим Lecturer")
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнивать можно только с другим Lecturer")
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнивать можно только с другим Lecturer")
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнивать можно только с другим Lecturer")
        return self.get_average_grade() != other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнивать можно только с другим Lecturer")
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнивать можно только с другим Lecturer")
        return self.get_average_grade() >= other.get_average_grade()



class Reviewer(Mentor):
    """
    Класс, представляющий проверяющего домашние задания.
    Этот класс наследует от Mentor и добавляет функциональность для выставления оценок студентам.
    """
    def __init__(self, name, surname):
        """
        Инициализирует объект Reviewer.

        Args:
            name (str): Имя проверяющего.
            surname (str): Фамилия проверяющего.
        """
        super().__init__(name, surname)  # Вызов конструктора родительского класса Mentor

    def rate_hw(self, student, course, grade):
        """
        Выставляет студенту оценку за домашнее задание.

        Args:
            student (Student): Студент, которому выставляется оценка.
            course (str): Название курса.
            grade (int): Оценка.
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            # Проверка, является ли student объектом Student, и есть ли курс в списках
            if course in student.grades:
                student.grades[course] += [grade]  # Добавление оценки в список оценок студента по данному курсу
            else:
                student.grades[course] = [grade]  # Создание нового списка оценок, если его еще нет
        else:
            return 'Ошибка'  # Возвращает 'Ошибка', если студент или курс не соответствуют условиям

    def __str__(self):
        """
        Возвращает строковое представление проверяющего.
        Определяет, что будет выведено при попытке напечатать объект Reviewer.
        """
        courses_str = ', '.join(self.courses_attached) if self.courses_attached else "Не проверяет курсы"
        return f"Имя: {self.name}, Фамилия: {self.surname}, Проверяет курсы: {courses_str}"


def calculate_average_hw_grade_for_course(students, course):
    """
    Подсчитывает среднюю оценку за домашние задания по всем студентам в рамках конкретного курса.

    Args:
        students (list): Список объектов Student.
        course (str): Название курса.

    Returns:
        float: Средняя оценка или 0, если студентов нет или нет оценок по курсу.
    """
    total_grades = 0  # Инициализация переменной для хранения суммы оценок
    total_count = 0  # Инициализация переменной для хранения количества оценок
    for student in students:
        if course in student.grades:  # Проверка, есть ли оценки по данному курсу у студента
            total_grades += sum(student.grades[course])  # Суммирование оценок студента по данному курсу
            total_count += len(student.grades[course])  # Подсчет количества оценок студента по данному курсу
    return total_grades / total_count if total_count > 0 else 0  # Возвращает среднюю оценку, если есть оценки, иначе 0


def calculate_average_lecture_grade_for_course(lecturers, course):
    """
    Подсчитывает среднюю оценку за лекции всех лекторов в рамках курса.

    Args:
        lecturers (list): Список объектов Lecturer.
        course (str): Название курса.

    Returns:
        float: Средняя оценка или 0, если лекторов нет или нет оценок по курсу.
    """
    total_grades = 0  # Инициализация переменной для хранения суммы оценок
    total_count = 0  # Инициализация переменной для хранения количества оценок
    for lecturer in lecturers:
        if course in lecturer.grades:  # Проверка, есть ли оценки по данному курсу у лектора
            total_grades += sum(lecturer.grades[course])  # Суммирование оценок лектора по данному курсу
            total_count += len(lecturer.grades[course])  # Подсчет количества оценок лектора по данному курсу
    return total_grades / total_count if total_count > 0 else 0  # Возвращает среднюю оценку, если есть оценки, иначе 0


# Создаем экземпляры классов
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.add_course('Python')  # Используем add_course
student1.add_course('Git')
student1.finish_course('Введение в программирование')  # Используем finish_course

student2 = Student('John', 'Doe', 'male')
student2.add_course('Python')
student2.finish_course('Основы программирования')

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Jane', 'Smith')
lecturer2.courses_attached += ['Python', 'Git']

reviewer1 = Reviewer('Other', 'Buddy')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Mike', 'Johnson')
reviewer2.courses_attached += ['Python']

# Вызываем методы и взаимодействуем с экземплярами
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 8)

student2.rate_lecturer(lecturer1, 'Python', 7)
student2.rate_lecturer(lecturer1, 'Python', 9)

student1.rate_lecturer(lecturer2, 'Git', 10)
student1.rate_lecturer(lecturer2, 'Git', 10)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 7)

reviewer2.rate_hw(student1, 'Python', 9)


# Выводим информацию об экземплярах
print(student1)  # Вывод информации о student1 с использованием метода __str__
print(student2)  # Вывод информации о student2 с использованием метода __str__
print(lecturer1)  # Вывод информации о lecturer1 с использованием метода __str__
print(lecturer2)  # Вывод информации о lecturer2 с использованием метода __str__
print(reviewer1)  # Вывод информации о reviewer1 с использованием метода __str__
print(reviewer2)  # Вывод информации о reviewer2 с использованием метода __str__

# Выводим списки всех студентов и лекторов
print("Все студенты:")
for student in Student.all_students:
    print(student)  # Вывод информации о каждом студенте в списке с использованием метода __str__

print("Все лекторы:")
for lecturer in Lecturer.all_lecturers:
    print(lecturer)  # Вывод информации о каждом лекторе в списке с использованием метода __str__

# Сравниваем студентов и лекторов
print(f"Сравнение студентов: student1 < student2 = {student1 < student2}")
print(f"Сравнение лекторов: lecturer1 < lecturer2 = {lecturer1 < lecturer2}")

# Вызываем функции для подсчета средних оценок
python_hw_average = calculate_average_hw_grade_for_course([student1, student2], 'Python')
print(f"Средняя оценка за ДЗ по Python: {python_hw_average:.2f}")

python_lecture_average = calculate_average_lecture_grade_for_course([lecturer1, lecturer2], 'Python')
print(f"Средняя оценка за лекции по Python: {python_lecture_average:.2f}")

git_lecture_average = calculate_average_lecture_grade_for_course([lecturer1, lecturer2], 'Git')
print(f"Средняя оценка за лекции по Git: {git_lecture_average:.2f}")




class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        completed_courses_str = ', '.join(self.finished_courses) if self.finished_courses else "Нет пройденных курсов"
        in_progress_str = ', '.join(self.courses_in_progress) if self.courses_in_progress else "Нет изучаемых курсов"
        average_grade = self.get_average_grade()
        return f"Имя: {self.name}, Фамилия: {self.surname}, Пол: {self.gender}, Средняя оценка за домашние задания: {average_grade:.2f}, Курсы в процессе изучения: {in_progress_str}, Завершенные курсы: {completed_courses_str}"

    def rate_lecturer(self, lecturer, course, grade):
        """
        Выставляет оценку лектору за лекцию.

        Args:
            lecturer (Lecturer): Лектор, которому выставляется оценка.
            course (str): Название курса.
            grade (int): Оценка (от 1 до 10).
        """
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if not isinstance(grade, int):
                raise TypeError("Оценка должна быть целым числом.")
            if not 1 <= grade <= 10:
                raise ValueError("Оценка должна быть от 1 до 10.")
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        """
        Вычисляет среднюю оценку за домашние задания для студента.

        Returns:
            float: Средняя оценка или 0, если оценок нет.
        """
        total_grades = 0
        total_count = 0
        for grades_list in self.grades.values():
            total_grades += sum(grades_list)
            total_count += len(grades_list)
        return total_grades / total_count if total_count > 0 else 0

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
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        courses_str = ', '.join(self.courses_attached) if self.courses_attached else "Не ведет курсов"
        average_grade = self.get_average_grade()
        return f"Имя: {self.name}, Фамилия: {self.surname}, Ведет курсы: {courses_str}, Средняя оценка за лекции: {average_grade:.2f}"

    def get_average_grade(self):
        """
        Вычисляет среднюю оценку за лекции.

        Returns:
            float: Средняя оценка или 0, если оценок нет.
        """
        total_grades = 0
        total_count = 0
        for grades_list in self.grades.values():
            total_grades += sum(grades_list)
            total_count += len(grades_list)
        return total_grades / total_count if total_count > 0 else 0

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
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """
        Выставляет студенту оценку за домашнее задание.

        Args:
            student (Student): Студент, которому выставляется оценка.
            course (str): Название курса.
            grade (int): Оценка.
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
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
    total_grades = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_count += len(student.grades[course])
    return total_grades / total_count if total_count > 0 else 0


def calculate_average_lecture_grade_for_course(lecturers, course):
    """
    Подсчитывает среднюю оценку за лекции всех лекторов в рамках курса.

    Args:
        lecturers (list): Список объектов Lecturer.
        course (str): Название курса.

    Returns:
        float: Средняя оценка или 0, если лекторов нет или нет оценок по курсу.
    """
    total_grades = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    return total_grades / total_count if total_count > 0 else 0


# Создаем экземпляры классов
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('John', 'Doe', 'male')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Основы программирования']

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
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

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




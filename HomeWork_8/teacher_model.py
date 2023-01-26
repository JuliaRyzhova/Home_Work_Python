import csv


def check_lesson(lesson):
    """Проверка на правильность ввода названия урока"""
    study_discipline = ['Математика', 'Русский язык', 'Литература',
                        'Биология', 'География', 'Химия', 'Английский язык']
    if lesson in study_discipline:
        return True
    else:
        return False


def check_surname_student(lesson, surname_student):
    """Проверка на правильность ввода фамилии ученика (для учителя)"""
    with open('HomeWork_8/db.csv', encoding='utf-8', newline='', mode='r') as f:
        data = csv.reader(f,  delimiter=',')
        count = 0
        for line in data:
            if surname_student in line and lesson in line:
                count += 1
                return True
        if count == 0:
            return False


def check_mark(mark):
    """Проверка правильности оценки"""
    if mark in ['2', '3', '4', '5']:
        return True
    else:
        return False


def add_assessment(lesson, surname_student, mark):
    """Добавление новой оценки"""
    with open('HomeWork_8/db.csv', encoding='utf8', newline='', mode='r') as csvfile:
        data = csv.reader(csvfile,  delimiter=',')
        data = list(data)
        for line in data:
            if lesson in line and surname_student in line:
                line[3] = (line[3] + '-' + mark)
                writer = csv.writer(
                    open('HomeWork_8/db.csv', encoding='utf8', newline='', mode='w'))
                writer.writerows(data)


def show_result_adding(lesson, surname_student):
    """Вывод оценок ученика после проставления новой оценки"""
    with open('HomeWork_8/db.csv', encoding='utf8', newline='', mode='r') as csvfile:
        data = csv.reader(csvfile,  delimiter=',')
        for line in data:
            if surname_student in line and lesson in line:
                print(
                    f"{''.join(line[0])}\nУченик: {''.join(line[1])} {''.join(line[2])}\nОценки: {''.join(line[3])}")
                print('______________________________________')


def show_list_lessons():
    """Формирование списка предметов"""
    with open('HomeWork_8/db.csv', encoding='utf-8', newline='', mode='r') as f:
        data = csv.reader(f,  delimiter=',')
        data = list(data)
        lst = []
        print('Список предметов:')
        for line in data[1:]:
            lst.append(line[0])
        lst = set(lst)
        print('\n'.join(lst))


def show_list_students():
    """Формирование списка учеников"""
    with open('HomeWork_8/db.csv', encoding='utf-8', newline='', mode='r') as f:
        data = csv.reader(f,  delimiter=',')
        data = list(data)
        count_students = 13
        lst = []
        print()
        print('Список учеников:')
        for line in data[1:count_students + 1]:
            lst.append(line[1])
            lst.append(line[2])
            print(line[1], line[2])

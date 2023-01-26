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


def add_assessment(lesson, surname_student, mark):
    """Добавление новой оценки"""
    with open('HomeWork_8/db.csv', encoding='utf8', newline='', mode='r') as csvfile:
        data = csv.reader(csvfile,  delimiter=',')
        data = list(data)
        for line in data:
            if lesson in line and surname_student in line:
                # print(type(mark))
                line[3] = (line[3] + '-' + mark)
                # print(type(line[3]))
                # print(line[3])
                writer = csv.writer(
                    open('HomeWork_8/db.csv', encoding='utf8', newline='', mode='w'))
                writer.writerows(data)


def show_result_adding(lesson, surname_student):
    with open('HomeWork_8/db.csv', encoding='utf8', newline='', mode='r') as csvfile:
        data = csv.reader(csvfile,  delimiter=',')
        for line in data:
            if surname_student in line and lesson in line:
                # print('{}\nУченик: {}\nОценки: {}'
                #       .format(''.join(line[0]), ''.join(line[1]), ''.join(line[3])))
                # print('______________________________________')
                print(f"{''.join(line[0])}\nУченик: {''.join(line[1])} {''.join(line[2])}\nОценки: {''.join(line[3])}")
                print('______________________________________')

# les = 'Математика'
# user = 'Захарова'
# ocenka = '3'

# check_surname_student(les, user)

import csv

def check_lesson(lesson):
    """Проверка на правильность ввода названия урока"""
    study_discipline = ['Математика', 'Русский язык', 'Литература', 'Биология', 'География', 'Химия', 'Английский язык']
    if lesson in study_discipline:
        return True
    else:
        print('Такого урока нет. Проверьте правильно ли Вы написали?')


def check_surname_student(lesson, surname_student):
    """Проверка на правильность ввода фамилии ученика (для учителя)"""
    with open('HomeWork_8/db.csv', encoding='utf-8', newline='', mode='r') as f:
        data = csv.reader(f,  delimiter=';')
        count = 0
        for line in data:
            if surname_student in line and lesson in line:
                count +=1
                return True
        if count == 0:
            print('Такого ученика нет!!!')


# def add_new_assessment(lesson, surname_student, assessment):
#     """Добавление новой оценки по конкретному предмету - конкретному ученику"""
#     with open('HomeWork_8/csv.py', encoding='utf-8', newline='', mode='r') as f:
#         data = csv.DictReader(f, delimiter=',')

def update_assessment(file_name= ''):
    with open('HomeWork_8/db.csv', newline="") as f:
        readData = [row for row in csv.DictReader(f)]
        # print(readData)
        readData[0]['Rating'] = '9.4'
        # print(readData)
        readHeader = readData[0].keys()







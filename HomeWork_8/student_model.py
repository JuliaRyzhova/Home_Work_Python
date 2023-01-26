import csv


def chech_your_surname(surname_student):
    """Проверка на правильность ввода фамилии ученика"""
    with open('HomeWork_8/db.csv', encoding='utf-8', newline='', mode='r') as f:
        data = csv.reader(f,  delimiter=',')
        count = 0
        for line in data:
            if surname_student in line:
                count += 1
                return True
        if count == 0:
            return False
 

def show_diary(surname_student):
    """Вывод всех оценок ученика"""
    with open('HomeWork_8/db.csv', encoding='utf8', newline='', mode='r') as csvfile:
        data = csv.reader(csvfile,  delimiter=',')
        print()
        print('Успеваемость ученика: ' + surname_student)
        print()
        for line in data:
            if surname_student in line:
                print('{}\nВаши оценки: {}'
                      .format(''.join(line[0]), ''.join(line[3])))
                print('______________________________________')




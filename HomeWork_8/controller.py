from user_interface import get_role, get_lesson, get_surname_student, get_assessment
from teacher_model import check_lesson, check_surname_student, add_assessment, show_result_adding
from student_model import chech_your_surname, show_diary
from logger import role_logger

surname = ''

def run():
    while True:
        option = get_role()
        role_logger(option)
        if option == '1':
            lesson = get_lesson()
            while check_lesson(lesson) == False:
                print('Нет такого предмета!!! Попробуйте еще раз!')
                print()
                lesson = get_lesson()
            surname = get_surname_student()
            while check_surname_student(lesson, surname) == False:
                print('Нет такого ученика. Попробуйте еще раз!')
                print()
                surname = get_surname_student()
            mark = get_assessment()
            add_assessment(lesson, surname, mark)
            show_result_adding(lesson, surname)
        if option == '2':
            surname = get_surname_student()
            while chech_your_surname(surname) == False:
                print('Неправильно написали фамилию. Попробуйте еще раз!')
                print()
                surname = get_surname_student()
            show_diary(surname)
        if option =='3':
            break

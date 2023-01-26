from user_interface import get_role, get_lesson, get_surname_student, get_assessment
from teacher_model import *
from student_model import chech_your_surname, show_diary
from logger import *


def run():
    while True:
        option = get_role()
        role_logger(option)
        if option == '1':
            show_list_lessons()
            list_lesson_logger()
            lesson = get_lesson()
            input_lesson_logger(lesson)
            while check_lesson(lesson) == False:
                incorrect_lesson_logger(lesson)
                print('Нет такого предмета!!! Попробуйте еще раз!')
                print()
                show_list_lessons()
                list_lesson_logger()
                lesson = get_lesson()
                input_lesson_logger(lesson)
            show_list_students()
            list_student_logger()
            surname = get_surname_student()
            input_surname_logger(surname)
            while check_surname_student(lesson, surname) == False:
                input_surname_logger(surname)
                print('Нет такого ученика. Попробуйте еще раз!')
                print()
                show_list_students()
                list_student_logger()
                surname = get_surname_student()
                input_surname_logger(surname)
            mark = get_assessment()
            while check_mark(mark) == False:
                incorrect_mark_logger(mark)
                print(
                    'Не бывает таких оценок\nМожно поставить 2, 3, 4 или 5 \nПопробуйте еще раз!')
                print()
                mark = get_assessment()
                add_mark_logger(mark)
            input_mark_logger(lesson, surname, mark)
            add_assessment(lesson, surname, mark)
            add_mark_logger()
            show_result_adding(lesson, surname)
            show_result_logger()
        if option == '2':
            role_logger(option)
            show_list_students()
            list_student_logger()
            surname = get_surname_student()
            input_surname_logger(surname)
            while chech_your_surname(surname) == False:
                incorrect_surname_logger(surname)
                print('Нет такого ученика. Попробуйте еще раз!')
                print()
                surname = get_surname_student()
                input_surname_logger(surname)
            show_diary(surname)
        if option == '3':
            exit_program_logger(option)
            break

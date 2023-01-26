from datetime import datetime as dt
from time import time
import csv


def role_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Start programm by role; {}\n'
                   .format(time, data))
        
def list_lesson_logger():
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Showing a list of all lessons\n'
                   .format(time))

def input_lesson_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Lesson selection; {}\n'
                   .format(time, data))

def incorrect_lesson_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Try incorrect lesson selection; {}\n'
                   .format(time, data)) 

def list_student_logger():
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Showing a list of all students\n'
                   .format(time))

def input_surname_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Surname student selection; {}\n'
                   .format(time, data))

def incorrect_surname_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Try incorrect surname student selection; {}\n'
                   .format(time, data)) 

def input_mark_logger(lesson, surname, mark):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Input mark lesson {}; student {}; mark {};\n'
                   .format(time, lesson, surname, mark)) 


def incorrect_mark_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Try incorrect mark add; {}\n'
                   .format(time, data))

def add_mark_logger():
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Mark added\n'
                   .format(time))

def show_result_logger():
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Showing result of addig mark\n'
                   .format(time))

def exit_program_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Exit program; {}\n'
                   .format(time, data)) 

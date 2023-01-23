from datetime import datetime as dt
from time import time
import csv

def operation_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_7/log.csv', encoding='utf8', newline='', mode ='a') as file:
        file.write('{}; Input operation; {}\n'
                   .format(time, data))
        

def searching_data_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_7/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Searching request; {}\n'
                   .format(time, data))
        
def surname_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_7/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Surname input; {}\n'
                   .format(time, data))
        

def name_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_7/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Name input; {}\n'
                   .format(time, data))
        

def phone_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_7/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Phone input; {}\n'
                   .format(time, data))

def description_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_7/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Description input; {}\n'
                   .format(time, data))
        

def create_new_contact_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_7/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Create new contact; {}\n'
                   .format(time, data))
        

def search_contact_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_7/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Try searching contact; {}\n'
                   .format(time, data))
        

def showDB_v1_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_7/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Show data in line; {}\n'
                   .format(time, data))
        

def showDB_v2_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_7/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Show data in column; {}\n'
                   .format(time, data))

from datetime import datetime as dt
from time import time
import csv


def role_logger(data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_8/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; Start programm by role; {}\n'
                   .format(time, data))



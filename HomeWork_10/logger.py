from datetime import datetime as dt
from time import time
import csv
from telegram import Update



def logger_start(update):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_10/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; User id = {}; full name: {}; Bot is started by user\n'
                   .format(time, update.message.from_user.id, update.message.from_user.full_name))
        

def logger_input_data(update, data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_10/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; User id = {}; full name: {}; input example: {}\n'
                   .format(time, update.message.from_user.id, update.message.from_user.full_name, data))
        
def logger_result(update, data):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_10/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; User id = {}; full name: {}; got the result: {}\n'
                   .format(time, update.message.from_user.id, update.message.from_user.full_name, data))
        
def logger_menu(update):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_10/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; User id = {}; full name: {}; called the command "Menu"\n'
                   .format(time, update.message.from_user.id, update.message.from_user.full_name))
        

def logger_next(update):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_10/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; User id = {}; full name: {}; called the command "Next"\n'
                   .format(time, update.message.from_user.id, update.message.from_user.full_name))
        

def logger_exit(update):
    time = dt.now().strftime('%D %H:%M:%S')
    with open('HomeWork_10/log.csv', encoding='utf8', newline='', mode='a') as file:
        file.write('{}; User id = {}; full name: {}; called the command "Cancel", Bot is OFF"\n'
                   .format(time, update.message.from_user.id, update.message.from_user.full_name))
        

        
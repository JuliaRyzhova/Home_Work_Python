import csv


def create_contact(cont_data):
    """Функция добавления нового контакта
    Входящий параметр - список"""
    with open('HomeWork_7/guide.csv', encoding='utf8', newline='', mode='a') as csvfile:
        data = csv.writer(csvfile, delimiter=',')
        data.writerow(cont_data)



def searching_contact(search_request):
    """Функция выводящая только найденные записи по запросу"""
    with open('HomeWork_7/guide.csv', encoding='utf8', newline='', mode='r') as csvfile:
        data = csv.reader(csvfile,  delimiter=',')
        count = 0
        for line in data:
            if search_request in line:
                print('______________________________________')
                print(' '.join(line))
                print('______________________________________')
                count +=1
        if count == 0:
            print('Такого контакта нет!!!')


def show_data_inline():
    """Функция выводящая все записи построчно"""
    with open('HomeWork_7/guide.csv', encoding='utf8', newline='', mode='r') as csvfile:
        data = csv.reader(csvfile,  delimiter=',')
        for line in data:
            print(' '.join(line))
            print('______________________________________')


def show_data_incolumn():
    """Функция выводящая все записи в столбик"""
    with open('HomeWork_7/guide.csv', encoding='utf8', newline='', mode='r') as csvfile:
        data = csv.DictReader(csvfile,  delimiter=',')
        for item in data:
            item = dict(item)
            for k in item:
                print('{}: {}'.format(k, item[k]))
            print('______________________________________')

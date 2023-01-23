
def get_operation():
    print()
    print('Что будем делать со справочником?')
    get = input('Введите 1 - посмотреть все контакты, 2 - найти контакт, 3 - добавить новый контакт ->: ')
    print()
    return get

def get_searching_data():
    search = input('Введите данные для поиска: ').title()
    return search

def get_surname():
    surname = input('Фамилия: ').title()
    return surname

def get_name():
    name = input('Имя: ').title()
    return name

def get_phone():
    phone = input('Номер телефона: ')
    return phone

def get_description():
    description = input('Описание: ').capitalize()
    return description


def get_show_option():
    print()
    print('В каком формате хотите увидеть справочник?')
    print('')
    print('Построчный формат:')
    print('Имя: Фамилия: Номер телефона: Описание: ')
    print('или в ряд')
    print('')
    print('Имя: \nФамилия: \nНомер телефона: \nОписание:\n')
    option = input('Введите 4 - если построчно, 5 - если в ряд ->: ')
    return option




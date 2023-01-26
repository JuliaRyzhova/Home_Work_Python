def get_role():
    print('Добро пожаловать в электронный дневник.\nПредставьтесь, пожалуйста!')
    print()
    role = input(
        'Если Вы учитель, введите 1: \nЕсли Вы ученик, введите 2: \nВыйти из дневника 3: ')
    print()
    return role


def get_lesson():
    lesson = input('Выберете один из предметов: ').capitalize()
    return lesson


def get_surname_student():
    surname = input('Введите фамилию: ').title()
    return surname


def get_assessment():
    assessment = input('Оценка: ')
    print()
    return assessment

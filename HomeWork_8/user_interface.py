def get_role():
    print('Добро пожаловать в электронный дневник.\nПредставьтесь, пожалуйста!')
    print()
    role = input('Если Вы учитель, введите 1: \nЕсли Вы ученик, введите 2: ')
    print()
    return role

def get_lesson():
    lesson = input('Введите название предмета: ').title()
    return lesson

def get_surname_student():
    surname = input('Введите фамилию: ').title()
    return surname

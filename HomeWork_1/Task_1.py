# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def is_weekend(date):
    if date in range(1, 6):
        return 'Ооой, это буднй день. Время работать!'
    elif date == 6 or date == 7:
        return 'Это выходной!!! Можно и отдохнуть :)'
    else:
        print('Неправильное число!')


day = int(input('Введите день недели от 1 до 7: '))
print(is_weekend(day))

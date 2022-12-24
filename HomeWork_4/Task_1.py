# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, 
# сколько указал пользователь(БЕЗ round())

from math import pi
# print(pi)

amount = int(input('Input the count of characters after the comma in "pi": '))

pi = str(pi)
def crop_number(value):
    if value <= 15:
        print(f'Pi with {value} characters after the comma is', end=' ')
        for i in range(value + 2):
            print(pi[i], end ='')
    else:
        print('Your number must be less or equal to 15')

crop_number(amount)

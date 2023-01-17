# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

from random import randint

# Алгоритм игры Человек против человека. Добавила жеребьевку первого хода

total_sweet = 120
take_sweet = 0
player1_sweet = 0
player2_sweet = 0
max_take = 28
min_take = 1

# Функция жеребьевки первого хода


def first_step():
    rnd = randint(1, 2)
    if rnd == 1:
        player1_step()
    else:
        player2_step()

# Логика хода первого игрока


def player1_step():
    global total_sweet
    global take_sweet
    global player1_sweet
    print(f'Ход первого игрока. Сейчас на столе {total_sweet} конфет(ы).')
    take_sweet = int(input('Сколько берете конфет? '))
    print()
    while take_sweet > max_take or take_sweet < min_take or take_sweet > total_sweet:
        take_sweet = int(
            input('Неверное количество конфет. Попробуйте снова: '))
    total_sweet -= take_sweet
    player1_sweet += take_sweet
    if total_sweet > 0:
        player2_step()
    else:
        print('Вы победили!!!!!!!!!!')

# Логика хода второго игрока


def player2_step():
    global total_sweet
    global take_sweet
    global player2_sweet
    print(f'Ход второго игрока. Сейчас на столе {total_sweet} конфет(ы)')
    take_sweet = int(input('Сколько берете конфет? '))
    print()
    while take_sweet > max_take or take_sweet < min_take or take_sweet > total_sweet:
        take_sweet = int(
            input('Неверное количество конфет. Попробуйте снова: '))
    total_sweet -= take_sweet
    player2_sweet += take_sweet
    if total_sweet > 0:
        player1_step()
    else:
        print('Вы победили!!!!!!!!!')


def main():
    print('На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.\nЗа один ход можно забрать не более чем 28 конфет. Победитель - тот, кто оставил на столе 0 конфет.')
    print()
    first_step()


main()

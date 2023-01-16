# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# # Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

from random import randint

# Алгоритм игры Человек против человека.
    
gamer_1 = True
gamer_2 = False

bonbon = 120
max_bon = 28
min_bon = 1

def step_of_play(candies, player_1, player_2):
    if candies >= max_bon:
        step = int(input(f'Вы можете взять от {min_bon} до {max_bon} конфет: '))
        candies -= step
    else:
        step = int(input(f'Вы можете взять от {min_bon} до {candies} конфет: '))
        candies -= step
    return step

def play(player_1, player_2, candies, function):
    while candies > 0:
        if player_1:
            print('Ход первого игрока: ')
            print(f'На столе {candies} конфет(ы)')
            step = step_of_play(candies, player_1, player_2)
            candies -= step
            print()
            player_1, player_2 = False, True
        elif player_2:
            print('Ход второго игрока: ')
            print(f'На столе {candies} конфет(ы)')
            step = step_of_play(candies, player_1, player_2)
            candies -= step
            print()
            player_2, player_1 = False, True
    else:
        if player_1:
            print('Game Over. Победил игрок номер 2')
        elif player_2:
            print('Game Over. Победил игрок номер 1')


play(gamer_1, gamer_2, bonbon, step_of_play)


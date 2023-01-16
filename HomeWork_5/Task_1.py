# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# # Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

from random import randint

# Алгоритм игры Человек против человека.

# def play():
#     player = True
#     bot = False
#     candies = 120
#     while candies > 0:
#         if player == True:
#             print('Ход первого игрока: ')
#             if candies >= 28:
#                 step = int(input('Вы можете взять от 1 до 28 конфет: '))
#                 candies -= step
#             else:
#                 step = int(input(f'Вы можете взять от 1 до {candies} конфет: '))
#                 candies -= step
#             print(f'Игрок взял {step} конфет(ы)')
#             print(f'Осталось {candies} конфет(ы)')
#             print()
#             player = False
#             bot = True
#         else:
#             print('Ход второго игрока: ')
#             if candies >= 28:
#                 step = int(input('Вы можете взять от 1 до 28 конфет: '))
#                 candies -= step
#             else:
#                 step = int(input(f'Вы можете взять от 1 до {candies} конфет: '))
#                 candies -= step
#             print(f'Игрок взял {step} конфет(ы)')
#             print(f'Осталось {candies} конфет(ы)')
#             print()
#             bot = False
#             player = True
#     else:
#         if player == False:
#             print('Game Over. Победил игрок номер 1')
#         elif bot == False:
#             print('Game Over. Победил игрок номер 2')

# play()       


# gamer_1 = True
# gamer_2 = True

# bonbon = 120

# def step_of_play(candies):
#     if candies >= 28:
#         step = int(input('Вы можете взять от 1 до 28 конфет: '))
#         candies -= step
#     else:
#         step = int(input(f'Вы можете взять от 1 до {candies} конфет: '))
#         candies -= step
#     return step


# def play(player, bot, candies, function):
#     while candies > 0:
#         if player == True:
#             print('Ход первого игрока: ')
#             print(f'Игрок взял {step_of_play(bonbon)} конфет')
#             candies -= step_of_play(bonbon)
#             print(f'Осталось {candies} конфет')
#             print()
#             player = False
#             bot = True
#         else:
#             print('Ход второго игрока: ')
#             print(f'Игрок взял {step_of_play(bonbon)} конфет')
#             candies -= step_of_play(bonbon)
#             print(f'Осталось {candies} конфет')
#             print()
#             bot = False
#             player = True
#     else:
#         if player == True:
#             print('Game Over. Победил игрок номер 1')
#         elif bot == True:
#             print('Game Over. Победил игрок номер 2')


# play(gamer_1, gamer_2, bonbon, step_of_play)

# Алгоритм игры Человек против бота.

# def play():
#     player = True
#     bot = False
#     candies = 120
#     while candies > 0:
#         if player == True:
#             print('Ваш ход: ')
#             if candies >= 28:
#                 step = int(input('Вы можете взять от 1 до 28 конфет: '))
#                 candies -= step
#             else:
#                 step = int(
#                     input(f'Вы можете взять от 1 до {candies} конфет: '))
#                 candies -= step
#             print(f'Осталось {candies} конфет(ы)')
#             print()
#             player = False
#             bot = True
#         else:
#             print('Ход бота: ')
#             if candies >= 28:
#                 step = randint(1, 28)
#                 candies -= step
#             else:
#                 step = randint(1, candies)
#                 candies -= step
#             print(f'Бот взял {step} конфет(ы)')
#             print(f'Осталось {candies} конфет(ы)')
#             print()
#             bot = False
#             player = True
#     else:
#         if player == False:
#             print('Поздравляю! Вы победили')
#         elif bot == False:
#             print('Game Over. Победил бот')


# play()


# Алгоритм игры Человек против умного бота.

# def play():
#     player = True
#     bot = False
#     candies = 120
#     while candies > 0:
#         if player == True:
#             print('Ваш ход: ')
#             if candies >= 28:
#                 step = int(input('Вы можете взять от 1 до 28 конфет: '))
#                 candies -= step
#             else:
#                 step = int(input(f'Вы можете взять от 1 до {candies} конфет: '))
#                 candies -= step
#             print(f'Осталось {candies} конфет(ы)')
#             print()
#             player = False
#             bot = True
#         else:
#             print('Ход бота: ')
#             if candies >= 28:
#                 step = 29 - step
#                 candies -= step
#             else:
#                 step = candies
#                 candies -= step
#             print(f'Бот взял {step} конфет(ы)')
#             print(f'Осталось {candies} конфет(ы)')
#             print()
#             bot = False
#             player = True
#     else:
#         if player == False:
#             print('Поздравляю! Вы победили')
#         elif bot == False:
#             print('Game Over. Победил бот')


# play()

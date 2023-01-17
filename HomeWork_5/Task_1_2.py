# Алгоритм игры Человек против глупого бота.
from random import randint

total_sweet = 120
take_sweet = 0
human_sweet = 0
bot_sweet = 0
max_take = 28
min_take = 1

# Функция жеребьевки первого хода


def first_step():
    rnd = randint(1, 2)
    if rnd == 1:
        human_step()
    else:
        bot_step()

# Логика хода первого игрока


def human_step():
    global total_sweet
    global take_sweet
    global human_sweet
    print(f'Ваш ход. Сейчас на столе {total_sweet} конфет(ы).')
    take_sweet = int(input('Сколько берете конфет? '))
    print()
    while take_sweet > max_take or take_sweet < min_take or take_sweet > total_sweet:
        take_sweet = int(
            input('Неверное количество конфет. Попробуйте снова: '))
    total_sweet -= take_sweet
    human_sweet += take_sweet
    if total_sweet > 0:
        bot_step()
    else:
        print('Вы победили!!!!!!')

# Логика хода бота


def bot_step():
    global total_sweet
    global take_sweet
    global bot_sweet
    if total_sweet > max_take:
        take_sweet = randint(min_take, max_take)
    else:
        take_sweet = randint(min_take, total_sweet)
    print(f'Бот взял {take_sweet} конфет(ы)')
    print()
    total_sweet -= take_sweet
    bot_sweet += take_sweet
    if total_sweet > 0:
        human_step()
    else:
        print('Бот выйграл!!!!!!!')


def main():
    print('На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.\nЗа один ход можно забрать не более чем 28 конфет. Победитель - тот, кто оставил на столе 0 конфет.')
    print()
    first_step()


main()

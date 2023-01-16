#  Алгоритм игры Человек против умного бота.

gamer = True
bot = False

bonbon = 120
max_bon = 28
min_bon = 1

def step_of_human(candies, min_bon, max_bon):
    if candies >= max_bon:
        step = int(
            input(f'Вы можете взять от {min_bon} до {max_bon} конфет: '))
        candies -= step
    else:
        step = int(
            input(f'Вы можете взять от {min_bon} до {candies} конфет: '))
        candies -= step
    return step

def play(player, bot, candies, func_1):
    while candies > 0:
        if player:
            print('Ваш ход: ')
            print(f'На столе {candies} конфет(ы)')
            step = step_of_human(candies, min_bon, max_bon)
            candies -= step
            print()
            player, bot = False, True
        elif bot:
            print('Ход бота: ')
            if candies >= max_bon:
                step = min_bon + max_bon - step
                candies -= step
            else:
                step = candies
                candies -= step
            print(f'Бот взял {step} конфет(ы)')
            print(f'Осталось {candies} конфет(ы)')
            print()
            bot, player = False, True
    else:
        if player == False:
            print('Поздравляю! Вы победили')
        elif bot == False:
            print('Game Over. Победил бот')


play(gamer, bot, bonbon, step_of_human)

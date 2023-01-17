# Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

pole = list(range(1, 10))

wins_positions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (7, 5, 3)]

# функция отрисовки игрового поля
def draw_pole():
    print('-------------')
    for i in range(3):
        print('|', pole[0 + i*3], '|', pole[1 + i*3], '|', pole[2 + i*3], '|')
    print('-------------')


# Функция проверки ввода. Проверка на правильность ввода и прокерка на то, занята эта клетка уже или нет
def take_input(player_step):
    while True:
        value = input('Куда поставить: ' + player_step + '? ')
        if not value in '123456789':
            print('Неверный ввод. Повторите снова.')
            continue
        value = int(value)
        if str(pole[value - 1]) in 'XO':
            print('Эта клетка уже занята')
            continue
        pole[value - 1] = player_step
        break

# Функция проверки на выгрыш. Перебирает все выйгрышные ситуации, если да-то игра окончена
def check_winner():
    for each_pos in wins_positions:
        if (pole[each_pos[0] - 1] == pole[each_pos[1] - 1] == pole[each_pos[2] - 1]):
            return pole[each_pos[1] - 1]
    else:
        return False

# Функция игровой логики
def main():
    count = 0
    while True:
        draw_pole()
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if count > 3:
            winner = check_winner()
            if winner:
                draw_pole()
                print(winner, 'выйграл!')
                break
        count += 1
        if count > 8:
            draw_pole()
            print('Ничья!')
            break

main()
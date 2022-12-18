# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, 
# который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

import random
number = int(input('Input any number: '))
list_numbers = []

# Заполняем список [-N, N]
for i in range(-number, number + 1):
    list_numbers.append(i)
print(list_numbers)

# Заполняем список с индексами
list_indexes = []
for i in range(5):
    list_indexes.append(random.randint(0, 2 * number))
print(list_indexes)


multiple = 1
for  i in list_indexes:
    multiple *= list_numbers[i]
print (f'The multiple of numbers and respective indexes is {multiple}')

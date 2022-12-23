# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

size_list = int(input("Input the size of list: ")) 
list_numbers = []
for i in range(size_list):
    list_numbers.append(random.randint(0, 20))

sum_odd_items = 0
for i in range(1, size_list, 2):
    sum_odd_items += list_numbers[i]

print(list_numbers)
print(f'The sum of the odd items in this list is {sum_odd_items}')
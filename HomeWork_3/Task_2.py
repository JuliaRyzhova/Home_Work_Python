# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

size_list = int(input("Input the size of list: ")) - 1
list_numbers = [size_list]
for el in range(size_list):
    list_numbers.append(random.randint(0, 10))

print(list_numbers)

multipl_items = []
for i in range(size_list):
    if i < size_list // 2:
        multipl_items.append(list_numbers[i] * list_numbers[-1 -i])
    else:
        multipl_items.append(list_numbers[i] * list_numbers[i])
        break

print(multipl_items)

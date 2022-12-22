# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
# Генерируем список случайных вещественных чисел
size_list = int(input("Input the size of list: ")) - 1
list_numbers = [size_list]
for el in range(size_list):
    list_numbers.append(round(random.uniform(0, 10), 2))

print(list_numbers)

# Создаем новый список из дробных частей 
fractional_part_list = []
for el in list_numbers:
    fractional_part_list.append(round(el - int(el), 2))

print(fractional_part_list)

diff = max(fractional_part_list) - min(fractional_part_list)
print(f'The difference between max and min fractional part is {diff}')
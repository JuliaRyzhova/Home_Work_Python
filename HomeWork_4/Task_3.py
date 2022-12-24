# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1

import random 

# Создаем рандомный список
size_list = int(input("Input the size of list: ")) 
list_numbers = []
for i in range(size_list):
    list_numbers.append(random.randint(0, 10))

print(list_numbers)

# Ищем уникальные элементы
for el in list_numbers:
    count = list_numbers.count(el)
    if count == 1:
        print(el, end=' ')



            
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Input any number: '))

# список для простых чисел
simple_numbers_list = []
# count- счетчик делителей
count = 0
# проходим циклом по всем числам от 2 до N. Т.к. 1 - это и не простое и не составное число
for i in range(2, number + 1):
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:
        simple_numbers_list.append(i)
    else:
        count = 0

# print (simple_numbers_list)

def decompose_number(value):
    for i in simple_numbers_list:
        while value % i == 0:
            if value > i:
                print(i, end =' * ')
                value //= i 
            else:
                print(i)
                break

decompose_number(number)








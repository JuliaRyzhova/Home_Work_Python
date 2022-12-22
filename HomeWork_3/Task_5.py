# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Input any positiv number: '))

# Создала список последовательности для положительных индексов и заполнила его
fibonachi = []
for i in range(0, number):
    if i == 0 or i == 1:
        fibonachi.append(1)
    else:
        fibonachi.append((fibonachi[i - 1]) + (fibonachi[i - 2]))

# print(fibonachi)
# Создала список последовательности для отрицательных индексов и заполнила его
negafibonachi = []
for i in range(0, number + 1):
    if i == 0:
        negafibonachi.append(0)
    elif i == 1:
        negafibonachi.append(1)
    elif i == 2:
        negafibonachi.append(-1)
    else:
        negafibonachi.append(negafibonachi[i - 2] - negafibonachi[i  - 1])

# Развернула список для отрицательных индексов в обратном порядке       
negafibonachi.reverse()
# Объединила два списка в один
negafibonachi.extend(fibonachi)
print(negafibonachi)

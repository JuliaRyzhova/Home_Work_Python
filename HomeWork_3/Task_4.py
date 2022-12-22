# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Input any number: "))

# Создаем новый список, чтобы занести в него остатки от деления числа на 2
binary_list = []

while number > 0:
    binary_list.append(number % 2)
    number //= 2

# Разворачиваем список в обратном порядке
binary_list.reverse()

# Выводим на печать с преобразованием списка списка чисел в строку
print(f"This is {''.join(map(str, binary_list))} in binaryy notation")


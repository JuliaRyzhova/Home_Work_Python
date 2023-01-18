# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите любое вещественное число: ')

lst = list(map(int, (el for el in number if el.isdigit())))

sum_digit = sum(lst)

print(f'Исходное число: {number}')
print(f'Сумма его чисел = {sum_digit}')

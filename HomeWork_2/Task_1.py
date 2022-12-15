# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

#  6782 -> 23
#  0,56 -> 11

number = float(input('Введите вещественное число: '))
fraction = int(number % 1 * 100)  # Дробную часть числа выводим в отдельную переменную
number = int(number)
sum = 0

while number != 0 or fraction != 0:
    sum += fraction % 10 + number % 10
    number //= 10
    fraction //= 10

print(f'Сумма цифр числа = {sum}')

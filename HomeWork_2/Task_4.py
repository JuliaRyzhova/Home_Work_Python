# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

number = int(input('Input any number: '))

sum = 0
for i in range(2, number + 1, 2):
    sum += i

print(f'The sum of positive numbers in range from 1 to {number} is {sum}')

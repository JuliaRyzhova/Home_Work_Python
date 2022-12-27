# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и вывести многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 
# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h
#     a, b, c, d, e, h - рандом

from random import randint

k = int(input('Input the max degree of the polynomial: '))

# функция герерирования случайного многочлена степени n с коэффициентами в диапазоне от 0 до 99
def generate_polystring(n):
    generated_polynom = ""
    for i in range(n, -1, -1):
        rnd = randint(0,100)
        if rnd != 0:
            # если элемент не первый, то добавляем в строку +
            if len(generated_polynom) > 1:
                generated_polynom += " + "
            # если итерация последняя, то добавляем коэффициент без x**, т.к. x**0 == 1
            if i == 0:
                generated_polynom += str(rnd)
            else:
                generated_polynom += str(rnd) + "*x**" + str(i)
    return generated_polynom

polynom = generate_polystring(k)
print('The created polynom is:', polynom)


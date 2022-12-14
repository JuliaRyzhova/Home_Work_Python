# Задача 2. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. (0,0,0), (0,0,1) и тд


def law_de_morgan():

    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not (x or y or z) == (not x) and (not y) and (not z):
                    print(f'{x}, {y}, {z}, True')
                else:
                    print(f'{x}, {y}, {z}, False')

law_de_morgan()

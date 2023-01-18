# Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

with open('HomeWork_6/data_for_task2.txt', mode='r') as data:
    stroka = ''
    for el in data:
        stroka += el


lst_num = list(map(int, filter(lambda x: x.isdigit(), stroka)))
lst_str = list(filter(lambda x: not x.isdigit(), stroka))


print(f'Исходные данные: {stroka}')
print(f'Список содержащий только цифры: {lst_num}')
print(f'Список содержащий только буквы: {lst_str}')

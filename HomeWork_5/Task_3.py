# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.
# Пример:
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"

with open('HomeWork_5/text.txt', mode='r') as data:
    stroka = ''
    for el in data:
        stroka += el

lst = list(map(str, stroka))
print(f'Исходные данные: {lst}')

# Функция кодирования текста
def rle_encoding(text):
    encoding = ''
    diff_el = ''
    count = 0
    for el in text:
        if el != diff_el:
            if diff_el:
                encoding += str(count) + diff_el
            count = 1
            diff_el = el
        else:
            count += 1
    else:
        encoding += str(count) + diff_el
        return encoding


encoding_text = rle_encoding(lst)
print(f'Текст после RLE-сжатия : {encoding_text}')


# Функция распаковки текста после кодирования
def rle_decoding(text):
    decoding = ''
    count = ''
    for el in text:
        if el.isdigit():
            count += el
        else:
            decoding += el * int(count)
            count = ''
    return decoding

print(f'Распакованный текст после кодирования : {rle_decoding(encoding_text)}')


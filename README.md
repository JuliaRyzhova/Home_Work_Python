# Домашние задания по теме "Знакомство с Python"

## HomeWork_1

### **Задача 1**:

Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
и проверяет, является ли этот день выходным.

Пример:

 6 -> да

 7 -> да
 
 1 -> нет

### **Задача 2**:

Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
(0,0,0), (0,0,1) и тд.

### **Задача 3**:

Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

x=34; y=-30 -> 4

x=2; y=4-> 1

x=-34; y=-30 -> 3

### **Задача 4**:

Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

### **Задача 5**:

Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

A (3,6); B (2,1) -> 5,09

A (7,-5); B (1,-1) -> 7,21

## HomeWork_2

### **Задача 1**:
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

### **Задача 2**:
Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

Пример:

Для n = 15: Ответ: 3

Для n = 35: Ответ: 5

### **Задача 3**:
Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

Ввод: 4

[-4, -3, -2, -1, 0, 1, 2, 3,4]

### **Задача 4**:
Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.


## HomeWork_3

### **Задача 1**:
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

### **Задача 2**:
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

### **Задача 3**:
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

### **Задача 4**:
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10

### **Задача 5**:
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

## HomeWork_

### **Задача 1**:
Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, 
сколько указал пользователь(БЕЗ round())

### **Задача 2**:
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

### **Задача 3**:
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
элементов исходной последовательности.

Ввод:

3 1 2 3

Вывод:

2 1

### **Задача 4**:
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и вывести многочлен степени k.

Пример:
k=2 => 2*x² + 4*x + 5 

k = 6

ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h

a, b, c, d, e, h - рандом


## HomeWork_5

### **Задача 1**:
Создайте программу для игры с конфетами человек против бота.
Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
Победитель - тот, кто оставил на столе 0 конфет.

120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

1.1) Добавьте игру против бота

1.2) Подумайте как наделить бота ""интеллектом"" (Теория игр)

### **Задача 2**:
Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

### **Задача 3**:
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные данные хранятся в отдельных текстовых файлах.

stroka = "aaabbbbccbbb"

stroka = "3a4b2c3b"

Вывод: stroka = "aaabbbbccbbb"
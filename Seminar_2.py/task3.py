# 3.	Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

n = int(input('Введите число N: '))
for i in range(n):
    print ((-3) ** i, end = ' ')
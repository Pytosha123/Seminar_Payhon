#Наибольший общий делитель
#В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел. Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.
#Входные данные Выходные данные
#36 6
#12
#144
#18

import math
my_list = []
print("Введите числа ")
i = '0'
nod = []
while i != '':
     i = input()
     my_list.append(i)
del my_list[-1]
my_list = [int(i) for i in my_list]

for el in range(len(my_list)-1):
     for j in range(el + 1, len(my_list)):
        nod.append(math.gcd(my_list[el], my_list[j]))

print(min(nod))

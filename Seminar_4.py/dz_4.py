#4.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
#Пример:
#	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input("Введите степень многочлена "))
exponent_list = []
coefficient_list = []

for i in range(k, 0, -1):
    exponent_list.append(i)

for i in range(k):
    coefficient_list.append(random.randint(0, 100)) 

with open('file.txt', 'w') as data:
    data.write('')

with open('file.txt', 'w') as data:
    for i in range(k):
        data.write(str(coefficient_list[i])+'x'+'^'+str(exponent_list[i])+'+')
    data.write(str(random.randint(0, 100))+' = 0')

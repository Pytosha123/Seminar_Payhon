#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

x = int(input("Введите координату по точке х "))
y = int(input("Введите координату по точке y "))
if x > 0 and y > 0:
    print('Точка находиться в первой координатной плоскости')
elif x < 0 and y > 0:
      print('Точка находиться в второй координатной плоскости')
elif x < 0 and y < 0:
    print('Точка находиться в третьей координатной плоскос')
elif x > 0 and y < 0:
    print('Точка находиться в четвертой координатной плоскости')
else:
    print('Введена нулевая координата')

            


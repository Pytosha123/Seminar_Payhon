#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

xa = int (input('Введите координату точки А по х '))
ya = int (input('Введите координату точки А по y '))
xb = int (input('Введите координату точки B по х '))
yb = int (input('Введите координату точки B по y '))
import math
print (math.sqrt(math.pow(xb - xa, 2) + math.pow(yb - ya, 2)))
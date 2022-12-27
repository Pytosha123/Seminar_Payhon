#2.	Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет, 
#можно ли из этих отрезков составить треугольник. 

a = 1
b = 1
c = 2

def triangle(a, b, c):
    if a+b>c and b+c>a and c+a>b:
        return True
    return False
print(triangle(a,b,c))




#5.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

number = int(input("Введите целое число "))

def fibonacci(n):
     if n == 0 or n == 1:
         return n
     return fibonacci(n - 1) + fibonacci(n - 2)

def negafibonacci(n):
     return (-1) ** (n + 1) * fibonacci(n)

list_fibonacci = []
for i in range(number + 1):
     list_fibonacci.append((negafibonacci(i)))

list_fibonacci.reverse()
list_fibonacci.pop(-1)

for i in range(number + 1):
     list_fibonacci.append(fibonacci(i))
print(list_fibonacci)
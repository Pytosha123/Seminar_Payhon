#змените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ), 
#применив лямбды, filter, map,
# zip, enumerate, списочные выражения.


#count = 1

#print("Введите  число N \n")
# n = int(input())
# for i in range(1, n+1):
#     count = count * i
#     print(count, end=' '

n = int(input("Введите  число N "))
sp = [i for i in range(1, n+1)]
sp = list(map(lambda x: math.factorial(x), sp))
print(sp)

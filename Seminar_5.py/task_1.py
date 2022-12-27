#1.	В файле находится N натуральных чисел, записанных через пробел. 
#Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


path = 'file.txt'

data = open(path , 'r')

a = data.read().split()
a = list(map(int,a))
print(a)

data.close()
for i in range(1,len(a)):
    if a[i]!=a[i-1] + 1:
        print (a[i+1]+1)

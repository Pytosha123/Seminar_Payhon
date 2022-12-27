# def func(x):
# return x ** 2
#
# res = func(3)
# print(res)

# res = lambda x: x ** 2
# print(res(3))

#def ispositive(x):
#return x > 0

sp = [1, -5, 3, -7, 8]
# res = list(filter(ispositive, sp))
res = list(filter(lambda s: s > 0, sp))
# print(res)


#def kvadrat(x):
#return x ** 2

#sp = [1, 2, 3, 4, 5]
# res = list(map(kvadrat, sp))
#res = list(map(lambda a: a ** 2, sp))
# print(res)

# Сортировка
sp = ['rrr', 'z', 'tyjuuu', 'aaaaaaaaaaa']
sp.sort(key=lambda a: -len(a))
sp.sort(key=lambda a: len(a), reverse=True)
# print(sp)

sp = [['a', 66], ['b', 66], ['c', 1], ['d', 1]]
sp.sort(key=lambda x: (-x[1], x[0]))
# print(sp)

# Списочные выражения
sp = [i * 10 for i in range(1, 100) if i % 4 == 0]
# print(sp)

a, b, c = [int(i) for i in input("Введите значения A,B,C: ").split()]
print(a + b + c)
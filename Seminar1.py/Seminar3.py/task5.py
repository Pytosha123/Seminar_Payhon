#5.	Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
element = 'qwe'
count = 0
for i in range(len(list)):
    if list[i] == element:
        count += 1
    if count == 2:
        print(i)
        break
    if count > 2:
        print(-1)
    
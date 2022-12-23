#3.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#[1, 2, 2, 3, 4]  -> [1, 3, 4]


colection = [1, 2, 2, 3, 4]
count1 = 0
colection_one_element = []
for i in colection:
    count1 = colection.count(i)        
    if count1 == 1:
        colection_one_element.append(i)
print(colection_one_element, end=' ')
# 5.	Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, другие методы из библиотеки random - можно).


import random
test_list = [1, 4, 5, 6, 3]
print ("The original list is : " + str(test_list))
random.shuffle(test_list)
print ("The shuffled list is : " +  str(test_list))
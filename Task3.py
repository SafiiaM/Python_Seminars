# 2.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

import random
numbers = [random.randint(-1,9) for i in range(15)]
print(numbers)
newnumbers = [] 
[newnumbers.append(i) for i in numbers if i not in newnumbers ]
print(newnumbers) 


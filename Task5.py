# Реализуйте алгоритм перемешевания списка 

import random

def mix_list(base_list):
    list = base_list[:]
    list_length = len(list)
    for i in range(list_length):
        index_accidental = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_accidental]
        list[index_accidental] = temp
    return list
list = [15, 2, 4, 8, 7, 6, 7, 3, 2]
mixed_list = mix_list(list)
print("Первоначальный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)
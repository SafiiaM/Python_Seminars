# 1.	Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.2, 3.1, 5, 10.01]
# print(list)

# def dif(list):
#     dif_max_min =[]
#     for i in range(len(list)):
#         dif_max_min.append(list[i]%1)
#     return max(dif_max_min) - min(dif_max_min)
# print(round(dif(list),2))

# улучшение

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))


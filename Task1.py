# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
result_list = list(filter(lambda a: my_list.count(a) == 1, my_list))
print(f'Для последовательности {my_list}, \n   список уникальных элементов => {result_list}')


# lst = [1, 2, 3, 5, 1, 5, 3, 10]
# print(list(set(lst)))

# numbers = [1, 2, 3, 5, 1, 5, 3, 10]
# unique_numbers = list(set(numbers))
# print(unique_numbers)

# numbers = [1, 2, 3, 5, 1, 5, 3, 10]

# def get_unique_numbers(numbers):
#     unique = []

#     for number in numbers:
#         if number in unique:
#             continue
#         else:
#             unique.append(number)
#     return unique

# print(get_unique_numbers(numbers))

# numbers = [1, 2, 3, 5, 1, 5, 3, 10]

# def get_unique_numbers(numbers):
#     unique = []
#     for number in numbers:
#         if number not in unique:
#             unique.append(number)
#     return unique

# print(get_unique_numbers(numbers))

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]

# def get_unic(my_list):
#     unic = []
#     for i in range(len(my_list)):
#         if my_list[i] not in my_list[i+1::] and my_list[i] not in my_list[:i-1:]:
#             unic.append(my_list[i])
#     return unic

    
# print(get_unic(my_list))




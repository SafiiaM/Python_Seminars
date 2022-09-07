# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# n = int(input('Введите число: ')) 
# list = [-n,n]
# def mult 


import random

def write_file(number):
    with open('file.txt', 'w') as data:
        for i in range(number):
            data.write(f'{random.randrange(0, 2*number)}\n')


def read_file():
    with open('file.txt', 'r') as data:
        indexs = list(map(int,data.readlines()))
    return indexs


n = int(input('Введите число N: '))
first_number = [i for i in range(-n, n+1)]
write_file(n)
first_index = read_file()
mult = 1
for i in range(len(first_index)):
    mult *= first_number[first_index[i]]
print(f'Произведение элементов = {mult}')
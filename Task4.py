# 3.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
# k = int (input('Введите натуральную степень k= '))
# numbers = [random.randint(0,100) for k in range(15)]
# with open('k.txt', 'w') as data:
#     data.write('2*x² + 4*x + 5 = 0\n')
# data.write('x² + 5 = 0 или 10*x² = 0\n')



import random
def write_file(st):
    with open('k.txt', 'w') as data:
        data.write(st)
def rnd():
    return random.randint(0,101)
def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr
k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))


# import random
# import pathlib

# k = int(input('Введите коэффициент: '))
# a = int(random.randint(0,100))
# b = int(random.randint(0,100))
# c = int(random.randint(0,100))
# if a != 0:
#     first = (str(a) + "x^" + str(k) + " + ")
# else:
#     first = (str())
# if b != 0:
#     second = (str(b) + "x" + " + ")
# else:
#     second = (str())
# if c != 0:
#     third = (str(c) + " = 0")
# else:
#     third = (str())
# print(f'{first}{second}{third}')


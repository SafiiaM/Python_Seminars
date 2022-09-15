# 1.	Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.

# import random

# def write_file(name,st): # запись в файл
#     with open(name, 'w') as data:
#         data.write(st)

# def rnd(): # создание случайного числа от 0 до 100
#     return random.randint(0,101)

# def create_mn(k): # создание коэффициентов многочлена
#     lst = [rnd() for i in range(k+1)]
#     return lst
    

# def create_str(sp): # создание многочлена в виде строки 
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# def sq_mn(k): # получение степени многочлена
#     if 'x^' in k:
#         i = k.find('^')
#         num = int(k[i+1:])
#     elif ('x' in k) and ('^' not in k):
#         num = 1
#     else:
#         num = -1
#     return num

# def k_mn(k): # получение коэффицента члена многочлена
#     if 'x' in k:
#         i = k.find('x')
#         num = int(k[:i])
#     return num

# def calc_mn(st): # разбор многочлена и получение его коэффициентов
#     st = st[0].replace(' ', '').split('=')
#     st = st[0].split('+')
#     lst = []
#     l = len(st)
#     k = 0
#     if sq_mn(st[-1]) == -1:
#         lst.append(int(st[-1]))
#         l -= 1
#         k = 1
#     i = 1 # степень
#     ii = l-1 # индекс
#     while ii >= 0:
#         if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
#             lst.append(k_mn(st[ii]))
#             ii -= 1
#             i += 1
#         else:
#             lst.append(0)
#             i += 1
        
#     return lst
    

# k1 = int(input("Введите натуральную степень для первого файла k = ")) # создание двух файлов
# k2 = int(input("Введите натуральную степень для второго файла k = "))
# koef1 = create_mn(k1)
# koef2 = create_mn(k2)
# write_file("seminar4_1.txt", create_str(koef1))
# write_file("seminar4_2.txt", create_str(koef2))

# with open('seminar4_1.txt', 'r') as data: # нахождение суммы многочлена
#     st1 = data.readlines()
# with open('seminar4_2.txt', 'r') as data:
#     st2 = data.readlines()
# print(f"Первый многочлен {st1}")
# print(f"Первый многочлен {st2}")
# print(f"Второй многочлен {st2}")
# lst1 = calc_mn(st1)
# lst2 = calc_mn(st2)
# ll = len(lst1)
# if len(lst1) > len(lst2):
#     ll = len(lst2)
# lst_new = [lst1[i] + lst2[i] for i in range(ll)]
# if len(lst1) > len(lst2):
#     mm = len(lst1)
#     for i in range(ll,mm):
#         lst_new.append(lst1[i])
# else:
#     mm = len(lst2)
#     for i in range(ll,mm):
#         lst_new.append(lst2[i])
# write_file("seminar4_res.txt", create_str(lst_new))
# with open('seminar4_res.txt', 'r') as data:
#     st3 = data.readlines()
# print(f"Итоговый многочлен {st3}")


with open('file_41.txt', 'w') as file:                 
                    file.write('4*x^2 + 7*x^4')
with open('file_42.txt', 'w') as file:                  
                    file.write('15*x^2 + 8*x^5')

with open('file_41.txt','r') as file:
                    file_41 = file.readline()
                    list_of_file_41 = file_41.split()


with open('file_42.txt','r') as file:
                    file_42 = file.readline()
                    list_of_file_42 = file_42.split()

print(f'{list_of_file_41} + {list_of_file_42}')
summa = list_of_file_41 + list_of_file_42

with open('summa.txt', 'w') as file:       
                    file.write(f'{list_of_file_41} + {list_of_file_42}')




summa = (list_of_file_41) ,'+', (list_of_file_42)




if len(file_41) > len(file_42):
                    s_file = file_41
                    file_41 = file_42
                    file_42=s_file
file_41 = file_41.split(' + ')
file_42 = file_42.split(' + ')
print(file_41,file_42)

count1 = 0
count2=len(file_42)-len(file_41)
summa = ''
for i in range(count2):
                    summa += file_42[i] + '+'

ind1 = ''
ind2 = ''

for i in range(len(file_42) - len(file_41), len(file_42)):
                    result = 0 
                    if i == len(file_42) - 1:
                        result += int(file_41[-1][:-4]+file_42[-1][:-4])
                        summa += str(result) + file_41[-1][-4:]
                    elif i == len(file_42) - 2:
                        result += int(file_41[-2][:-2] + file_42[-2][:-2])
                        summa += str(result) + file_41[-2][-2:] + ' + ' 
                    else:
                        result += int(file_41[count1][:-4]+file_42[count2][:-4])
                        summa += str(result) + file_41[count1][-4:] + ' + ' 
                        count1 += 1
                        count2 += 2
print(summa)
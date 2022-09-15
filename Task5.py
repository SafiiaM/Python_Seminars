# 1.	Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.


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
                        result += int(file_41[-2][:-2] + file_42[-2][:-2]) # ругается на эту строку (base = 10) 
                        summa += str(result) + file_41[-2][-2:] + ' + ' 
                    else:
                        result += int(file_41[count1][:-4]+file_42[count2][:-4])
                        summa += str(result) + file_41[count1][-4:] + ' + ' 
                        count1 += 1
                        count2 += 2
print(summa)

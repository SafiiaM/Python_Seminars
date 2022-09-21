# 1.	Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите число: ")) 

def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)

list = []
for a in range(1, n + 1):
    list.append(mult(a))


print(f"Произведения чисел от 1 до {n}:  {list}")

# улучшение

list = [ list[i-2] * i if list[i-2] != 0 else 1 for i in range(2, n+1) ]
print(f" Набор произведений чисел {list}")
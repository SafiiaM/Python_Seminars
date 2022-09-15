# 1.	Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


import math

pi = math.pi
print('π =', pi)
d = 0.001
print(f'Заданная точность {d}')
count = 0
while d < 1:
    count += 1
    d = d*10
print('π =' , round(pi, count))
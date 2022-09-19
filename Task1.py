# 2.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# Игра двух людей

# жребий
# from random import randint


# def p_print(name, n, count, volume):
#     print(f"Очередь {name} игрока, он взял {n} конфет, теперь у него {count} конфет. Осталось на столе {volume} конфет.")


# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while 28 < x < 1:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x

# player_1 = input("Введите имя первого игрока: ")
# player_2 = input("Введите имя второго игрока: ")
# volume = int(input("Введите количество конфет на столе: "))

# flag = randint(0,2) # очередность
# if flag:
#     print(f"Первый ходит {player_1}")
# else:
#     print(f"Первый ходит {player_2}")

# count1 = 0 
# count2 = 0

# while volume > 28:
#     if flag:
#         n = input_dat(player_1)
#         count1 += n
#         volume -= n
#         flag = False
#         p_print(player_1, n, count1, volume)
#     else:
#         n = input_dat(player_2)
#         count2 += n
#         volume -= n
#         flag = True
#         p_print(player_2, n, count2, volume)

# if flag:
#     print(f"Выиграл {player_1}")
# else:
#     print(f"Выиграл {player_2}")

# Игра человека с ботом 

# from random import randint

# # жребий

# def p_print(name, n, count, volume):
#     print(f"Очередь {name}, он взял {n}, теперь у него {count}. Осталось на столе {volume} конфет.")


# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while 28 < x < 1:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# player_1 = input("Введите имя первого игрока: ")
# player_2 = "Bot"
# volume = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # очередность
# if flag:
#     print(f"Первый ходит {player_1}")
# else:
#     print(f"Первый ходит {player_2}")

# count1 = 0 
# count2 = 0

# while volume > 28:
#     if flag:
#         n = input_dat(player_1)
#         count1 += n
#         volume -= n
#         flag = False
#         p_print(player_1, n, count1, volume)
#     else:
#         n = randint(1,29)
#         count2 += n
#         volume -= n
#         flag = True
#         p_print(player_2, n, count2, volume)

# if flag:
#     print(f"Выиграл {player_1}")
# else:
#     print(f"Выиграл {player_2}")

# Игра человека против бота c "интеллектом":

from random import randint

# жребий

def p_print(name, n, count, volume):
    print(f"Очередь {name}, он взял {n}, теперь у него {count}. Осталось на столе {volume} конфет.")

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while 28 < x < 1:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def bot_calc(volume):
    n = randint(1,29)
    while  28 >= volume-n > 29:
        n = randint(1,29)
    return n

player_1 = input("Введите имя первого игрока: ")
player_2 = "Bot"
volume = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # очередность
if flag:
    print(f"Первый ходит {player_1}")
else:
    print(f"Первый ходит {player_2}")

count1 = 0 
count2 = 0

while volume > 28:
    if flag:
        n = input_dat(player_1)
        count1 += n
        volume -= n
        flag = False
        p_print(player_1, n, count1, volume)
    else:
        n = bot_calc(volume)
        count2 += n
        volume -= n
        flag = True
        p_print(player_2, n, count2, volume)

if flag:
    print(f"Выиграл {player_1}")
else:
    print(f"Выиграл {player_2}")

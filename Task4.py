# Напишите программу, удаляющую из текста все слова, содержащие "абв".

txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')


# with open("words.txt", "r") as fin:
#     for line in fin:
#         words = line.split()
#         for word in words:
#             if "абв" in word:
#                 words.remove(word)
#         sentence = " ".join(words)
#         print(sentence)

# with open('tex.txt','r') as n:
# lst = [int(i) for i in n.readline().split()]  
# for i in range(1,len(lst)):
#         if lst[i] - lst[i - 1] > 1:
#             print(lst[i]-1)


# def del_some_words(my_text):
#     my_text = list(filter(lambda x:'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# my_text = del_some_words(my_text)
# print(my_text)


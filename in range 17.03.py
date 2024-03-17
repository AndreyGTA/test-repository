# # for i in range(1, 5, 1):
# #     print(i, end=",")
# # for i in range(10, 0, -1):
# #     print(i, end=",")
# # for i in range(2, 23, 4):
# #     print(i, end=",")
# # for i in range(1, 50, 9):
# #     print(i, end=",")
# # for i in range(2, 22, 44):
# #     print(i, end=",")
# # for i in range(50, 31, -5):
# #     print(i, end=",")
# # deck = int(input("ckoлько раз вам написать привет ?   "))
# # for deck in range(deck):
# #     print("привет")
# # deck = int(input("введите число "))
# # r = int(input("введите число "))
# # u = int(input("введите число "))
# # if deck > r and u >= 0 or deck <= r and u <= 0:
# #     print("так не может быть")   
# # for i in range(deck,r,u):
# #     print(i , end = ",")
# sumw = 0
# for x in range(1,21):
#      sumw = sumw + x
#      print(sumw)
# y = str(input("\n1.ПРИВЕТ\n2.ПОКА\n3.ДО СВИДАНИЯ\n4.КАК ДЕЛА\n5.ПЯТЬ\nвыберите слово : "))
# T = int(input("ckoлько раз написать выбраное вами слово?  "))
# for i in range(T):
#     print(y)
# for i in range(9):
#     text = input("Введите текст: ")
#     if text == "стоп":
#         break

import shutil
for i in range(9):
    i = str(i)
    shutil.copy("data", "data"+i+".txt") 
     


# summa = 0
# vvod = input("Введите оценку Дома или слово «стоп»: ")
# while vvod != "стоп":
#     num = int(vvod)
#     summa =  num
#     vvod = input("Введите оценку Дома или слово «стоп»: ")
#     
# 
# print("Среднее арефметическое оценок Дома:",  num / summa * num )

# import random
# num = random.randint(1, 1000)
# vpr = int(input("какое число я загадал ?"))
# while vpr != num:
#     if vpr > num:
#         print("меньше")
#         vpr = int(input("какое число я загадал ?"))
#     elif vpr < num:
#         print("больше")
#         vpr = int(input("какое число я загадал ?"))
# print("всё правильно")
# print("ты молодец")
# vpr = str(input("как ты угадал ?"))
vpr = int(input("cумма покупки ?  "))
bal = vpr / 10
while bal != 1000:
    print("надо ещё . " , 10000 - vpr)
    vpr = int(input("cумма покупки ?  "))
    vpr = (bal + vpr / 10)
print("надо тратить баллы")

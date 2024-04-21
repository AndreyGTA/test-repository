# slova = ["снежок", "пирожок", "СМЕТАААНА","негр" ,"ент"]
# slova[0] = "рогалик"
# slova[4] = " рот "
# print(slova) 

# slova = ["снежок", "пирожок", "СМЕТАААНА"]
# for slovo in slova:
#     print(slovo, end=" ") 
# 
# slovo = input("Введите новое слово: ")
# slova.append(slovo)
# eky = input("Введите новое слово: ")
# slova.append(eky)
# for slovo in slova:
#     print(slovo, end=" ") 

# slova = []
# for slovo in slova:
#     print(slovo, end=" ") 
# for i in range(5):
#     slovo = input("Введите новое слово: ")
#     slova.append(slovo)
# for slovo in slova:
#     print(slovo, end=" ") 
#  


# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# e = int(input("какой номер элимента списка вам нужно узнать?"))
# print(fruits[e])
# # index = fruits.index("e")

counter = 4
f = ["#", "#", "#", "#", "*", "#", "#", "#", "#",]
w = str(input("ВПРАВО\nВЛЕВО\nкуда идти :"))
while counter > 0 or counter < 8 :
    if w == "ВЛЕВО":
        f[counter - 1] = "*"
        f[counter] = "#"
        counter = counter - 1
    print(f)
        
    w = str(input("ВПРАВО\nВЛЕВО\nкуда идти :"))
    
   
print("ты прошёл")
  #  elif w == "ВПРАВО":
    







# name = input("Введите имя: ")                                                                                                                                                              
# 
# if name == "щдуп":
#     print("Привет, дима!")
#     print("Как твои дела?")
# elif name == "Игорь":
#     print("ОООО, ИГОРЮНДЕЛЬ!")
#     print("ЗАХОДИ СКОРЕЙ, ТАМ ШАШЛЫК ГОТОВ!")
# elif name == "Василий":
#     print("Здравствуйте, Василий Игоревич!")
#     print("Проходите к столу")
# else:
#     print("Ты кто такой? А ну-ка иди отсюда!")
dima = int(input("ckoko denec?  "))
if dima >= 1001 and dima <= 5000:
    print("скидка 5% , ",dima - (dima / 20))
elif dima <= 1000 :
    print("скидки нет ," ,dima )
elif dima >= 5001 and dima <= 10000:
    print("скидка 10% , " , dima - (dima / 10))
elif dima >= 10001:
    print("скидка 20% ," , dima - (dima / 5))
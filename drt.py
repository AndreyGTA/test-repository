# bg = int(input("сколько кг весит ваш багаж ?  "))
# if bg <= 25:
#     print("проходите товарищ ")
# elif bg >= 25:
#     vpr1 = str(input("надо доплатить , вы согласны?  "))
#     if vpr1 == "да":
#         print("c вас 300 $ ")
#     else:
#         print("охрана подойдите , у нас особо буйный клиент ")
MTC = int(input("1  Узнать тарифы, баланс и подключенные услуги\n2  Узнать новые интересные предложения\n3  Узнать про подключённые подписки и отключить их\n0  Соединиться с оператором\nКакую информацию вам надо узнать ?  "))
if MTC == 1:
    m1 = int(input("\n\n\n\n\n\nтариф(1)\nбаланс(2)\nподключённые услуги(3)\nотменить(0)\nКакую информацию вам надо узнать ?  "))
    if m1 == 1:
        print("тариф премиум")
    elif m1 == 2:
        print(" 2024 p")
    elif m1 == 3:
        print("1 ноль без границ\n2 мтс блек")
    elif m1 == 0:
        print("отменить")
elif MTC == 2:
    m2 = int(input("\n\n\n\n\n\nНовое предложение : найти друзей \n1 подключить\n2 не подключать"))
    if m2 == 1:
        print("спасибо доверяете нам")
    elif m2 == 2:
        print("извените , что отвлекаем вас")
elif MTC == 3:
    print("\n\n\n\n\n\nПодписки :\n1 MTC голд\n2 MTC платинум\n3 MTC титан")
elif MTC == 0:
    print("ожидайте, оператор занят.")
else:
    print("неправильный ввод")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
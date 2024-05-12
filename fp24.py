from math import sin, cos
from PIL import Image
import os
import random
login = "djfjd"
Pyautogui  = 5656
login = str(input("введите логин :"))
while login != "djfjd" :
    if login == "djfjd":    
        print("логин верный")
    else:
        print("логин неверный")
    login = str(input("введите логин :"))    
Pyautogui = int(input("введите пароль :"))
while Pyautogui != 5656:                                   
    if Pyautogui == 5656:
        print("пароль верный")
    else:
        print("пароль неверный")
    Pyautogui = int(input("введите пароль :"))
    t = str(input("Чем займёмся ?\n1.Калькулятор\n2.Corector фото\n3.УГАДАЙ ЧИСЛО\nЧем займёмся ?"))
    if t == 1:
        
        print('Калькулятор')
        f = int(input('Выберите функцию \nСложение -- 1\nВычитание -- 2\nУмножение -- 3\nДеление -- 4\nВозведение в квадрат -- 5\nВычисление квадратного корня -- 6\nВычисление синуса -- 7\nВычисление косинуса -- 8\n'))
        if f == 1:
            ch1 = int(input('Введите первое число: '))
            ch2 = int(input('Введите второе число: '))
            r = ch1 + ch2
        elif f == 2:
            ch1 = int(input('Введите первое число: '))
            ch2 = int(input('Введите второе число: '))
            r = ch1 - ch2
        elif f == 3:
            ch1 = int(input('Введите первое число: '))
            ch2 = int(input('Введите второе число: '))
            r = ch1 * ch2
        elif f == 4:
            ch1 = int(input('Введите первое число: '))
            ch2 = int(input('Введите второе число: '))
            if ch1 == 0 or ch2 == 0:
                print("на 0 делить нельзя ")
            else:
                r = float(ch1 / ch2)
            
        elif f == 5:
            ch = int(input('Введите число: '))
            r = ch * ch

        elif f == 6:
            ch = int(input('Введите число: '))
            sqrt = ch ** (0.5)
            r = sqrt

        elif f == 7:
            ch = int(input('Введите число: '))
            r = sin(ch)

        elif f == 8:
            ch = int(input('Введите число: '))
            r = cos(ch)

        print('Ответ:', r)
    if t == 2:
        vpr = str(input("inst.jpg\ngoogle.jpg\nyandex.jpg\nкакое фото открыть :"))
        image = Image.open(vpr)
        os.startfile(vpr)
        print("Ширина:", image.width)
        print("Высота:", image.height)
        vp1 = int(input("на сколько хотите расширить или сжать ?"))
        vp2 = int(input("на сколько хотите расширить или сжать ?"))
        new_image = image.resize((vp1 , vp2),Image.LANCZOS)
      ####### # new_image = image.resize((vp2 , image.width),Image.LANCZOS)
        new_image.save("new.png")
        os.startfile("new.png")
        print("Ширина:",new_image.width)
        print("Высота:",new_image.height)
        image.close()
        new_image.close()
    if t == 3:
        num = random.randint(1, 1000)
        vpr = int(input("какое число я загадал ?"))
        while vpr != num:
            if vpr > num:
                print("меньше")
                vpr = int(input("какое число я загадал ?"))
            elif vpr < num:
                print("больше")
                vpr = int(input("какое число я загадал ?"))
        print("всё правильно")
        print("ты молодец")
    else:
        print("нет такого варианта выбора")

from math import sin, cos
from PIL import Image
import os
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
    t = str(input("Чем займёмся ?\n1.Калькулятор\n2.Corector фото\nЧем займёмся ?"))
    if t == "Калькулятор":
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
    if t == "f": #"Corector фото":
        vpr = str(input("logo_Apple.jpg\nlogo_Yandex.jpg\nlogo_Google\nкакое фото открыть :"))
        image = Image.open(vpr)
        os.startfile(vpr)
        print("Ширина:", image.width)
        print("Высота:", image.height)
        new_image = image.resize((300 , image.height),Image.LANCZOS)
        new_image = image.resize((950 , image.width),Image.LANCZOS)
        new_image.save("new.png")
        os.startfile("new.png")
        print("Ширина:",new_image.width)
        print("Высота:",new_image.height)
        image.close()
        new_image.close()

        

""""
'''Задание 4
from PIL import Image point = input("Как повернуть картинку? Направо на 90 градусов, налево, вверх ногами или оставить, как есть.")
if point.lower == "оставить как есть":
    print()
elif point.lower() == "направо на 90 градусов":
    image = Image.open('tiger.jpg')
    new_image = image.rotate(240)
    new_image.save("tiger right.jpg")
    image.close()
    new_image.close()
elif point == "налево на 90 градусов":
    image = Image.open('tiger.jpg')
    new_image = image.rotate(90)
    new_image.save("tiger left.jpg")
    image.close()
    new_image.close()
elif point == "вверх ногами":
    image = Image.open('tiger.jpg')
    new_image = image.rotate(180)
    new_image.save("tiger3.jpg")
    image.close()
    new_image.close()

else:
    print("Команда не ясна")
"""

from PIL import Image
image = Image.open('lion.jpg')

art = input("Что сделать с картинкой: обрезать, повернуть, показать формат, изменить формат.Если вам больше не надо редактировать напишите стоп.")
while art != "стоп":
    art = input("Что сделать с картинкой: обрезать, повернуть, показать формат, изменить формат.Если вам больше не надо редактировать напишите стоп.")
    
    if art == "обрезать":
        rez = int(input("Насколько хотите обрезать?"))
        new_image = image.resize((300 , image.height),Image.LANCZOS)
        new_image.save("lion.jpg")
    #art = input("Что сделать с картинкой: обрезать, повернуть, показать формат, изменить формат.Если вам больше не надо редактировать напишите стоп.")
    elif art == "повернуть":
        pov = input("Насколько хотите повернуть?")
        new_image = image.rotate(pov)
        new_image.save("lion rotate.jpg")
    #art = input("Что сделать с картинкой: обрезать, повернуть, показать формат, изменить формат.Если вам больше не надо редактировать напишите стоп.")    
    elif art == "показать формат":
         print("Ширина:", image.width)
         print("Высота:", image.height)
         print("Название:", image.filename)
    #art = input("Что сделать с картинкой: обрезать, повернуть, показать формат, изменить формат.Если вам больше не надо редактировать напишите стоп.")
    elif art == "поменять формат":
        art = input("На какой формат хотели бы вы поменять? ")
        print(image.format)
        image.save('art.png', 'png')  
        img.close()
        new_img.close()


    


        
    
    
    
        
        
        
    
    
    
    
    







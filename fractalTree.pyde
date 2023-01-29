def fractalTree(x, y, length):
    if length > 5: # рисовать дерево, если длина больше 5
        line(x, y, x, y - length) #линия
        translate(0, -length) # перенос на конец этой линии
        push()
        rotate(radians(15)) # поворот на 15 градусов
        fractalTree(x, y, length * 3 / 4) # фрактальное дерево
        pop() # отмена поворота
        push()
        rotate(radians(-15)) # поворот в другую сторону
        fractalTree(x, y, length * 3 / 4) # дерево с новым поворотом
        pop()

size(1000,800)
background(100)
translate(width / 2, height / 2 + 200)
fractalTree(0, 0, 120)

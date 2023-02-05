
r = 0
def fractalTree(x, y, length, angle):
    if length > 20: # рисовать дерево, если длина больше 5
        line(x, y, x, y - length) #линия
        translate(0, -length) # перенос на конец этой линии
        push()
        rotate(angle) # поворот на 15 градусов
        fractalTree(x, y, length * 3 / 4, angle) # фрактальное дерево
        pop() # отмена поворота
        push()
        rotate(-angle) # поворот в другую сторону
        fractalTree(x, y, length * 3 / 4, angle) # дерево с новым поворотом
        pop()
        
def setup():
    size(600,600)
def draw():
    global r
    background(100)
    translate(width / 2, height / 2 + 200)
    fractalTree(0, 0, 120, r)
    r = r + 0.001

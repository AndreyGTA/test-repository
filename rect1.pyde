#2) При нажатии левой кнопки мыши на месте курсора появляется вращающийся узорчик. Угол поворота всех узорчиков одинаковый. При нажатии левой кнопки мыши последний элемент удаляется
worldsx = []
worldsy = []
angle = 0 
def setup():
     size(600,600)
def draw():
    global angle
    background(255,255,255)
    strokeWeight(20)
    global worldsx,worldsy
    rectMode(CENTER)
    for i in range(len(worldsx)):
        push()
        translate(worldsx[i],worldsy[i])
        rotate(radians(angle))
        rect(0,0,100,100)
        rect(0,0,20,20)
        point(0,0+30)
        point(0+30,0)
        point(0-30,0)
        point(0,0-30)
        point(0-30,0-30)
        point(0-30,0+30)
        point(0+30,0+30)
        point(0+30,0-30)
        pop()
    angle += 1
def mouseClicked():
    global worldsx,worldsy
    if mouseButton == LEFT:
       worldsx.append(mouseX)
       worldsy.append(mouseY)
    elif mouseButton == RIGHT:
         worldsx.pop() 
         worldsy.pop()

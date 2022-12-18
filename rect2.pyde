worldsx = []
worldsy = []
speed = []
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
        rotate(radians(speed[i]))
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
        speed[i] += 1
        pop()

def mouseClicked():
    global worldsx,worldsy
    if mouseButton == LEFT:
       worldsx.append(mouseX)
       worldsy.append(mouseY)
       speed.append(random(20))
    elif mouseButton == RIGHT:
         worldsx.pop() 
         worldsy.pop()

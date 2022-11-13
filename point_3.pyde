worldsx = []
worldsy = []
i = 0
def setup():
     size(600,600)
def draw():
    background(255,255,255)
    strokeWeight(20)
    global worldsx,worldsy,i
    for i in range(len(worldsx)):
        point(worldsx[i],worldsy[i])
        if i < 0:
          i >= 0
def mouseClicked():
    global worldsx,worldsy
    if mouseButton == LEFT:
       worldsx.append(mouseX)
       worldsy.append(mouseY)
    elif mouseButton == RIGHT:
         worldsx.pop() 
         worldsy.pop()

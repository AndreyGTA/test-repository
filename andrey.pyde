x = 200
y = 150

def setup():
    size(400,400)
    rectMode(CENTER)
    frameRate(60)
def draw():
    global x,y
    background(0)
    fill(225,225,0)
    if mousePressed:
        if mouseX > (x-25) and mouseX < (x+25) and mouseY > (y-25) and mouseY < (y+25):
            mouseDragged()
    rect(x,y,50,50)
def mouseDragged():
    global x,y
    x = mouseX
    y = mouseY
    if x > width:
        x = width
    if x > 0:

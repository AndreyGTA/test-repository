mode = "d"
SIZE = 50
def setup():
    size(600,600)
def draw():
    background(0)
    global mode,SIZE
    rectMode(CENTER)
    if mode == "d":
       SIZE = SIZE + 10
    if mode == "c":
       SIZE = SIZE - 10
    if SIZE == 10:
       mode = "d"
    if SIZE == 60:
       mode = "c"
    rect(300,300,SIZE,SIZE)
    if mousePressed:
        if mouseButton == RIGHT:
            fill(0)
def mouseClicked():
    if mouseButton == LEFT:
        fill(random(255),random(255),random(255))

x = 300
y = 300
def setup():
    size(600,600)
    strokeWeight(20)
def draw():
    global x,y
    if keyPressed:
        if keyCode == UP:
            y = y + 1
        if keyCode == DOWN:
            y = y - 1
        if keyCode == LEFT:
            x = x + 1
        if keyCode == RIGHT:
            x = x - 1
    point(x,y)

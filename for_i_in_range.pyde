y = 0
x = 0
def setup():
    size(600,400)
def draw():
    global x , y
    background(0)
    for i in range(8):
        rect(x,y,50,50)
        y = y + 50
    y = 0
    x = x + 1 

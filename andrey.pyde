x = 0
a = 0 
g = 0
def setup():
    size(600,600)
def draw():
    global a,g
    y = 0
    x = 0
    while x < width:
        fill(random(100,250),random(100,250),random(100,250))
        ellipse(x + a,y + g,5,5)
        x = x + 5
        y = y + 5
    a = a - 5
    g = g + 5

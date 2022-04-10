bg = 0
def setup():
    size(600,400)
def draw():
    global bg
    fill(255)
    line(mouseX,mouseY,pmouseX,pmouseY)
    

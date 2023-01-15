def setup():
    size(600,400)

def draw():
    snegovik(2, x, y)
  #  snegovik(10)

def snegovik(changeSize, x, y):
    scale(changeSize)
    ellipse(x,y,30,30)
    
def mouseClicked():
    if mouseButton == LEFT:
       x = x - 10
    if mouseButton == RIGHT:
       x = x + 10 
    if mouseButton == UP:
       y = y - 10
    if mouseButton == DOWN:
       y = y + 10
    

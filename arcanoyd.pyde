class Brick:
    def __init__(self , x , y , w , h ):
        self.x = x
        self.y = y
        self.w = w
        self.h = h 
    def draw(self):
        fill(0)
        rect(self.x,self.y,self.w,self.h)
        
bricks = [Brick(10,0,100,50),Brick(130,0,100,50),Brick(250,0,100,50),Brick(370,0,100,50),Brick(490,0,100,50)]
x = 270
def setup():
    size(600,400)
    
def draw():
    background(100)
    for i in range(len(bricks)):
        bricks[i].draw()
    rect(x,300,50,5)

def keyPressed():
    global x 
    if keyCode == LEFT:
        x = x - 5  
    if keyCode == RIGHT:
        x = x + 5
    if x > 600:
        x = 0
    if x < 0:
        x = 600

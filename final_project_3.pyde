class Brick:
    def __init__(self , x , y , w , h ):
        self.x = x
        self.y = y
        self.w = w
        self.h = h 
    def draw(self):
        fill(0)
        rect(self.x,self.y,self.w,self.h)
class Shar:
    def __init__(self , x , y ):
        self.x = x 
        self.y = y
        self.xdirection = 1
        self.ydirection = 1
        self.rad = 30
        
    def draw(self):
        fill(255,0,0)

        ellipse(self.x,self.y, self.rad*2, self.rad*2)
        
    def move(self):
        xspeed = 1
        yspeed = 2
        self.x = self.x + ( xspeed * self.xdirection )
        self.y = self.y + ( yspeed * self.ydirection )
        if (self.x > width-self.rad or self.x < self.rad): 
            self.xdirection *= -1
        if (self.y > height-self.rad or self.y < self.rad):
            self.ydirection *= -1
class Stik:
    def __init__(self , x , y , t , h ):
        self.x = x 
        self.y = y 
        self.t = t 
        self.h = h
        
    def draw(self):
        rect(self.x,self.y,self.t,self.h)
        
    def moveR(self, speed):
        self.x = self.x + speed
        
    def moveL(self, speed):
        self.x = self.x - speed
  

bricks = [Brick(10,0,100,50),Brick(130,0,100,50),Brick(250,0,100,50),Brick(370,0,100,50),Brick(490,0,100,50)]
shar = Shar(270,300)
stik = Stik(270,300,50,5)
def setup():
    size(600,400)
    
def draw():
    background(100)
    for i in range(len(bricks)):
        bricks[i].draw()
    shar.draw()
    shar.move()
    stik.draw()
    
def keyPressed():
    if keyCode == LEFT:
        stik.moveL(10)
    if keyCode == RIGHT:
        stik.moveR(10)
    if stik.x > 600:
        stik.x = 0
    if stik.x < -50:
        stik.x = 600

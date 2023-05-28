class Brick:
    def __init__(self , x , y , w , h ):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visibality = 1
    def draw(self):
        fill(0)
        rect(self.x,self.y,self.w,self.h)
        
    def collide(self, x , y,  rad):
        print('coolide', x, y, (self.y + self.h + rad), (self.x + self.w + rad))
        if x >= self.x and x <= (self.x + self.w + rad) and y >= self.y  and y <=  (self.y + self.h + rad):
            print('VISIBLE')
            self.visibality = 0 
class Shar:
    def __init__(self , x , y ):
        self.x = x 
        self.y = y
        self.xdirection = 1
        self.ydirection = 1
        self.rad = 15
        
    def draw(self):
        fill(255,0,0)
        ellipse(self.x,self.y, self.rad*2, self.rad*2)
        
    def move(self , brickS , stik,k = 1):
        xspeed = 0.2*k
        yspeed = 0.4*k
        self.x = self.x + ( xspeed * self.xdirection )
        self.y = self.y + ( yspeed * self.ydirection )
        # Отскок от стен горизонтальный
        if (self.x > width-self.rad or self.x < self.rad): 
            self.xdirection *= -1
        # Откок от стен вертикальный
        if ( self.y < self.rad):
            self.ydirection *= -1
        if self.y > height-self.rad :
            noLoop()
        
        for i, br in enumerate(bricks):
            if ((self.y - self.rad ) < ( br.y + br.h )) \
                and ((self.x + self.rad) < ( br.x + br.w )) and ((self.x + self.rad) > ( br.x  )):
                del bricks[i]   
                self.ydirection *= -1
        if (self.y + self.rad ) > ( stik.y ) and (self.x) > ( stik.x ) and (self.x ) < (stik.x + 50):
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
  

bricks = [Brick(10,0,100,50),Brick(130,0,100,50),Brick(250,0,100,50),Brick(370,0,100,50),Brick(490,0,100,50),Brick(10,60,100,50),Brick(130,60,100,50),Brick(250,60,100,50),Brick(370,60,100,50),Brick(490,60,100,50)]
shar = Shar(200,250)
stik = Stik(200,350,50,5)
def setup():
    size(600,400)
    
def draw():
    background(100)
    for i in range(len(bricks)):
        bricks[i].collide(shar.x, shar.y, shar.rad)

        if bricks[i].visibality:
            bricks[i].draw()

    shar.draw()
    shar.move(bricks, stik, 10)
    stik.draw()
def keyPressed():
    if keyCode == LEFT:
        stik.moveL(20)
    if keyCode == RIGHT:
        stik.moveR(20)
    if stik.x > 600:
        stik.x = 0
    if stik.x < -50:
        stik.x = 600

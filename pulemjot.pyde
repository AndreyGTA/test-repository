class Pulja:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        self.x = self.x + 1
        self.y = self.y - 1
class Pushka:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw(self):
        rect(self.x, self.y, self.w, self.h)
        
pushka = Pushka(0, 0, 60, 30)
puli = []
def setup():
    size(600,400)

def draw():
    background(100)
    translate(300, 200)
    push()
    translate(-280, 170)
    rotate(radians(-45))
    pushka.draw()
    pop()
    
    for i in range(len(puli)-1, 0, -1):
        circle(puli[i].x, puli[i].y, 10)
        puli[i].move()
        if puli[i].y < -100:
            puli.pop(i)

def keyPressed():
    if key == " ":
        puli.append(Pulja(-260, 170))

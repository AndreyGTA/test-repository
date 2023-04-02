speeds = [random(1,2) for i in range(30)]
x = [random(600) for i in range(30)]
y = [random(-100,100) for i in range(30)]
scales = [random(10,30)for i in range(30) ]
t = [random(1,4) for i in range(30)]
phi = [random(1,4) for i in range(30)]
k = 0
angle = 0
# Создадим класс — чертёж будущего объекта
class snow_flake:
    def __init__(self, sX, sY, ssSize = 1, angle = 45, speed = 45):
        self.x = sX
        self.y = sY + 45
        self.sSize = ssSize
        self.angle = angle
        self.speed = speed
    def snDraw(self):
        push()
        translate(self.x,self.y)
        scale(self.sSize/10)
        rotate(radians(self.angle))
        for i in range(4):    
           # fill(255,255,255)
            rotate(radians(45))
            line(0,-10,0,10)
            line(0,-5, 2,-8)
            line(0,-5, -2,-8)
            line(0,5, 2,+8)
            line(0,5, -2,+8)
        pop()

 
def setup():
    size(600,400)
    
def draw(): 
    global speed, angle, x, y, t, k, phi
    background(255)
    snow_flakes = []
    # Создадим два объекта и у второго 
    # Перед отрисовкой поменяем свойства
    for i, (xx,yy, ssize, speed, tt, phase) in enumerate(zip(x, y, scales, speeds, t, phi)):
       flake = snow_flake(xx,yy,ssize,angle, speed)
       y[i] = yy + speed
       x[i] = xx + tt*sin(radians(k) + phase)
       snow_flakes.append(flake)
    
    for flake in snow_flakes:
        flake.snDraw()
    k += 1
    angle += 1
    
    for i, _ in enumerate(y):
        if y[i] > height:
            y[i] = -100
    

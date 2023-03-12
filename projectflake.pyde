speed = 0
# Создадим класс — чертёж будущего объекта
class snow_flake:
    def __init__(self,sX,sY,ssSize = 1,speed = 45):
        self.x = sX
        self.y = sY
        self.sSize = ssSize 
        self.speed = speed
    def snDraw(self):
        push()
        translate(self.x,self.y)
        scale(self.sSize/10)
        # line(0,0,10,10)
        rotate(radians(self.speed))
        for i in range(4):    
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
    global speed  
    background(255)
    # Создадим два объекта и у второго 
    # Перед отрисовкой поменяем свойства
    
    sn1 = snow_flake(50,50,50,speed)
    sn2 = snow_flake(550,50,50,speed)
    sn3 = snow_flake(550,350,50,speed)
    sn4 = snow_flake(50,350,50,speed)
    sn5 = snow_flake(300,200,100,speed)  
    
        # А теперь оба нарисуем
    sn1.snDraw()
    sn2.snDraw()
    sn3.snDraw()
    sn4.snDraw()
    sn5.snDraw()
    
    speed += 1

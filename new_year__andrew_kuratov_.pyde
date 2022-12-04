snowballx = [50,75,100,125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500,525,550]
snowbally = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
speed = [1.6,1.2,1.4,1.1,1.3,1.7,1.0,1.7,1.2,1.8,1.4,1.9,1.4,1.6,1.3,1.9,1.6,1.5,1.2,1.4,1.7 ]
speed = [random(1,2) for i in range(100)]
worldsx = []
worldsy = []
i = 0
y = 540 
def setup():
     size(600,600)
def draw():
    background(0)
    global worldsx,worldsy,i, snowballx,snowbally,speed
    #fill(169,169,169)
    
    fill(255,165,0)
    ellipse(40,40,20,20)
    fill(255,215,0)
    ellipse(20,20,200,200)
    for i in range(len(snowballx)):
        fill(255,255,255)
        ellipse(snowballx[i],snowbally[i],15,15)
        snowbally[i] += speed[i]
        if snowbally[i] > height:
            snowbally[i] = 0
    strokeWeight(20)
    fill(139,69,19)
    strokeWeight(10)
    rect(260,540,60,100)
    fill(0,255,0)
    triangle(220,540,360,540,290,420)
    triangle(220,450,360,450,290,340)
    triangle(220,360,360,360,290,260)
    strokeWeight(0)
    fill(random(0,255),random(255),random(255))
    for i in range(len(worldsx)):
         ellipse(worldsx[i],worldsy[i],20,20)

def mouseClicked():
    global worldsx,worldsy
    if mouseButton == LEFT:
       worldsx.append(mouseX)
       worldsy.append(mouseY)
    elif mouseButton == RIGHT:
         worldsx.pop() 
         worldsy.pop()

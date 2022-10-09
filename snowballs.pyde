snowballx = [50,75,100,125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500,525,550]
snowbally = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
speed = [1.6,1.2,1.4,1.1,1.3,1.7,1.0,1.7,1.2,1.8,1.4,1.9,1.4,1.6,1.3,1.9,1.6,1.5,1.2,1.4,1.7 ]
speed = [random(1,2) for i in range(100)]
def setup():
    size(600,600)
    strokeWeight(10)
def draw():
    background(255,255,255)
    global snowballx,snowbally,speed
    for i in range(len(snowballx)):
        fill(255,255,255)
        point(snowballx[i],snowbally[i])
        snowbally[i] += speed[i]
        if snowbally[i] > height:
            snowbally[i] = 0

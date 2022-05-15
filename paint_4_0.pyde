x = 0
t = 0
y = 0
bg = 0 
r = 0 
def setup():
    size(600,400)
    
def draw():
    global bg,r,y 
              
    strokeWeight(0)

    fill(255,255,255)
    rect(0,50,100,50)
    rect(400,0,100,50)
    rect(300,0,100,50)
    rect(200,0,100,50)
    rect(500,0,100,50)
    rect(100,0,100,50)
    rect(0,0,100,50)
    fill(0)
    text(u"больше",230,30)
    text(u"меньше",430,30)
    text(u"цвет",340,30)
    text(u"100 кружочков",510,30)
    text(u"фон",140,30)
    text(u"сохранить",20,30)
    text(u"сбросить фон",15,80)
    fill(255,255,255)
    if mousePressed:
        if r < 0 :
            r = 1
        strokeWeight(r)
        line(mouseX,mouseY,pmouseX,pmouseY)
def mouseClicked():
    global bg,r,t
    if mouseX > 300 and mouseX < 400 and mouseY > 0 and mouseY < 50:
       fill(255,0,0)
       rect(0,350,50,50)
       fill(255,160,16)
       rect(50,350,50,50)
       fill(255,254,32)
       rect(100,350,50,50)
       fill(0,192,0)
       rect(150,350,50,50)
       fill(80,208,255)
       rect(200,350,50,50)
       fill(0,32,255)
       rect(250,350,50,50)
       
       fill(160,32,255)
       rect(300,350,50,50)
       fill(255,96,208)
       rect(350,350,50,50)
       fill(0)
       rect(400,350,50,50)
       fill(255,255,255)
       rect(450,350,50,50)
       fill(255,208,160)
       rect(500,350,50,50)
       fill(160,128,96)
       rect(550,350,50,50)
    if mouseX > 200 and mouseX < 300 and mouseY > 0 and mouseY < 50:
        r = r + 10
    if mouseX > 400 and mouseX < 500 and mouseY > 0 and mouseY < 50:
        r = r - 10
    if mouseX > 500 and mouseX < 600 and mouseY > 0 and mouseY < 50:
       for i in range(100):
           point(random(0,600),random(0,400))
           
    if mouseX > 100 and mouseX < 200 and mouseY > 0 and mouseY < 50:
       for x in range(0,650,50):
           for t in range(0,450,50):
               fill(random(0,255),random(0,255),random(0,255))
               ellipse(x,t,50,50)
       x = x + 50
       t = t + 50
    if mouseX  > 0 and mouseX < 100 and mouseY > 0  and mouseY < 50:
       save('qwerty.png')
       background(0)
       fill(255,255,255)
       text(u"cтоп",300,300)
    if mouseX > 0 and mouseX < 150 and mouseY > 50 and mouseY < 100:
       background(200,200,200)
       

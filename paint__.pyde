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
    
    rect(450,150,100,50)
    rect(250,150,100,50)
    rect(150,150,100,50)
    rect(350,150,100,50)
    rect(50,150,100,50)

    fill(0)
    text(u"больше",180,180)
    text(u"меньше",380,180)
    text(u"цвет",290,180)
    text(u"100 кружочков",460,180)
    text(u"фон",90,180)
    fill(255)
    if mousePressed:
        if r < 0 :
            r = 1
        strokeWeight(r)
        line(mouseX,mouseY,pmouseX,pmouseY)
def mouseClicked():
    global bg,r
    if mouseX > 250 and mouseX < 350 and mouseY > 150 and mouseY < 200:
        stroke(random(255), random(255),random(255))
    if mouseX > 150 and mouseX < 250 and mouseY > 150 and mouseY < 200:
        r = r + 10
    if mouseX > 350 and mouseX < 450 and mouseY > 150 and mouseY < 200:
        r = r - 10
    if mouseX > 450 and mouseX < 550 and mouseY > 150 and mouseY < 200:

       for i in range(100):
           point(random(0,600),random(0,400))
    if mouseX > 50 and mouseX < 150 and mouseY > 150 and mouseY < 200:
       
       for x in range(0,650,50):
           for t in range(0,450,50):
               fill(random(0,255),random(0,255),random(0,255))
               ellipse(x,t,50,50)
       x = x + 50
       t = t + 50
        #save('qwerty.png')

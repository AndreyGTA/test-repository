bg = 0 
r = 0 
def setup():
    size(600,400)

def draw():
    global bg,r
    strokeWeight(0)
    rect(250,150,100,50)
    rect(150,150,100,50)
    rect(350,150,100,50)
    fill(255)
    text(u"меньше",200,100)
    text(u"меньше",200,100)
    text(u"цвет",200,100)
    if mousePressed:
        if r < 0 :
            r = 1
        strokeWeight(r)
        line(mouseX,mouseY,pmouseX,pmouseY)
def mouseClicked():
    global bg,r
    if mouseX > 250 and mouseX < 350 and mouseY > 150 and mouseY < 200:
        stroke(random(255), random(255),random(255))
    if mouseX > 150 and mouseX < 350 and mouseY > 150 and mouseY < 200:
        r = r + 10
    if mouseX > 350 and mouseX < 450 and mouseY > 150 and mouseY < 200:
        r = r - 10

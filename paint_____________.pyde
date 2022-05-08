bg=0
r=0
g=0
b=0
weight = 5
def setup():
    size(600,400)
    background(128)
def draw():
    global bg,r,g,b,weight
    strokeWeight(0)
    #кнопка прямоугольная
    fill(255)
    #левый верхни угол 250 150, размеры 100 на 50
    rectMode(CENTER)
    rect(100,50,100,50) # х от 250 до 250+100, у от 150 + 50
    rect(100+100,50,100,50)
    rect(100+100+100,50,100,50)
    #круглая круглая кнопка
    ellipse(400,350,70,70) #центр x=400 y=350 dimetr 70,radius 35
    textSize(10)
    fill(0) #да, и цвет текста  это задаёт тоже 
    textAlign(CENTER,CENTER) # а так же LEFT/RIGHT и T0P/BOTTOM
    text(u"тыкни",100,50) 
    text(u"тыкни",100+100,50) 
    text(u"тыкни",100+100+100,50) 
    strokeWeight (weight)
    stroke(r,g,b)
    line(mouseX, mouseY, pmouseX, pmouseY)

             
def mouseClicked():
    global bg,r,g,b,weight
    # ecли прямоугольная кнопка нажата
    if mouseX > 50 and mouseX <150 and mouseY > 25 and mouseY < 200:
        r,g,b = 255,255,255
    if mouseX > 150 and mouseX <250 and mouseY > 25 and mouseY < 200:
          r,g,b = 0,0,0 
    if mouseX > 150+100 and mouseX <250+100 and mouseY > 25 and mouseY < 200:
         weight = weight +5          
    #если круглая кнопка нажата
    xDif = 400  - mouseX
    yDif = 350 - mouseY
    if sqrt(xDif*xDif + yDif*yDif) < 35:
        bg=0    
     

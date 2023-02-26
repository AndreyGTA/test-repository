suma = 0
def setup():
    size(600,600)
def draw():
    background(0)
    fill(255,0,0)
    rect(50,450,100,100)
    b = summa(0,suma)
    text(b,20,30)

def summa(a,b):
    return a+b
def mouseClicked():
    global suma
    if mouseX > 50 and mouseX < 150 and mouseY > 450 and mouseY < 550:
         suma = suma + 1
    

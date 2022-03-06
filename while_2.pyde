y = 0
cvet = 255
def setup():
    size(800,800)
def draw():
    x = 0
    
    global y ,cvet
    while x < 800:
        fill(cvet)
        rect(x,y,50,50)
        x += 50
        if cvet == 0:
            cvet = 255
        else:   
            cvet = 0 
    y += 50            
    if cvet == 0:
        cvet = 255
    else:
        cvet = 0 
    

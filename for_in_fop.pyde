def setup():
    size(900,900)
def draw():
    cvet = 255
   # fill(random(0,255),random(0,255),random(0,255))
    for y in range(0,900,50):
        for x in range(0,900,50):
            fill(cvet)
            rect(x,y,50,50) 
            if cvet == 255:
                cvet = 0
            else:   
                cvet = 255
               
        if cvet == 255:
            cvet = 0
        else:
            cvet = 255   

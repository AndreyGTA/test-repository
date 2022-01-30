

def setup():
    size(600,600)
def draw():

    if keyPressed:
        rotate(radians(random(270) )  )
        fill(random(255),random(225),random(255))
        text(key,random(600),random(600))
        textSize(random(200))
        

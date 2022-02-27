def setup():
    size(750,750)
def draw():

    #fill(random(0,255),random(0,255),random(0,255))
    for y in range(0,500,50):
        for x in range(0,500,50):
            rect(x,y,50,50) 
    noLoop()

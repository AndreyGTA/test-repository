y = 300
x = 300
mode = 'right'
def setup():
    size(600,600)
    frameRate(60)
def draw():
    global x,y, mode
    background(0)
    
    for i in range(10):
        fill(random(255),random(255),random(255))
        ellipse(random(0,600),random(0,600),100,100)
    
    fill(255)
    rect(x,y,100,100)
    if mode == 'right':
        x += 1
    if mode == 'left':
        x -= 1
        
    if x > 500:
        mode = 'left'
    if x < 0:
        mode = 'right'
     

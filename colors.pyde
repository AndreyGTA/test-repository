colors = ["brown","black","yellow", 'red', 'cyan']
def setup():
    size(600,600)
def draw():
    global any
    for color_item in colors:
        if color_item == 'brown':
            fill(124,64,48)
        if color_item == 'black':
            fill(0)
        if color_item == 'yellow':
            fill(255,255,0)
        if color_item == 'red':
            fill(255,0,0)
        if color_item == 'cyan':
            fill(0,0,255)
        rect(100,300,100,100)
        translate(100,0)

    

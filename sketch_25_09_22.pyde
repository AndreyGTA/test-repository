fruits = [u"хлеб",u"арбуз",u"гребешки","ORBIT",u"сыр"]

i = 0
def setup():
    size(600,600)
def draw():
    background(0)
    global fruits, i
    for k in range(len(fruits)):
        print(i, k)
        if k == i:
            fill(255,0,0)
            text(fruits[k],150,300)
            translate(0,50)
        else:
            fill(255)
            text(fruits[k],150,300)
            translate(0,50)

        
def keyPressed():
    
    global i
    if keyCode == UP:
       i = i - 1
    if keyCode == DOWN:
       i = i + 1
    if i > len(fruits) - 1 :
        i = 0 
    if i < 0 :
        i = len(fruits) - 1       

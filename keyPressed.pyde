word = [u'в',u'о',u'р',u'о',u'т',u'а']
indeces = [0,0,0,0,0,0]
y = 300
def setup():
    size(600,600)
def draw():
    global  y,word,indeces
    x = 200
    rectMode(CENTER)
    fill(255)
    background(0)
    k = 0
    for idx in indeces:
        if idx == 0:
            rect(x,y,50,50)
            x+=50
        else:
            rect(x,y,50,50)
            fill(0)    
            text(word[k], x,y)
            fill(255)
            x+=50
        k += 1
def keyPressed():
    global indeces, word
    for letter in word:
        if key == letter:
            i = word.index(letter)
            indeces[i] = 1 

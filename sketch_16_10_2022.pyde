rondom = [u'жить хорошо',u'Путин топ',u'Россия великая нация']
i = 0
def setup():
    size(600,600)
def draw():
    background(0)
    global i
    text(rondom[i],250,325)
    rect(50,300,100,50)
    rect(450,300,100,50)
    if i > 2:
      i = 0
def mouseClicked():
    global i
    if mouseX > 450 and mouseX < 550 and mouseY > 300 and mouseY < 350: 
       i = i + 1
    if i > 2:
      i = 0
    if mouseX > 50 and mouseX < 150 and mouseY > 300 and mouseY < 350:
        i = i - 1
    if i < 0:
      i = 2 

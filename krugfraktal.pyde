size(1000,800)
background(100)

def krugFractal(x, y, size): #создаю функцию «Квадрат и квадраты»
  if size > 1 :
    ellipse(x, y, size, size) # круг диаметра size
    krugFractal(x + size * 2, y, size / 2) # круг правее на два size и в два раза меньше
    krugFractal(x - size * 2, y, size / 2) # круг левее на два size и в два раза меньше

rectMode(CENTER) # пусть рисует мои квадраты из центра
translate(width / 2, height / 2)
krugFractal(0, 0, width/10)

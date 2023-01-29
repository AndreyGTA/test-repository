size(1000,800)
background(100)

def squareFractal(x, y, size): #создаю функцию «Квадрат и квадраты»
  if size > 1 :
    rect(x, y, size, size) # квадрат диаметра size
    squareFractal(x + size * 2, y, size / 2) # квадрат правее на два size и в два раза меньше
    squareFractal(x, y + size * 2, size / 2) # квадрат ниже на два size и в два раза меньше
    squareFractal(x - size * 2, y, size / 2) # квадрат левее на два size и в два раза меньше
    squareFractal(x, y - size * 2, size / 2) # квадрат выше на два size и в два раза меньше

rectMode(CENTER) # пусть рисует мои квадраты из центра
translate(width / 2, height / 2)
squareFractal(0, 0, width/20)

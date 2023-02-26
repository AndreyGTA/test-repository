# Перед отрисовкой поменяем свойства



size(600,400)
# Создадим класс — чертёж будущего объекта
class Snegovik:
   def __init__(self):
       self.x = 300
       self.y = 200
       self.sSize = 50
   def snDraw(self):
       push()
       translate(self.x,self.y)
       scale(self.sSize/10)
       ellipse(10,-10,10,-40)
       ellipse(-10,-10,-10,-40)
       ellipse(0,0,40,40)
       pop()      

sn1 = Snegovik()


# А теперь оба нарисуем
sn1.snDraw()  
sn1.x = 100  
sn1.snDraw()   
# Создадим два объекта с разными полями

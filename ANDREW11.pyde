pole = [[0,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,0],
        [0,0,0,0,0]]


#Посчитаем и запомним, сколько рядов и столбцов
numRyad = len(pole) # длина списка списков,
numStolbets = len(pole[0]) # длина первого списка в списке
def setup():
    size(600,400)
    
def draw():
    
    global finRyad, finStolbets
    for nRyada in range(numRyad): # берём каждый ряд
        # в нём каждый столбец
        for nStolbtsa in range(numStolbets):
            # если 1 красим в чёрный иначе в белый
            if pole[nRyada][nStolbtsa] == 1:
                fill(255,0,0)
            else:
                fill(255)
    
            #рисуем клеточку
            rect(nStolbtsa*30,nRyada*30,30,30)

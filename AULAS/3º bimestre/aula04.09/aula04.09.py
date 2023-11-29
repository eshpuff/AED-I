import graphics as gf
import random 
# pip install tkinter  
# criando um objeto GraphWin 

janela = gf.GraphWin("Shrek",1800,1000)

centro = gf.Point(50,50)
raio = 30
# bolinha = gf.Circle(centro,raio)
# bolinha.draw(janela)
anterior = centro
continua = True

while continua:
    coordenada = janela.getMouse()
    if coordenada.getX() == anterior.getX():
        continua = False
    else:
        anterior = coordenada

    bolinha = gf.Circle(coordenada,30)
    bolinha.draw(janela)
    bolinha.setFill(gf.color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    janela.setBackground(gf.color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

janela.close()
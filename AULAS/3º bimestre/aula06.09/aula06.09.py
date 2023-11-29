import graphics as gf
import random 

janela = gf.GraphWin("teste",500,500)

centro = gf.Point(50,50)
raio = 20
bolinha = gf.Circle(centro,raio)
bolinha.draw(janela)
coordenada = janela.getMouse()

while True:
    tecla = janela.checkKey()
    if tecla != "":
        print(tecla)

coordenada = janela.getMouse()

janela.close()
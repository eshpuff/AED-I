from graphics import *
import random

win = GraphWin("campinho",400,280)
x = 100
y = 100

campo = Rectangle(Point(20,20),Point(380,260))
campo.draw(win)

linha = Line(Point(200,20) , Point(200, 260))
linha.draw(win)

centro = Point(x,y)
raio = 20
bola = Circle(centro,raio)
bola.draw(win) 

key = win.checkKey()


while key != "Return":
    if key == "a" and x > 40:
        bola.move(-3,0)
        x -= 3
    elif key == "d":
        bola.move(3,0)
        x += 3
    elif key == "s":
        bola.move(0,3)
        y += 3
    elif key == "w":
        bola.move(0,-3)
        y -= 3

    elif key == "z":
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        bola.setFill(color_rgb(r,g,b))

    elif key == "equal":
        centro = bola.getCenter()
        bola.undraw()
        raio += 10
        bola = Circle(centro,raio)
        bola.draw(win)
        bola.setFill(color_rgb(r,g,b))

    elif key == "minus":
        centro = bola.getCenter()
        bola.undraw()
        raio -= 10
        if raio < 1:
            raio = 1
        bola = Circle(centro,raio)
        bola.draw(win)
        bola.setFill(color_rgb(r,g,b))

    key = win.checkKey()


win.getMouse()
win.close()
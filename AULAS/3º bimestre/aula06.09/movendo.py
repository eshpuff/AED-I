from graphics import *
import random

win = GraphWin("oii",500,500)
x = 30
y = 30
r = 255
g = 255
b = 255
centro = Point(x,y)
raio = 20
c = Circle(centro,raio)
c.draw(win)
key = win.checkKey()


while key != "Return":
    if key == "a":
        c.move(-3,0)
    elif key == "d":
        c.move(3,0)
    elif key == "s":
        c.move(0,3)
    elif key == "w":
        c.move(0,-3)
    elif key == "z":
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        c.setFill(color_rgb(r,g,b))
    elif key == "equal":
        centro = c.getCenter()
        c.undraw()
        raio += 10
        c = Circle(centro,raio)
        c.draw(win)
        c.setFill(color_rgb(r,g,b))
    elif key == "minus":
        centro = c.getCenter()
        c.undraw()
        raio -= 10
        if raio < 1:
            raio = 1
        c = Circle(centro,raio)
        c.draw(win)
        c.setFill(color_rgb(r,g,b))
    elif key == "b":
        win.setBackground(color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    key = win.checkKey()

# coordenada = win.getMouse()

# win.close()

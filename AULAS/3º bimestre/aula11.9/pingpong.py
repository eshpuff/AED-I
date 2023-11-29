from graphics import *

win = GraphWin("Ping Pong", 700, 500)

player1 = Rectangle(Point(20,20),Point(10,150))
player1.setFill(rgb_color(229,204,255))



player1.draw(win)
coordenada = win.getMouse()


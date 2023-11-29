from graphics import *
import time, os, sys


win = GraphWin("Relógio", 700, 700)
# hora_x = 0
# hora_y = 0
# horas = Line(Point(350,350), Point(hora_x,hora_y))


contorno = Circle(Point(350, 350), 300)
h1 = Text(Point(496, 100), "1")
h2 = Text(Point(607, 210), "2")
h3 = Text(Point(638, 353), "3")
h4 = Text(Point(611, 478), "4")
h5 = Text(Point(504, 600), "5")
h6 = Text(Point(352, 639), "6")
h7 = Text(Point(208, 601), "7")
h8 = Text(Point(89, 478), "8")
h9 = Text(Point(59, 357), "9")
h10 = Text(Point(86, 229), "10")
h11 = Text(Point(193, 105), "11")
h12 = Text(Point(351, 64), "12")

contorno.draw(win)
h1.draw(win)
h2.draw(win)
h3.draw(win)
h4.draw(win)
h5.draw(win)
h6.draw(win)
h7.draw(win)
h8.draw(win)
h9.draw(win)
h10.draw(win)
h11.draw(win)
h12.draw(win)

if time.strftime("%H",time.localtime()) == "1":
    print('oi')
    hora_x = 488
    hora_y  = 117
    horas = Line(Point(350,350), Point(hora_x,hora_y))
    horas.draw(win)

if time.strftime("%H",time.localtime()) == "2":
    print('oi')
    hora_x = 588
    hora_y  = 220
    horas = Line(Point(350,350), Point(hora_x,hora_y))
    horas.draw(win)

if time.strftime("%H",time.localtime()) == "3":
    print('oi')
    hora_x = 619
    hora_y  = 352
    horas = Line(Point(350,350), Point(hora_x,hora_y))
    horas.draw(win)

if time.strftime("%H",time.localtime()) == "4":
    print('oi')
    hora_x = 594
    hora_y  = 473
    horas = Line(Point(350,350), Point(hora_x,hora_y))
    horas.draw(win)

if time.strftime("%H",time.localtime()) == "5":
    print('oi')
    hora_x = 498
    hora_y  = 584
    horas = Line(Point(350,350), Point(hora_x,hora_y))
    horas.draw(win)

if time.strftime("%H",time.localtime()) == "6":
    print('oi')
    hora_x = 351
    hora_y  = 621
    horas = Line(Point(350,350), Point(hora_x,hora_y))
    horas.draw(win)

if time.strftime("%H",time.localtime()) == "7":
    print('oi')
    hora_x = 219
    hora_y  = 585
    horas = Line(Point(350,350), Point(hora_x,hora_y))
    horas.draw(win)

if time.strftime("%H",time.localtime()) == "8":
    print('oi')
    hora_x = 111
    hora_y  = 475
    horas = Line(Point(350,350), Point(hora_x,hora_y))
    horas.draw(win)

if time.strftime("%H",time.localtime()) == "9":
    print('oi')
    hora_x = 80
    hora_y  = 358
    horas = Line(Point(350,350), Point(hora_x,hora_y))
    horas.draw(win)

if time.strftime("%H",time.localtime()) == "10":
    print('oi')
    hora_x = 107
    hora_y  = 235
    horas = Line(Point(350,350), Point(hora_x,hora_y))
    horas.draw(win)

if time.strftime("%H",time.localtime()) == "11":
    print('oi')
    hora_x = 207
    hora_y  = 125
    horas = Line(Point(350,350), Point(hora_x,hora_y))
    horas.draw(win)

if time.strftime("%H",time.localtime()) == "12":
    print('oi')
    hora_x = 353
    hora_y  = 84
    horas = Line(Point(350,350), Point(hora_x,hora_y))
    horas.draw(win)

coordenada = win.getMouse()


print(coordenada)
print(time.strftime("%H",time.localtime()))

win.getMouse()
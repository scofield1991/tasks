__author__ = 'user'

import turtle

#circ=turtle.Turtle()
#scr=turtle.Screen()

def circle(circ,size, color):

    radius=int(size)
    rollingPer = 0

    circ.penup()
    circ.forward(radius)
    circ.left(90)
    circ.pendown()
    circ.color(color)
    circ.begin_fill()
    circ.circle(radius)
    circ.end_fill()
    circ.home()
    circ.right(90)
    circ.color('black')
    #scr.exitonclick()

def square(circ, size, color):
    circ.begin_fill()
    for i in range(4):
        circ.forward(int(size))
        circ.left(90)
    circ.color(color)
    circ.end_fill()

def triangle(tr, size, color):
    size=float(size)
    tr.fillcolor(color)
    tr.begin_fill()
    tr.right(120)
    tr.forward(size)
    tr.left(120)
    tr.forward(size)
    tr.left(120)
    tr.forward(size)
    tr.end_fill()


def drawSpiral(circ, lineLen):
    if lineLen > 0:
        circ.forward(lineLen)
        circ.right(90)
        drawSpiral(circ,lineLen-5)

    #drawSpiral(myTurtle,100)
    #myWin.exitonclick()

myPoints = [[-200, -50],[0, 200], [200, -50]]
#drawTriangle(myPoints, 'blue', circ)
#square(circ)
#circle(circ,scr)
#drawSpiral(circ, 100)
#scr.exitonclick()


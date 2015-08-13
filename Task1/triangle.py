__author__ = 'root'
import turtle
from math import sqrt, pow

#Функция рисует триугольник
def drawTriangle(points, color, tr):

    tr.fillcolor(color)
    tr.up()
    tr.goto(points[0][0],points[0][1])
    tr.down()
    tr.begin_fill()
    tr.goto(points[1][0], points[1][1])
    tr.goto(points[2][0],points[2][1])
    tr.goto(points[0][0], points[0][1])
    tr.end_fill()

#Расчет середины стороны треугольника

def getMid(p1,p2):
    return ((p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2)

#Рекурсивно вызываем функцию для прорисовки меньших треугольников

def sierpinski(points, degree, tr):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree], tr)

    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                       degree-1, tr)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                       degree-1, tr)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                       degree-1, tr)

#Расчитываем точки для каждой стороны треугольника

def calculate_points(size):
    p1=int(size/2)
    p2=int(sqrt(pow(size,2)-pow(size/2,2)))
    points=[[0, 0],[p1,p2],[ size,0]]
    return points

def main():
    size=400
    tr = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints=calculate_points(size)
    #myPoints = [[0, 0],[25, 43], [50, 0]]
    sierpinski(myPoints, 4, tr)
    myWin.exitonclick()
main()


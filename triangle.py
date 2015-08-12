__author__ = 'root'
import turtle

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

def getMid(p1,p2):
    return ((p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2)

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

def main():
    tr = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-200, -50],[0, 200], [200, -50]]
    sierpinski(myPoints, 4, tr)
    myWin.exitonclick()
main()
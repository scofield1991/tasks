__author__ = 'user'

import random
import turtle
from math import  sin,cos, sqrt, atan2

def flame(n, eqCount, it, xRes, yRes):
    fig=turtle.Turtle()
    coeff={
        1:{'a':0.5, 'b': -0.3, 'd': 0.23, 'e':0.1, 'c': 1.3, 'f': 2.1, 'red':255, 'green':255, 'blue':0},
        2:{'a':-0.3, 'b': 0.2, 'd': 0.43, 'e':0.21, 'c': 2.3, 'f': 1.1,'red':255, 'green':0, 'blue':255},
        3:{'a':0.31, 'b': 0.13, 'd': -0.43, 'e':-0.31, 'c': 1.3, 'f': 3.1,'red':0, 'green':255, 'blue':255}
    }
    pixels = [[{'x':0, 'y':0, 'red':0, 'green':0, 'blue':0, 'counter':0} for x in range(xRes)] for y in range(yRes)]

    symmetry = 1
    theta2=0
    XMIN = -1.777
    XMAX = 1.777
    YMIN = -1
    YMAX = 1


    for num in range(n):
        newX = random.uniform(XMIN, XMAX)
        newY = random.uniform(YMIN, YMAX)

        for step in range(-20, it):
            i = random.randint(1,3)
            x = coeff[i]['a']*newX + coeff[i]['b']*newY + coeff[i]['c']
            y = coeff[i]['d']*newX + coeff[i]['e']*newY + coeff[i]['f']

            #newx = sin(x)
            #newy = sin(y)

            #r = x * x + y * y
#            newx = x * sin (r) - y * cos (r)
#            newy = x * cos (r) + y * sin (r)

            r = sqrt (x * x + y * y);
            theta = atan2 (y, x);
            newx = (1.0 / r) * (cos (theta) + sin (r))
            newy = (1.0 / r) * (sin (theta) - cos (r))

            theta2 += ((2 * 3.14) / symmetry)
            x_rot = newx * cos (theta2) - newy * sin (theta2)
            y_rot = newx * sin (theta2) + newy * cos (theta2)

            if step >=0 and  XMIN<=newX<=XMAX and YMIN<=newY<=YMAX:
                x1 = xRes - round(((XMAX-x_rot)/(XMAX-XMIN))*xRes)
                y1 = yRes - round(((YMAX-y_rot)/(YMAX-YMIN))*yRes)

                if x1<xRes and y1<yRes:

                    if pixels[x1][y1]['counter'] == 0:
                        pixels[x1][y1]['red'] = coeff[i]['red']
                        pixels[x1][y1]['green'] = coeff[i]['green']
                        pixels[x1][y1]['blue'] = coeff[i]['blue']
                    else:
                        pixels[x1][y1]['red'] = (pixels[x1][y1]['red'] + coeff[i]['red'])//2
                        pixels[x1][y1]['green'] = (pixels[x1][y1]['green'] + coeff[i]['green'])//2
                        pixels[x1][y1]['blue'] = (pixels[x1][y1]['blue'] + coeff[i]['blue'])//2

                    pixels[x1][y1]['counter'] += 1

                    turtle.colormode(255)
                    #turtle.color(255,255,255)
                    fig.color(pixels[x1][y1]['red'], pixels[x1][y1]['green'], pixels[x1][y1]['blue'])
                    fig.setx(x1)
                    fig.sety(y1)
                    fig.dot(1)



flame(1000,3,3,400,400)

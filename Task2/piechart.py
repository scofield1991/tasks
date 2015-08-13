__author__ = 'user'


from turtle import *
from collections import defaultdict
import random

# Подсчет слов в тексте
def counter(txt):
    d = defaultdict(int)
    words = txt.split()
    for word in words:
        d[word] +=1

    dict_words=dict(d)
    len_txt=len(words)
    for word in dict_words:
        dict_words[word] = round(float(dict_words[word])/len_txt, 3)
    print(dict_words)
    return dict_words

#Прорисовка каждого сектора диаграммы
def sector(radius, angle):
    forward(radius)
    left(90)
    circle(radius, angle)
    left(90)
    forward(radius)
    left(180-angle)

#Прорисовка легенды
def legend(col, dict):
    i=0
    color('white')
    setx(200)
    sety(200)
    y=10
    for key in dict:
        y+=20

        color(col[i])
        dot(10)
        write("       "+key, True)
        color('white')
        setx(200)
        sety(200-y)
        i+=1


#Прорисовка всей диаграммы
def radioactive(radius1,  parts):

    #colormap = ['blue', 'red', 'green', 'yellow', 'violet', 'orange', 'palegreen', 'aqua' ]
    hexname='0123456789ABCDEF'
    colormap=[]
    words = parts
    i=0
    col='#'
    for key in words:
        #color(colormap[i])
        i+=1
        begin_fill()
        sector(radius1,words[key]*360)
        left(words[key]*360)
        #left((360 - 3 * angle)/3 + 60)
        for i in range(6):
            col=col+random.choice(hexname)
        colormap.append(col)
        #color(random.choice(colormap))
        color(col)
        end_fill()

        col='#'
        print(words)
    print(colormap)
    legend(colormap,words)


tx='So  the are are the is is the for the segments. Note'
def main():
    reset()
    width(1)
    speed(1)
    radioactive(160, counter(tx))
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
   # counter(tx)


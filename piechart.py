__author__ = 'user'


from turtle import *
from collections import defaultdict
import random

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


def sector(radius, angle):
    forward(radius)
    left(90)
    circle(radius, angle)
    left(90)
    forward(radius)
    left(180-angle)


def radioactive(radius1, radius2, side, parts):

    colormap = ['blue', 'red', 'green', 'yellow', 'violet', 'orange', 'palegreen', 'aqua' ]
    words = parts
    i=0
    for key in words:
        #color(colormap[i])
        i+=1
        begin_fill()
        sector(radius1,words[key]*360)
        left(words[key]*360)
        #left((360 - 3 * angle)/3 + 60)
        color(random.choice(colormap))
        end_fill()
        print(words)


tx='So while your function to draw segments has been defined, you are not calling the function (running the code in the function). Your function takes one argument (parameter) percentages which is a list of percentages for the segments. Note'
def main():
    reset()
    width(1)
    speed(1)
    radioactive(160, 36, 400, counter(tx))
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
   # counter(tx)


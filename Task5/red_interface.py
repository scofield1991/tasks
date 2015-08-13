__author__ = 'user'

#!/usr/bin/env python3
import shelve
from redactor import Circle, Square, Triangle
import turtle
import  figures

def doc():
    fieldnames=('name', 'size', 'color')
    maxfield = max(len(f) for f in fieldnames)
    db = {}
    while True:

        var=input('Choose operation: \n1.See list of allowed figures \n2.Add new figure or change the old one'
                  ' \n3.Delete figure \n4.Build figures \n5.Save document \n6.Open saved document ')
        if not var: break

#Просмотр доступных фигур

        if var=='1':
           print("\nAllowed figures: \n1.Circle \n2.Square \n3.Triangle\n")

#Отридактировать существующую фигуру, усли фигуры с таким именем нет, то создается фигура по умолчанию
#Классы для создание экземпляров фигур хранятся в модуле redactor

        if var=='2':
            while True:
                key = input('\nFigure? => ')
                if not key: break

#Создание круга

                if key == 'Circle':
                    name = input('\nName? => ')

                    if name in db:
                        record = db[name]
                    else:
                        record = Circle(name='?', size=50, color='black')
                    for field in fieldnames:
                        currval = getattr(record, field)
                        newtext = input('\t[%s]=%s\n\t\tnew?=>' %(field, currval))
                        if newtext:
                            setattr(record, field, newtext)
                    db[name] =record

#Создание квадрата

                if key == 'Square':
                    name = input('\nName? => ')

                    if name in db:
                        record = db[name]
                    else:
                        record = Square(name='?', size=50, color='black')
                    for field in fieldnames:
                        currval = getattr(record, field)
                        newtext = input('\t[%s]=%s\n\t\tnew?=>' %(field, currval))
                        if newtext:
                            setattr(record, field, newtext)
                        #record.field=str(newtext)
                    db[name] =record

#Создание круга

                if key == 'Triangle':
                    name = input('\nName? => ')

                    if name in db:
                        record = db[name]
                    else:
                        record = Triangle(name='?', size=50, color='black')
                    for field in fieldnames:
                        currval = getattr(record, field)
                        newtext = input('\t[%s]=%s\n\t\tnew?=>' %(field, currval))
                        if newtext:
                            setattr(record, field, newtext)
                        #record.field=str(newtext)
                    db[name] =record

                #rec[key]=record
                #rec[key]=record
                #dbn.close()
                #2db.close()
                #return rec

#Удалить фигуру из документа

        if var=='3':
            while True:
                key = input('\nName? => ')
                if not key: break
                if key in db:
                    del db[key]

#Прорисовка фигур на документе, Функции для рисования фигур хранятся в модуле figures

        if var=='4':
            print(db)
            fig=turtle.Turtle()
            scr=turtle.Screen()

            for key in db:
                #print(db[key].__class__.__name__)
                if db[key].__class__.__name__=='Circle':
                    figures.circle(fig, db[key].size, db[key].color)

                elif db[key].__class__.__name__=='Square':
                    figures.square(fig, db[key].size, db[key].color)

                elif db[key].__class__.__name__=='Triangle':
                    figures.triangle(fig, db[key].size, db[key].color)

                scr.exitonclick()

#Сохранение документа в базу figures-shelve. Если такой документ уже есть в базе, предлагается его заменить.

        if var=='5':
            dbn = shelve.open('figures-shelve')
            name = input('\nName? => ')
            if name in dbn:
                answer=input('File with such name has already been excisting, save anyway(Y/N)?')
                if answer=='Y':
                    dbn[name]=db
                else: pass
            else:
                dbn[name]=db
            dbn.close()

#Открытие сохраненного документа

        if var=='6':
            dbn = shelve.open('figures-shelve')
            name = input('\nName? => ')
            if name in dbn:
                for key in dbn[name]:
                    db[key]=dbn[name][key]
            else:
                print('\nSuch document does not excists\n')



doc()
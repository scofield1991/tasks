__author__ = 'user'

#class Doclist:
#   def __init__(self, name, date, notes={}):
#        self.name=name
#        self.date=date
#        self.notes=notes

#class Document:
#    def __init__(self, name, description, figures={}):
#        self.name=name
#        self.description=description
#        self.figures=figures
#    def __str__(self):
#        return '<%s => %s>' %(self.__class__.__name__, self.name)

class Figure:
    def __init__(self, name, size, color):
        self.name=name
        self.size=size
        self.color=color

class Circle(Figure):
    pass

class Square(Figure):
    pass

class Triangle(Figure):
    pass




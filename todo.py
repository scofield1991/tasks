class Note:
    def __init__(self, name, description, active=1):
        self.name=name
        self.description=description
        self.active=active
    def __str__(self):
        return '<%s => %s>' %(self.__class__.__name__, self.name)


class Notelist:
    def __init__(self, name, date, notes={}):
        self.name=name
        self.date=date
        self.notes=notes

#import shelve 
#note1=Note('first',"it's my first note")
#note2=Note('second',"it's my second note")
#db=shelve.open('class-shelve')
#db['note1']=note1
#db['note2']=note2
#db.close()

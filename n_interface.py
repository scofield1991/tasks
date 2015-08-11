#!/usr/bin/env python3 
import shelve
from todo import Note, Notelist

def note(rec):
    fieldnames=('name', 'description', 'active')
    maxfield = max(len(f) for f in fieldnames)
    while True:
        db = shelve.open('class-shelve')
        var=input('Choose operation: 1 - see note, 2 -add new note or change the old one, 3-delete note:  ')
        if not var: break

        if var=='1':
            while True:
                key= input('\nNote? => ')
                if not key: break
                if key in rec:
                    record=db[key]
                    for field in fieldnames:
                        print(field.ljust(maxfield), '=>', getattr(record, field)) 
                else:
                    print('No such key "%s"!' %key)
               

        if var=='2':
            while True:
                #db = shelve.open('class-shelve')
                #dbn = shelve.open('notelist-shelve')
                #records=dbn[notelist].notes
                key = input('\nNote? => ')
                if not key: break
                if key in db and key in rec:
                    record = db[key]
                else:
                    record = Note(name='?', description='?')
                for field in fieldnames:
                    currval = getattr(record, field)
                    newtext = input('\t[%s]=%s\n\t\tnew?=>' %(field, currval))
                    if newtext:
                        setattr(record, field, newtext)
                        #record.field=str(newtext)
                db[key] =record
                
                rec[key]=record
                #rec[key]=record
                #dbn.close()
                db.close()
                return rec

        if var=='3':    
            while True:
                key = input('\nNote? => ')
                if not key: break
                if key in db:
                    del db[key]



fieldnames=('name', 'date', 'notes')
maxfield = max(len(f) for f in fieldnames)

while True:
    db = shelve.open('notelist-shelve')
    var=input('Choose operation:\n1 - see all notelists, \n2 - notelist information, \n3 - add new notelist or change the old one, \n4 - work with notes of notelist, \n5 - delete notelist :  ')
    if not var: break
    if var=='1':
        for key in db:
            print(key, ' => ', db[key].name)
        print('\n')
    

    if var=='2':
        while True:
            key= input('\nNotelist? => ')
            if not key: break
            try:
                record=db[key]
            except: print('No such key "%s"!' %key)
            else:
                for field in fieldnames:
                    print(field.ljust(maxfield), '=>', getattr(record, field))  

    if var=='3':
        while True:
            #db = shelve.open('class-shelve')
            key = input('\nNotelist? => ')
            if not key: break
            if key in db:
                record = db[key]
            else:
                record = Notelist(name='?', date='?', notes={})
            for field in ('name', 'date'):
                currval = getattr(record, field)
                newtext = input('\t[%s]=%s\n\t\tnew?=>' %(field, currval))
                if newtext:
                    setattr(record, field, newtext)
                    #record.field=str(newtext)
            db[key] =record
        db.close()  

    if var=='4':
        while True:
            notelist  = input('\nNotelist? => ')
            if not notelist: break
            try:
                record=db[notelist].notes
                nd= db[notelist]
            except: print('No such key "%s"!' %notelist)
            else:
            #    for field in record:
            #        print( '\n', field.ljust(maxfield))
             #   note(record)
                nd.notes=note(record)
                if nd.notes!= None:
                    db[notelist]=nd
               # else:
                #    note(record)
        db.close() 
    
    if var=='5':    
            while True:
                key = input('\nNotelist? => ')
                if not key: break
                if key in db:
                    del db[key]   
    
 
#    while True:
#        key= input('\nKey? => ')
#        if not key: break
#        try:
#            record=db[key]
#        except: print('No such key "%s"!' %key)
#        else:
#            for field in fieldnames:
#                print(field.ljust(maxfield), '=>', getattr(record, field))    

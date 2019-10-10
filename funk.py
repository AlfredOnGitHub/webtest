from bd import *

def crearbd():
    db.connect()
    db.create_tables([Info], safe=True)

def gen():
    user = Info.create(useragent='pepe')

def lista():
    for x in Info.select():
        print("Timestamp: {}".format(Info.timestamp))
        print("User Agent: {}".format(Info.useragent))
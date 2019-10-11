from bd import *
import requests
import sqlite3

ua = requests.get('http://httpbin.org/user-agent')
data = ua.json()
tstamp = requests.get('http://httpbin.org/')
stamp = tstamp.headers["Date"]



def crearbd():
    db.connect()
    db.create_tables([Info], safe=True)

def gen():
    timestamp = Info.create(timestamp=stamp,useragent=data['user-agent'])

def lista():
    conectar = sqlite3.connect('apptest.db')
    cursor = conectar.cursor()
    cursor.execute("select * from info;")
    print(cursor.fetchall())
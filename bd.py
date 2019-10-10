from peewee import *
from datetime import datetime
from urllib.parse import urlparse
import requests

now = datetime.now()
db = SqliteDatabase('apptest.db')

class Info(Model):
    timestamp = now
    useragent = CharField()

    class Meta:
        database = db


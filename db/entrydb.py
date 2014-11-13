import settings
from mongoengine import *
import logging

mongo_database = settings.get('mongo_database')
connect('entry', host=mongo_database['host'])

class Entry(Document):
    age = IntField(required=True)
    GENDERS = ('M', 'F')
    gender = StringField(required=True, choices=GENDERS)
    kids = IntField(required=True)
    income = IntField(required=True)
    height = IntField(required=True) # 62 = 5'2"
    weight = IntField(required=True)


    def __str__(self):
        return "Entry of id: %s" % self.id





import settings
from mongoengine import *
import logging

mongo_database = settings.get('mongo_database')
connect('entry', host=mongo_database['host'])

class Entry(Document):
    session_id = IntField(required=True) # Generated by JS on page ready
    date = DateTimeField(required=True)
    age = IntField()
    GENDERS = ('M', 'F')
    gender = StringField(choices=GENDERS)
    kids = IntField()
    income = IntField()
    height = IntField() # 62 = 5'2"
    weight = IntField()
    name = StringField()
    email = StringField() # Don't validate w/ emailfield b/c they might mess up


    def __str__(self):
        return "Entry of id: %s" % self.id





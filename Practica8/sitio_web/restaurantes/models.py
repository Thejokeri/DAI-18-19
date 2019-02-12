from django.db import models
from django.utils import timezone
from pymongo import MongoClient
from mongoengine import *

connect('test')

class restaurants(Document):
    name = StringField(required=True)
    location = PointField()
    
class platos(Document):
    restaurante = ReferenceField(restaurants, on_delete=models.CASCADE)
    nombre = StringField(required=True)
    tipoCocina = StringField()
    alergenos = ListField(StringField())
    precio = FloatField(required=True)
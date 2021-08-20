from peewee import *
from os import path

ROOT = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(ROOT, "MeatZone.db"))


class Meat(Model):
    name = CharField()
    price = IntegerField()
    quantity = IntegerField()
    total_cost = IntegerField()

    class Meta:
        database = db


class Categories(Model):
    category = CharField()
    product_name = IntegerField()
    price = IntegerField()

    class Meta:
        database = db


class Hesabu(Model):
    name = CharField()
    price = IntegerField()
    quantity = IntegerField()
    total_cost = IntegerField()

    class Meta:
        database = db


Meat.create_table(fail_silently=True)
Hesabu.create_table(fail_silently=True)

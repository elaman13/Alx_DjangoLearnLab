from django.db import models
from django.db.models import CharField, IntegerField


# Create your models here.
class Book(models.Model):
    title = CharField(max_length=200)
    author = CharField(max_length=100)
    publication_year = IntegerField()

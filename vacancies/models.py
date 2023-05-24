from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=1000)


class Goods(models.Model):
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000, null=True)
    is_published = models.BooleanField(null=True)
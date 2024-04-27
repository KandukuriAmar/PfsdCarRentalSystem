from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True, unique=True)
    password = models.CharField(max_length=100)
    phonenumber = models.IntegerField()

    class Meta:
        db_table = 'sdp'


class Caruserinfo(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(primary_key=True, unique=True)
    phonenumber = models.IntegerField()
    t = models.IntegerField(default=0)

    class Meta:
        db_table = 'userbooked'

class feed(models.Model):
    FirstName=models.CharField(max_length=100, default='')
    LastName=models.CharField(max_length=100, default='')
    Email=models.EmailField()
    Comment=models.CharField(max_length=1000, default='')

    class Meta:
        db_table='userfeed'
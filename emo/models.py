from django.db import models

# Create your models here.


class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)

class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
class Chat(models.Model):
    Fromid=models.ForeignKey(Login,on_delete=models.CASCADE,related_name="fid")
    Toid=models.ForeignKey(Login,on_delete=models.CASCADE,related_name="tid")
    message=models.CharField(max_length=500)
    date=models.DateField()
class Complaints(models.Model):
    Complaints=models.CharField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    reply=models.CharField(max_length=500)
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=500)
    rating=models.FloatField()
    date=models.DateField()
class Manageplaylist(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    song=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    musician=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    file=models.FileField()
    emotion=models.CharField(max_length=300)


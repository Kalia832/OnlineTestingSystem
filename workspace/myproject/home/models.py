from django.db import models

# Create your models here.
class Users(models.Model):
    firstname=models.CharField(null=False,max_length=20)
    lastname=models.CharField(null=False, max_length=20)
    username=models.CharField(primary_key=True,max_length=20)
    phone=models.BigIntegerField()
    email=models.CharField(null=False,max_length=50)
    password=models.CharField(max_length=30)
    testattempted=models.IntegerField(default=0)
    points=models.FloatField(default=0.0)

class Questions(models.Model):
    qid=models.BigAutoField(auto_created=True,primary_key=True)
    que=models.TextField()
    a=models.CharField(max_length=255)
    b=models.CharField(max_length=255)
    c=models.CharField(max_length=255)
    d=models.CharField(max_length=255)
    ans=models.CharField(max_length=2)

class Result(models.Model):
    resultid=models.BigAutoField(primary_key=True,auto_created=True)
    username=models.ForeignKey(Users,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    attends=models.IntegerField()
    right=models.IntegerField()
    wront=models.IntegerField()
    points=models.FloatField()




from asyncio.windows_events import NULL
from sqlite3 import Timestamp
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    #------------Customer Suppot -----------
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=14)
    desc = models.TextField()
    def __str__(self):
        return self.email
class Customer(models.Model):
    #-----------User Details ---------------------
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=40,unique=True)
    password=models.CharField(max_length=40)
    phone = models.CharField(max_length=14,unique=True)
    weight=models.CharField(max_length=4)
    height=models.CharField(max_length=4)
    allergies=models.BooleanField()
    Age=models.IntegerField()
    #-------------Medician Name --------------------
    Med1= models.CharField(max_length=24,default="Medician 1")
    Med2= models.CharField(max_length=24,default="Medician 2")
    Med3= models.CharField(max_length=24,default="Medician 3")
    Med4= models.CharField(max_length=24,default="Medician 4")
    Med5= models.CharField(max_length=24,default="Medician 5")
    Med6= models.CharField(max_length=24,default="Medician 6")
    Med7= models.CharField(max_length=24,default="Medician 7")
    Med8= models.CharField(max_length=24,default="Medician 8")
    #--------------- Time Of Medician --------------
    time_1= models.TimeField(blank=True, null=True)
    time_2= models.TimeField(blank=True, null=True)
    time_3= models.TimeField(blank=True, null=True)
    time_4= models.TimeField(blank=True, null=True)
    time_5= models.TimeField(blank=True, null=True)
    time_6= models.TimeField(blank=True, null=True)
    time_7= models.TimeField(blank=True, null=True)
    time_8= models.TimeField(blank=True, null=True)
    #---------------- Pills ------------------------
    pills_1=models.IntegerField(blank=True,null=True)
    pills_2=models.IntegerField(blank=True,null=True)
    pills_3=models.IntegerField(blank=True,null=True)
    pills_4=models.IntegerField(blank=True,null=True)
    pills_5=models.IntegerField(blank=True,null=True)
    pills_6=models.IntegerField(blank=True,null=True)
    pills_7=models.IntegerField(blank=True,null=True)
    pills_8=models.IntegerField(blank=True,null=True)
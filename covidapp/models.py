# type:ignore
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date, datetime as dt
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role_choices = (('is_doctor','Doctor'),('is_patient','Patient'))

    # is_doctor = models.BooleanField(default=False)
    # is_patient = models.BooleanField(default=True)
    role = models.CharField(max_length=20, choices=role_choices,null=False)
    phone = models.IntegerField(blank=False,default=0)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True),
    def __str__(self):
        return self.user.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True),
    def __str__(self):
        return self.user.username

class ContactTracing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=60, blank=True)
    contact = models.IntegerField(blank=False,unique=True)
    date = models.DateField(null=True)

    def __str__(self):
        return f'{self.user.username}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=255, default="Add Bio....", blank=True)
    name = models.CharField(max_length=60,blank=True)
    location = models.CharField(max_length=60,blank=True)
    contact = models.ManyToManyField(ContactTracing)
    profile_pic= CloudinaryField('image')

    def __str__(self):
        return f'{self.user.username} profile'



class PatientInput(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')    
    name = models.CharField(max_length=300,blank=True)
    symptoms = models.TextField(max_length=1000,blank=True)
    location = models.CharField(max_length=300,blank=False,default='location')
    date_modified = models.DateField(auto_now=True,)
    date = models.DateField(null=True)

    def __str__(self):
        return f'{self.user.username} patient'

class DoctorsInput(models.Model):
    response=(
        ('positive', 'Positive'),
        ('negative', 'Negative'),   
    )
    recomend=(
        ('hospital care','Hospital Care'),
        ('home care', 'Home Care'),   
    )
    name = models.CharField(max_length=60,blank=True)
    status = models.CharField(choices=response,blank=False,default=0,max_length=200)
    recomendations = models.CharField(choices=recomend,blank=False,default=0,max_length=1000)
    remarks = models.TextField(max_length=1000,blank=True)
    date_modified = models.DateField(auto_now=True,)
    date = models.DateField(null=True)





# type:ignore
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime as dt



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=255, default="Add Bio....", blank=True)
    name = models.CharField(max_length=60,blank=True)
    location = models.CharField(max_length=60,blank=True)
    profile_pic= CloudinaryField('image')

    def __str__(self):
        return f'{self.user.username} profile'

class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='location') 
    name = models.CharField(max_length=60,blank=True)


class PatientInput(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')    
    name = models.CharField(max_length=300,blank=True)
    symptoms = models.TextField(max_length=1000,blank=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='location')

    def __str__(self):
        return f'{self.user.username} profile'

class DoctorsInput(models.Model):
    response=(
        (1, 'Positive'),
        (2, 'Negative'),   
    )
    recomend=(
        (1,'Hospital Care'),
        (2, 'Home Care'),   
    )
    name = models.CharField(max_length=60,blank=True)
    status = models.IntegerField(choices=response,blank=False,default=0)
    recomendations = models.IntegerField(choices=recomend,blank=False,default=0)
    remarks = models.TextField(max_length=1000,blank=True)



class ContactTracing(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contact') 
    name = models.CharField(max_length=60, blank=True)
    contact = models.IntegerField(blank=False)
    date = models.DateField(null=True)




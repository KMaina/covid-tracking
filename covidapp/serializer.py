# type:ignore
from rest_framework import serializers
from .models import Profile
from cloudinary.models import CloudinaryField

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id','username','email','phone','password','is_doctor','is_patient','role']

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id','username','email','phone','password','is_doctor','is_patient','role']
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic
    def save(self):
        user = super().save()
        user.contact = self.data.get('contact')
        user.role = self.data.get('role')
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    profile_pic = CloudinaryField('image')
    class Meta:
        model = Profile
        fields = ('name','location','bio','profile_pic')   

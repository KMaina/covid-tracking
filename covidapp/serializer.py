# type:ignore
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,DoctorsInput,PatientInput,ContactTracing
from cloudinary.models import CloudinaryField

from django.contrib.auth import get_user_model
from django.db import models, transaction

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        many=True
        model = User
        fields =  ['id','username','email','phone','role']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id','username','email','phone','password','role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], phone = self.data.get('phone'),role = self.data.get('role'))


        return user
class ProfileSerializer(serializers.ModelSerializer):
    profile_pic = CloudinaryField('image')
    class Meta:
        model = Profile
        fields = ('user','name','location','bio','profile_pic')

class DoctorInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsInput
        fields = ('id','name','status','recomendations','remarks','date','date_modified')

class PatientInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInput
        fields = ('id','user','name','symptoms','location','date','date_modified')

class ContactTracingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTracing
        fields = ('user','id','name','contact','date')


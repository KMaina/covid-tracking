# type:ignore
from django.db.models import fields
from rest_framework import serializers
from .models import Location, PatientInput, Profile
from django.contrib.auth.models import User
from .models import Profile
from cloudinary.models import CloudinaryField

from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id','username','email','phone','is_doctor','is_patient','role']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id','username','email','phone','password','is_doctor','is_patient','role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], phone = self.data.get('phone'),role = self.data.get('role'),
        is_doctor = self.data.get('is_doctor'),is_patient = self.data.get('is_patient'))


        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name','location','bio','profile_pic')  

class PatientInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInput
        fields = ('name', 'symptoms', 'location')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


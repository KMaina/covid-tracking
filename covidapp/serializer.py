# type:ignore
from django.db.models import fields
from rest_framework import serializers
from .models import PatientInput, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name','location','bio','profile_pic')  

class PatientInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInput
        fields = ('name', 'symptoms', 'location')

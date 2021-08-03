# type:ignore
from rest_framework import serializers
from .models import Profile
from cloudinary.models import CloudinaryField




class ProfileSerializer(serializers.ModelSerializer):
    profile_pic = CloudinaryField('image')
    class Meta:
        model = Profile
        fields = ('name','location','bio','profile_pic')   

# type:ignore 
from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm,UpdateUserForm,UpdateProfileForm
from .models import PatientInput, Profile, User
from .email import send_welcome_email
#api imports
from .permissions import IsAdminOrReadOnly
from .serializer import PatientInputSerializer, ProfileSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PatientInputList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        patients = PatientInput.objects.all()
        serializer = PatientInputSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializers = PatientInputSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
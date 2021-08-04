# type:ignore 
from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm,UpdateUserForm,UpdateProfileForm
from .models import Profile, User
from .email import send_welcome_email
#api imports
from .permissions import IsAdminOrReadOnly
from .serializer import ProfileSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
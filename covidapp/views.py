# type:ignore
from django.contrib.auth import get_user_model 
from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm,UpdateUserForm,UpdateProfileForm
from .models import ContactTracing, DoctorsInput, PatientInput, Profile
from .email import send_welcome_email
#api imports
from .permissions import IsAdminOrReadOnly
from .serializer import ProfileSerializer, RegisterSerializer,UserSerializer,DoctorInputSerializer,PatientInputSerializer,ContactTracingSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, generics,permissions
from rest_framework.response import Response

# auth import
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import UserSerializer, RegisterSerializer
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

User = get_user_model()

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ContactTracingViewSet(viewsets.ModelViewSet):
    queryset = ContactTracing.objects.all()
    serializer_class = ContactTracingSerializer

class DoctorsInputViewSet(viewsets.ModelViewSet):
    queryset = DoctorsInput.objects.all()
    serializer_class = DoctorInputSerializer

class PatientInputViewSet(viewsets.ModelViewSet):
    queryset = PatientInput.objects.all()
    serializer_class = PatientInputSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

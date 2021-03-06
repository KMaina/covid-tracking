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
from rest_framework.decorators import api_view
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
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import filters
User = get_user_model()
'''
     view set returning all CRUD method on profile model
'''
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

'''
     view set returning all CRUD and search method on profile model
'''
class ContactTracingViewSet(viewsets.ModelViewSet):
    search_fields = ['name','contact','user__username']
    filter_backends = (filters.SearchFilter,)
    queryset = ContactTracing.objects.all()
    serializer_class = ContactTracingSerializer
'''
     view set returning all CRUD and search method on doctors input model
'''
class DoctorsInputViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = DoctorsInput.objects.all()
    serializer_class = DoctorInputSerializer

'''
     view set returning all CRUD and search method on patient input model
'''
class PatientInputViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = PatientInput.objects.all()
    serializer_class = PatientInputSerializer

'''
    view set returning all CRUD and search method on user model
'''
class UserViewSet(viewsets.ModelViewSet):
    search_fields = ['email','username']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''
    registration api view to post new users
'''
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
'''
    Login  api view that inherits from KnoxLoginView to log in users
'''
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
'''
    custom api view to post user, generate token, confim token and login users
'''
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "role": user.role,
                "email": user.email,
                "username": user.username,
            }
        )
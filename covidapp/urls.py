# type:ignore
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet,DoctorsInputViewSet,PatientInputViewSet,ContactTracingViewSet,LocationViewSet
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI


router = DefaultRouter()

router.register('profile',ProfileViewSet,basename='profile')
router.register('location',LocationViewSet,basename='location')
router.register('contact',ContactTracingViewSet,basename='contact')
router.register('doctorsinpunt',DoctorsInputViewSet,basename='doctorsinpunt')
router.register('patientinpunt',PatientInputViewSet,basename='patientinpunt')

urlpatterns=[
    path('',include(router.urls)),
    path('<int:id>',include(router.urls)),
    path('api/patients/', views.PatientInputList.as_view()),
    path('api/location/', views.LocationList.as_view()),
    path('user/register/', RegisterAPI.as_view(), name='register'),
    path('user/login/', LoginAPI.as_view(), name='login'),
    path('user/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('user/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
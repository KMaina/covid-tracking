# type:ignore
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet,DoctorsInputViewSet,PatientInputViewSet,ContactTracingViewSet,UserViewSet
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI


router = DefaultRouter()

router.register('profile',ProfileViewSet,basename='profile')
router.register('contact',ContactTracingViewSet,basename='contact')
router.register('doctorsinpunt',DoctorsInputViewSet,basename='doctorsinpunt')
router.register('patientinpunt',PatientInputViewSet,basename='patientinpunt')
router.register('user',UserViewSet,basename='user')

urlpatterns=[
    path('',include(router.urls)),
    path('<int:id>',include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
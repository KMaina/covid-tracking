# type:ignore
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

router = DefaultRouter()

router.register('profile',ProfileViewSet,basename='profile')

urlpatterns=[
    path('',include(router.urls)),
    path('<int:id>',include(router.urls)),
    path('api/patients/', views.PatientInputList.as_view())

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
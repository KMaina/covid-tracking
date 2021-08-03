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
    path('viewset/',include(router.urls)),
    path('viewset/<int:id>',include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
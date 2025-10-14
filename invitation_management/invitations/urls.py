# Importation of necessary modules and classes
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvitationViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'invitations', InvitationViewSet, basename='invitation')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

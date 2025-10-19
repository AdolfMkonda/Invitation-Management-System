# Importation of necessary modules and classes
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvitationViewSet, InvitationListView, InvitationDetailView
from django.contrib import admin

router = DefaultRouter()
router.register(r'invitations', InvitationViewSet, basename='invitation')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('invitations/list/', InvitationListView.as_view({'get': 'list'}), name='invitation-list'),
    path('invitations/<int:pk>/', InvitationDetailView.as_view(), name='invitation-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

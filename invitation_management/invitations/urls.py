# Importation of necessary modules and classes
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import InvitationViewSet, InvitationListView, InvitationDetailView, send_invitation
from django.contrib import admin


router = DefaultRouter()
router.register(r'invitations', InvitationViewSet, basename='invitation')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('invitations/list/', InvitationListView.as_view(), name='invitation-list'),
    path('invitations/<int:pk>/', InvitationDetailView.as_view(), name='invitation-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('send-invitation/', send_invitation, name='send_invitation'),
]

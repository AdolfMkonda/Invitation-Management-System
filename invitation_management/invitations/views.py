from django.shortcuts import render
from .models import Invitation
from .serializers import InvitationSerializer
from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied


# Invitation View.
class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class InvitationListView(generics.ListAPIView):
    serializer_class = InvitationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invitation.objects.filter(recipient_email=self.request.user.email)
    
class InvitationDetailView(generics.RetrieveAPIView):
    serializer_class = InvitationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invitation.objects.filter(recipient_email=self.request.user.email)

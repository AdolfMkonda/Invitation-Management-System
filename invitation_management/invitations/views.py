from django.shortcuts import render
from .models import Invitation
from .serializers import InvitationSerializer
from rest_framework import viewsets, permissions


# Invitation View.
class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class InvitationListView(viewsets.ReadOnlyModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(recipient=self.request.user)
    
class InvitationDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs['pk'], recipient=self.request.user)

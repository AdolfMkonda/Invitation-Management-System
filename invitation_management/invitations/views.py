from django.conf import settings
from django.shortcuts import render, redirect
from .models import Invitation
from .serializers import InvitationSerializer
from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied
from .forms import InvitationForm, InvitationResponseForm


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


def send_invitation(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)

    if request.method == 'POST':
        form = InvitationForm(request.POST)
        if form.is_valid():
            invitation = form.save(commit=False)
            invitation.sender = request.user
            invitation.save()
            return render(request, 'invitations/invitation_sent.html', {'invitation': invitation})
    else:
        form = InvitationForm()
    return render(request, 'invitations/send_invitation.html', {'form': form})

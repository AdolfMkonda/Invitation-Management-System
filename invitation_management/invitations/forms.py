from django import forms
from .models import Invitation

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['recipient_email', 'message']
        widgets = {
            'recipient_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Recipient Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message here...', 'rows': 4}),
        }
        labels = {
            'recipient_email': 'Recipient Email',
            'message': 'Message',
        }
        help_texts = {
            'recipient_email': 'Enter the email address of the person you want to invite.',
            'message': 'Optional message to include with the invitation.',
        }

class InvitationResponseForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'status': 'Response',
        }
        help_texts = {
            'status': 'Select your response to the invitation.',
        }


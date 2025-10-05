from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Invitation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]
    sender = models.ForeignKey(User, related_name='sent_invitations', on_delete=models.CASCADE)
    recipient_email = models.EmailField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    sent_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Invitation from {self.sender.username} to {self.recipient_email} - {self.status}"


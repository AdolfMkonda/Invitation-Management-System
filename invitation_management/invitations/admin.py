from django.contrib import admin
from .models import Invitation


# Register your models here.
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient_email', 'status', 'sent_at', 'responded_at')
    list_filter = ('status', 'sent_at', 'responded_at')
    search_fields = ('sender__username', 'recipient_email', 'message')
    ordering = ('-sent_at',)

admin.site.register(Invitation, InvitationAdmin)


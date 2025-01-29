from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')  # Use model field names directly
    search_fields = ('name', 'email')
    readonly_fields = ('submitted_at',)


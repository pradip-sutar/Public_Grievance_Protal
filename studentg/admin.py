from django.contrib import admin
from .models import *
admin.site.register(Grievance)
admin.site.register(Reply)
admin.site.register(Notification)

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['user', 'mobile', 'address', 'pin', 'aadhaar']
    

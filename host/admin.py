from django.contrib import admin
from .models import Host

@admin.register(Host)
class HostPanel (admin.ModelAdmin) : 
    list_display = ['user','name','active','id']
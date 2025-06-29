from django.contrib import admin

from stemiotApp.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email')
    search_fields = ('client_name', 'client_email')

# Register your models here.

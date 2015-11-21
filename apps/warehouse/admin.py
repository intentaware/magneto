from django.contrib import admin
from .models import IPStore

# Register your models here.

class IPStoreAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IPStore._meta.fields]

admin.site.register(IPStore, IPStoreAdmin)

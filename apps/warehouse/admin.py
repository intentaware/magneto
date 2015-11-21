from django.contrib import admin
from .models import IPStore

# Register your models here.

class IPStoreAdmin(admin.ModelAdmin):
    list_display = ['ip', 'postal_code', 'added_on', 'updated_on']

admin.site.register(IPStore, IPStoreAdmin)

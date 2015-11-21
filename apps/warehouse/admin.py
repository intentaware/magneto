from django.contrib import admin
from .models import IPStore

# Register your models here.

class IPStoreAdmin(admin.ModelAdmin):
    list_display = ['ip', 'postal_code', 'country', 'geocode', 'added_on']
    ordering = ['postal_code__country']
    list_filter = ['postal_code__country']

admin.site.register(IPStore, IPStoreAdmin)

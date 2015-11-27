from django.contrib import admin
from .models import Asset
# Register your models here.

class AssetAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'publisher', 'url']
    list_display_links = ['id', 'url']

admin.site.register(Asset, AssetAdmin)

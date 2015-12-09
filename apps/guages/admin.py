from django.contrib import admin
from .models import Asset, Metric
# Register your models here.

class AssetAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'publisher', 'url']
    list_display_links = ['id', 'url']

class MetricAdmin(admin.ModelAdmin):
    list_display = ['id', 'asset', 'visitor', 'meta']

admin.site.register(Asset, AssetAdmin)
admin.site.register(Metric, MetricAdmin)

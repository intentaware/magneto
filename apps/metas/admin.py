from django.contrib import admin

from .models import Circle, PublisherCircle


class CircleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Circle._meta.fields]

class PublisherCircleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PublisherCircle._meta.fields]

admin.site.register(Circle, CircleAdmin)
admin.site.register(PublisherCircle, PublisherCircleAdmin)

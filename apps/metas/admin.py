from django.contrib import admin

from .models import *


class CircleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Circle._meta.fields]


admin.site.register(Circle, CircleAdmin)

from django.contrib import admin

from .models import *

class AdAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Ad._meta.fields]


admin.site.register(Ad, AdAdmin)

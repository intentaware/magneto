from django.contrib import admin

from .models import Impression


class ImpressionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Impression._meta.fields]


admin.site.register(Impression, ImpressionAdmin)

from django.contrib import admin

from .models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Company._meta.fields]


class CompanyGroupAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompanyGroup._meta.fields]


class CompanyUserAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompanyUser._meta.fields]


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyGroup, CompanyGroupAdmin)
admin.site.register(CompanyUser, CompanyUserAdmin)

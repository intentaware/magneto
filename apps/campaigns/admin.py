from django.contrib import admin

from .models import *


class CampaignAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Campaign._meta.fields]


class CouponAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Coupon._meta.fields]


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Coupon, CouponAdmin)

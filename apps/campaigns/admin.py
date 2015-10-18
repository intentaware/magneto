from django.contrib import admin
from import_export import resources, admin as ie_admin

from .models import *

class CampaignResource(resources.ModelResource):
    class Meta:
        model = Campaign

class CouponResource(resources.ModelResource):
    class Meta:
        model = Coupon


class CampaignAdmin(ie_admin.ExportActionModelAdmin):
    resource_class = CampaignResource
    list_display = [f.name for f in Campaign._meta.fields]


class CouponAdmin(ie_admin.ExportActionModelAdmin):
    list_display = [f.name for f in Coupon._meta.fields]
    resource_class = CouponResource


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Coupon, CouponAdmin)

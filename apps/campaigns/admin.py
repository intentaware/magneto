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
    #list_display = [f.name for f in Campaign._meta.fields]
    list_display = [
        'id', 'name', 'starts_on', 'ends_on', 'company', 'budget', 'coupon_value', 'is_active'
        ]
    list_display_links = ['id', 'name']
    list_filter = ['is_active', 'company']
    pass


class CouponAdmin(ie_admin.ExportActionModelAdmin):
    list_display = [f.name for f in Coupon._meta.fields]
    resource_class = CouponResource
    pass


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Coupon, CouponAdmin)

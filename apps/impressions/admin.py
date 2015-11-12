from django.contrib import admin
from import_export import resources, admin as ie_admin

from .models import Impression

class ImpressionResource(resources.ModelResource):
    model = Impression
    exclude = ['meta']


class ImpressionAdmin(ie_admin.ExportActionModelAdmin):
    list_display = ['id', 'added_on', 'campaign', 'publisher', 'meta']
    list_filter = ['campaign', 'publisher']
    resource_class = ImpressionResource
    pass


admin.site.register(Impression, ImpressionAdmin)

from rest_framework import serializers

from apps.guages.models import Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        exclude = ['publisher']

    def get_views(self, obj):
        return 0

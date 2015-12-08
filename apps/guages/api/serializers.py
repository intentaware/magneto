from rest_framework import serializers

from apps.guages.models import Asset

class AssetSerializer(serializers.ModelSerializer):
    impressions = serializers.SerializerMethodField()


    class Meta:
        model = Asset
        exclude = ['publisher']

    def get_impressions(self, obj):
        return obj.metrics.all().count()

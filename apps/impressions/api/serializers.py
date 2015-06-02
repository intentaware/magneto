from rest_framework import serializers
from apps.impressions.models import Impression


class ImpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impression

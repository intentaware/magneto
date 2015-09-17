from rest_framework import serializers
from apps.impressions.models import Impression
from apps.api.fields import JsonField


class ImpressionSerializer(serializers.ModelSerializer):
    meta = JsonField()

    class Meta:
        model = Impression

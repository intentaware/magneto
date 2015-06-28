from rest_framework import serializers
from apps.api.fields import JsonField
from apps.impressions.models import Impression


class ImpressionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Impression

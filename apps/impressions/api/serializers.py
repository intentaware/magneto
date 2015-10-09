from rest_framework import serializers
from apps.impressions.models import Impression, ImpressionUser
from apps.api.fields import JsonField


class ImpressionSerializer(serializers.ModelSerializer):
    #meta = JsonField()

    class Meta:
        model = Impression
        exclude = ('meta', )


class ImpressionUserSerializer(serializers.ModelSerializer):
    #meta = JsonField()

    class Meta:
        model = ImpressionUser


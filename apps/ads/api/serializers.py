from rest_framework import serializers

from apps.ads.models import Ad


class CreateAdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
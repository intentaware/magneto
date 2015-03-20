from rest_framework import serializers
from photologue.models import Photo

from apps.campaigns.models import Campaign
from apps.api.fields import Base64ImageField


class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign


class CreateCampaignSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Campaign
        exclude = ('company',)

    def create(self, validated_data):
        image = validated_data.get('image')
        image = Photo.objects.create(
            image=image, title=image.name, slug=image.name
        )
        i = validated_data
        i['image'] = image
        return Campaign.objects.create(**i)


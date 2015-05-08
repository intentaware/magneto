from rest_framework import serializers
from photologue.models import Photo

from apps.campaigns.models import Campaign
from apps.api.fields import Base64ImageField


class CampaignSerializer(serializers.ModelSerializer):
    preview_image_url = serializers.SerializerMethodField()
    claimed_coupons_sum = serializers.SerializerMethodField()

    class Meta:
        model = Campaign

    def get_preview_image_url(self, obj):
        if obj.image:
            return obj.image.get_preview_url()
        else:
            return ''

    def get_claimed_coupons_sum(self, obj):
        return obj.coupons.claimed().coupons_value_sum()


class CreateCampaignSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Campaign

    def create(self, validated_data):
        image = validated_data.get('image')
        if image:
            image = Photo.objects.create(
                image=image, title=image.name,
                slug=image.name
            )
        i = validated_data
        i['image'] = image
        return Campaign.objects.create(**i)

from rest_framework import serializers

from apps.campaigns.models import Campaign


class CreateCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign

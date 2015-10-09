from py2neo import Graph, Node, Relationship
from django.core.management import BaseCommand
import json

class Command(BaseCommand):
    help = 'imports impression data'

    def handle(self, *args, **kwargs):
        graph = Graph('http://neo4j:multiscan81@localhost:7474/db/data/')
        from apps.campaigns.models import Campaign
        from apps.impressions.models import Impression, ImpressionUser
        from apps.users.models import User
        from apps.campaigns.api.serializers import CampaignSerializer
        from apps.impressions.api.serializers import ImpressionSerializer, ImpressionUserSerializer
        from apps.dashboard.serializers import DashboardUserSerializer
        for campaign in Campaign.objects.all():
            campaign = CampaignSerializer(campaign).data
            campaign = Node.cast('Campaign', campaign)
            graph.create(campaign)
        for impression in Impression.objects.all():
            impression.hydrate_meta()
            meta = impression.meta
            #meta['impression'] = impression.id
            meta = Node.cast('ImpressionMeta', meta)
            graph.create(meta)
            impression = ImpressionSerializer(impression).data
            impression = Node.cast('Impression', impression)
            graph.create(impression)
        for iu in ImpressionUser.objects.all():
            iu = ImpressionUserSerializer(iu).data
            iu = Node.cast('ImpressionUser', iu)
            graph.create(iu)
        for user in User.objects.all():
            user = DashboardUserSerializer(user).data
            user = Node.cast('User', user)
            graph.create(user)






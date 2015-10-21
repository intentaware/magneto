from django.conf import settings
from django.core.management import BaseCommand
import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('campaign_id')

    def handle(self, *args, **kwargs):
        campaign_id = kwargs['campaign_id']
        self.stdout.write(campaign_id)
        from apps.impressions.models import Impression
        from apps.impressions.api.serializers import ImpressionCSVSerializer
        queryset = Impression.objects.filter(campaign_id=campaign_id)
        fieldnames = ['id', 'added_on', 'updated_on', 'visitor',
            'ip', 'city', 'postal_code', 'longitude', 'latitude', 'country',
            'user_agent', 'campaign', 'impression', 'coupon', 'publisher']
        with open('impressions.csv', 'w', encoding='utf8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for q in queryset:
                q.hydrate_meta()
                meta = dict(q.meta)
                q = dict(ImpressionCSVSerializer(q).data)
                print meta
                print q
                meta.update(q)
                print meta
                writer.writerow(meta)

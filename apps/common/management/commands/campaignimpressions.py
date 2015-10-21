from django.conf import settings
from django.core.management import BaseCommand
import csv
import cStringIO
import codecs

class UnicodeWriter(object):

    def __init__(self, f, fieldnames, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.DictWriter(self.queue, fieldnames, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, D):
        self.writer.writerow({k:str(v).encode("utf-8") for k,v in D.items()})
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for D in rows:
            self.writerow(D)

    def writeheader(self):
        self.writer.writeheader()



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
        with open('impressions.csv', 'w') as csvfile:
            csvfile.write(u'\ufeff'.encode('utf8')) #required for excel
            writer = UnicodeWriter(csvfile, fieldnames=fieldnames)
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

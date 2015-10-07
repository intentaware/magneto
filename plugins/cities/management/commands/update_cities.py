from django.core.management.base import BaseCommand

from plugins.cities.models import City


class Command(BaseCommand):
    help = 'Update City names to English'

    def handle(self, *args, **kwargs):
        self.stdout.write('Updating City Names')
        cities = City.objects.all()
        for c in cities:
            try:
                c.name = c.alt_names.get(language='en').name
                c.save()
            except:
                pass
        self.stdout.write('Updating Done')

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Create the initial API structure"

    def add_arguments(self, parser):
        parser.add_argument('app')

    def handle(self, *args, **options):
        app = options['app']
        self.stdout.write(app)
        from django.conf import settings
        self.stdout.write(settings.BASE_DIR)
        self.stdout.write("Creating API structure")

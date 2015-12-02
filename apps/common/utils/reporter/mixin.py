from django.db.models.loading import get_model

class Reporter(object):
    def __init__(self, app, model, fieldnames, serializer, update_ipstore=False):
        self.model = get_model(app, model)
        self.fieldnames = fieldnames
        self.serializer = serializer
        self.update_ipstore = update_ipstore

    def perform_ipstore_update(self):
        from apps.impressions.models import Impression
        from apps.warehouse.models import IPStore
        from plugins.cities.models import Country, PostalCode

        for imp in self.model.filter(meta__at_ip__isnull=False, meta__at_ip2geo__isnull=False):
            try:
                country_code = imp.meta['ip2geo']['country']['iso_code']
            except KeyError:
                country_code = None
                country = None

            if country_code:
                try:
                    country = Country.objects.get(code=country_code)
                except Country.DoesNotExist:
                    country = None

            try:
                postal_code = imp.meta['ip2geo']['postal']['code']
                postal_queryset = PostalCode.objects.filter(
                        code=postal_code,
                        country=country
                    )
                if postal_queryset.count() > 1:
                    postal_code_id = postal_queryset[0].id
                else:
                    postal_code_id = None

                ip, created = IPStore.objects.get_or_create(ip=imp.meta['ip'])
                if postal_code_id:
                    if not ip.postal_code_id:
                        ip.postal_code_id = postal_code_id
                        ip.save()
            except KeyError:
                pass



    def save(self, *args, **kwargs):
        pass


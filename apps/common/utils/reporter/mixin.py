from django.apps import apps

class Reporter(object):
    def __init__(self, app, model, fieldnames, serializer, update_ipstore=False):
        self.model = apps.get_model(app, model)
        self.fieldnames = fieldnames
        self.serializer = serializer
        self.update_ipstore = update_ipstore

    def perform_ipstore_update(self):
        """
        Summary:
            updates warehouse ipstore to all known ips, reverse geocodes the data
            and perform the warehouse.

        Returns:
            TYPE: None
        """
        queryset = self.model.objects.filter(
            meta__at_ip__isnull=False, meta__at_ip2geo__isnull=False
        )
        #self.update_warehouse_ipstore(queryset)
        self.reverse_geocode_ipstore(queryset)

    def update_warehouse_ipstore(self, queryset):
        from apps.warehouse.models import IPStore
        from plugins.cities.models import Country, PostalCode

        for q in queryset:
            try:
                country_code = q.meta['ip2geo']['country']['iso_code']
            except KeyError:
                country_code = None
                country = None

            if country_code:
                try:
                    country = Country.objects.get(code=country_code)
                except Country.DoesNotExist:
                    country = None

            try:
                postal_code = q.meta['ip2geo']['postal']['code']
                postal_queryset = PostalCode.objects.filter(
                        code=postal_code,
                        country=country
                    )
                if postal_queryset.count() > 0:
                    postal_code_id = postal_queryset[0].id
                else:
                    postal_code_id = None

                ip, created = IPStore.objects.get_or_create(ip=q.meta['ip'])
                if postal_code_id:
                    if not ip.postal_code_id:
                        ip.postal_code_id = postal_code_id
                        ip.save()
            except KeyError:
                pass

    def reverse_geocode_ipstore(self, queryset):
        from apps.warehouse.models import IPStore
        from googlemaps import Client
        from django.conf import settings
        import json

        gmaps = Client(key=settings.GOOGLE_GEOCODE_KEY)

        import datetime
        _now = datetime.datetime.now()

        for ip in IPStore.objects.filter(geocode__isnull=True):
            print '---'
            print ip.ip
            print '---'
            qs = queryset.filter(
                meta__at_ip=ip.ip).order_by('-added_on')
            print qs
            print '---'
            if qs.count() > 0:
                obj = qs[0]
            else:
                obj = None
            if obj:
                location = obj.meta['ip2geo']['location']
                ip.latitude = location['latitude']
                ip.longitude = location['longitude']
                result = gmaps.reverse_geocode((location['latitude'], location['longitude']))
                ip.geocode = result
                ip.save()
                print '---'
                print ip.ip
                print '---'
                print location
                print '---'
                print ip.geocode
                print '---'

    def save(self, *args, **kwargs):
        pass


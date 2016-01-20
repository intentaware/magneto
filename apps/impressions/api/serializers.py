from rest_framework import serializers
from apps.impressions.models import Impression
from apps.api.fields import JsonField


class ImpressionSerializer(serializers.ModelSerializer):
    #meta = JsonField()

    class Meta:
        model = Impression
        exclude = ('meta', )


class ImpressionCSVSerializer(ImpressionSerializer):
    visitor = serializers.SerializerMethodField()
    ip = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    postal_code = serializers.SerializerMethodField()
    nearest_address = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    screen = serializers.SerializerMethodField()
    navigator = serializers.SerializerMethodField()
    is_claimed = serializers.SerializerMethodField()

    def get_ipstore(self, obj):
        from apps.warehouse.models import IPStore
        ip = self.get_ip(obj)
        if ip:
            try:
                store = IPStore.objects.get(ip=ip)
            except IPStore.DoesNotExist:
                store = None
        else:
            store = None
        return store


    def get_visitor(self, obj):
        return obj.visitor.key


    def get_ip(self, obj):
        try:
            obj.meta['ip']
            return obj.meta['ip']
        except KeyError:
            return None


    def get_postal_code(self, obj):
        store = self.get_ipstore(obj)
        if store:
            lpc = store.long_postal_code
            if lpc:
                return lpc
            elif store.postal_code:
                return store.postal_code.code
            else:
                return None
        else:
            return None

    def get_city(self, obj):
        ip2geo = obj.meta.get('ip2geo', None)
        city = None
        if ip2geo:
            city = ip2geo['city']['names']['en']
        return city

    def get_nearest_address(self, obj):
        store = self.get_ipstore(obj)
        if store:
            a = store.nearest_address
            if a:
                return a
            else:
                return None
        else:
            return None

    def get_country(self, obj):
        ip2geo = obj.meta.get('ip2geo', None)
        country = None
        if ip2geo:
            country = ip2geo['country']['names']['en']
        return country

    def get_screen(self, obj):
        return obj.meta.get('screen', None)

    def get_navigator(self, obj):
        return obj.meta.get('navigator', None)

    def get_is_claimed(self, obj):
        if obj.coupon.claimed_on:
            return True
        else:
            return False

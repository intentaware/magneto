from rest_framework import serializers
from apps.impressions.models import Impression, ImpressionUser
from apps.api.fields import JsonField


class ImpressionSerializer(serializers.ModelSerializer):
    #meta = JsonField()

    class Meta:
        model = Impression
        exclude = ('meta', )


class ImpressionCSVSerializer(ImpressionSerializer):
    visitor = serializers.SerializerMethodField()
    ip = serializers.SerializerMethodField()
    postal_code = serializers.SerializerMethodField()
    nearest_address = serializers.SerializerMethodField()

    def get_ipstore(self, obj):
        ip = self.get_ip(obj)
        if ip:
            from apps.warehouse.models import IPStore
            return IPStore.objects.get(ip=ip)
        else:
            return None


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
            else:
                return store.postal_code.name
        else:
            return None

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




class ImpressionUserSerializer(serializers.ModelSerializer):
    #meta = JsonField()

    class Meta:
        model = ImpressionUser


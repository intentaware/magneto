from rest_framework import serializers
from plugins.cities.models import City

class CitySerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()

    class Meta:
        model = City
        exclude = ('region', 'subregion', 'alt_names', )

    def get_country(self, obj):
        return obj.country.name

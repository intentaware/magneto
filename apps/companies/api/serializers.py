from rest_framework import serializers

from apps.companies.models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ('users', )


class CircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circle
        exclude = ('added_on', 'updated_on',)

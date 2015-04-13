from rest_framework import serializers

from apps.companies.models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ('users', )

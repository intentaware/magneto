from rest_framework import serializers
from apps.companies.models import Company
from apps.users.models import User

class DashboardUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions']

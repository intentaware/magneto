from rest_framework import serializers

from apps.users.models import User
from apps.companies.models import Company, CompanyGroup, CompanyUser


class BaseRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=128)
    password1 = serializers.CharField(max_length=128)
    password2 = serializers.CharField(max_length=128)

    def validate_email(self, value):
        email = value.lower()
        try:
            User.objects.get(email=email)
            raise serializers.ValidationError('Email already exists')
        except User.DoesNotExist:
            return value

    def validate_password2(self, value):
        if value != self.data['password1']:
            raise serializers.ValidationError('Password Mismatch')
        else:
            return value


class UserRegistrationSerializer(serializers.Serializer):

    def save(self, **kwargs):
        email = self.validated_data('email')
        password = self.validated_data('password2')

        return User.objects.create_user(email, password)


class CompanyRegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)

    def save(self, **kwargs):
        name = self.validated_data('name')
        email = self.validated_data('email')
        password = self.validated_data('password2')

        user = User.objects.create_user(email=email, password=password)

        company = Company.objects.create(name=name)
        group = CompanyGroup.objects.create(name='Administrators', company=company)
        cu = CompanyUser.objects.create(
            user=user, company=company, group=group,
            is_owner=True, is_superuser=True, is_default=True)
        cu.set_default()
        return cu
from rest_framework import serializers

from apps.users.models import User
from apps.companies.models import Company, CompanyGroup, CompanyUser


class PasswordValidationSerializer(serializers.Serializer):
    password1 = serializers.CharField(max_length=128)
    password2 = serializers.CharField(max_length=128)

    def validate_password2(self, value):
        if value != self.initial_data['password1']:
            raise serializers.ValidationError('Password Mismatch')
        else:
            if len(value) < 8:
                raise serializers.ValidationError(
                    'Password too weak, must be 8 characters long')
            else:
                return value


class BaseRegistrationSerializer(PasswordValidationSerializer):
    email = serializers.EmailField(max_length=128)
    first_name = serializers.CharField(max_length=128, required=False)
    last_name = serializers.CharField(max_length=128, required=False)

    def validate_email(self, value):
        print value
        email = value.lower()
        try:
            User.objects.get(email=email)
            raise serializers.ValidationError('Email already exists')
        except User.DoesNotExist:
            return value


class UserRegistrationSerializer(BaseRegistrationSerializer):

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password2']

        return User.objects.create_user(email, password)


class CompanyRegistrationSerializer(BaseRegistrationSerializer):
    name = serializers.CharField(max_length=128)
    is_advertiser = serializers.BooleanField(required=False)
    is_publisher = serializers.BooleanField(required=False)

    def create(self, validated_data):
        name = validated_data['name']
        email = validated_data['email']
        password = validated_data['password2']
        try:
            is_publisher = validated_data['is_publisher']
        except:
            is_publisher = False

        try:
            is_advertiser = validated_data['is_advertiser']
        except:
            is_advertiser = False

        user = User.objects.create_user(
            email=email, password=password, first_name=validated_data['first_name'],
            last_name=validated_data['last_name'])

        company = Company.objects.create(
            name=name, is_advertiser=is_advertiser, is_publisher=is_publisher
        )
        group = CompanyGroup.objects.create(name='Administrators', company=company)
        cu = CompanyUser.objects.create(
            user=user, company=company, group=group,
            is_owner=True, is_superuser=True, is_default=True)
        cu.set_default()
        return cu

class LeadRegistrationSerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=128)
    user_name = serializers.CharField(max_length=512)
    email = serializers.EmailField(max_length=128)
    phone = serializers.CharField(max_length=128)
    role = serializers.CharField(max_length=128)

    def validate_email(self, value):
        email = value.lower()
        try:
            User.objects.get(email=email)
            raise serializers.ValidationError('Email already exists')
        except User.DoesNotExist:
            return value

    def create(self, validated_data):
        # TODO: when app machine is decommisioned in favour of live
        #       do migrations to accomodate phone number
        print validated_data
        user_name = validated_data['user_name']
        company_name = validated_data['company_name']
        email = validated_data['email']
        phone = validated_data['phone']
        role = validated_data['role']

        name = user_name.split(' ')
        first_name = name[0]

        if len(user_name) > 1:
            last_name = name[1]
        else:
            last_name = ''

        user = User.objects.create_user(
                email=email, password=None, first_name=first_name,
                last_name=last_name
            )

        company = Company.objects.create(
                name=company_name
            )

        group = CompanyGroup.objects.create(name='Administrators',
                company=company)

        company_user = CompanyUser.objects.create(
                company=company, group=group, user=user
            )

        return company_user



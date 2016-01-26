import factory
from apps.campaigns.models import *
from apps.companies.models import *
from apps.guages.models import *
from apps.users.models import *
from apps.finances.models import *


class CampaignFactory(factory.Factory):
    class Meta:
        model = Campaign

    name = "SampleSite"
    description = "Some words about campaign "
    budget = 600
    coupon_value = 10
    coupon_count = 5
    is_active = True

class CompaniesFactory(factory.Factory):
    class Meta:
        model = Company

    is_active = True
    is_advertiser = True
    publisher_key = "YufjaydQ_U2NQ2Qq8kogKA"
    advertiser_rate = 1.045
    payment_data = {'method' : 'bank', 'bank_name' : 'citi', 'acc_no' : '04596'}

class AssetFactory(factory.Factory):
    class Meta:
        model = Asset

    name = "Assests Name"
    url = "www.whatever.com/"
    key = "Xyshje12HjTv"

class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = 'Robert'
    last_name = 'Steve'
    email = 'selftest@example.com'
    password = 'password'

class BasePaymentModelFactory(factory.Factory):
    class Meta:
        model = BasePaymentModel

    amount = 30.25
    attempts = 3
    service_charges = 10
    taxes = 17
    gateway_response = {'status' : 'passed', 'amount' : '30', 'tax' : '17'}
    is_paid = True
    

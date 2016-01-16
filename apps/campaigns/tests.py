from django.test import TestCase
from models import *
import factory
from apps.companies.models import *
from django.test.client import Client

class CampaignFactory(factory.Factory):
    class Meta:
        model = Campaign

    name = "SampleSite"
    description = "Some words about campaign "


class CampaignTests(TestCase):
    campaign = CampaignFactory()
    rawName = "SampleSite"
    rawDesc = "Some words about campaign "
    c = Client()

    def test_name(self):
        name = self.campaign.name
        if name != self.rawName:
            return False

    def test_desc(self):
        desc = self.campaign.description
        if desc != self.rawDesc:
            return False

    def test_save(self):
        response = self.campaign.save()
        check = Campaign.objects.get(name="SampleSite")
        print type(check)

    def test_set_invoice(self):
        register = self.c.post('/users/auth/register/', {'name' : 'SampleName', 'email' : 'selftest@example.com', 'password1' : 'alphanum', 'password2' : 'alphanum'})
        company = Company.objects.get(name='SampleName')
        print company.id

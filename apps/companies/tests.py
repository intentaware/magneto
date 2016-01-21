from django.test import TestCase
from models import Company
import factory

class CompaniesFactory(factory.Factory):
    class Meta:
        model = Company

    is_active = True

class CompaniesTest(TestCase):
    company = CompaniesFactory()

    def test_is_active(self):
        self.assertEqual(self.company.is_active, True, "Company is_active test Failed.")
        print "Company is_active test Passed"





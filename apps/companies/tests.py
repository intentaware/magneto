from django.test import TestCase
from models import Company
import factory

class CompaniesFactory(factory.Factory):
    class Meta:
        model = Company

        



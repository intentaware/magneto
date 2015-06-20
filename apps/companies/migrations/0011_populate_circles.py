# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

circle_list = [
    "Agriculture",
    "Accounting",
    "Advertising",
    "Aerospace",
    "Aircraft",
    "Airline",
    "Apparel&Accessories",
    "Automotive",
    "Banking",
    "Broadcasting",
    "Brokerage",
    "Biotechnology",
    "CallCenters",
    "CargoHandling",
    "Chemical",
    "Computer",
    "Consulting",
    "ConsumerProducts",
    "Cosmetics",
    "Defense",
    "Department",
    "Education",
    "Electronics",
    "Energy",
    "Entertainment&Leisure",
    "ExecutiveSearch",
    "FinancialServices",
    "Food,Beverage&Tobacco",
    "Grocery",
    "HealthCare",
    "InternetPublishing",
    "InvestmentBanking",
    "Legal",
    "Manufacturing",
    "MotionPicture&Video",
    "Music",
    "NewspaperPublishers",
    "OnlineAuctions",
    "PensionFunds",
    "Pharmaceuticals",
    "PrivateEquity",
    "Publishing",
    "RealEstate",
    "Retail&Wholesale",
    "Securities&CommodityExchanges",
    "Service",
    "Soap&Detergent",
    "Software",
    "Stores",
    "Sports",
    "Technology",
    "Telecommunications",
    "Television",
    "Transportation",
    "VentureCapital",
    ]

def populate(apps, schema_editor):
    Circle = apps.get_model('companies', 'Circle')
    for c in circle_list:
        circle, created = Circle.objects.get_or_create(name=c)


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_company_circles'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]

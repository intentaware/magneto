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
    "Apparel & Accessories",
    "Automotive",
    "Banking",
    "Broadcasting",
    "Brokerage",
    "Biotechnology",
    "CallC enters",
    "Cargo Handling",
    "Chemical",
    "Computer",
    "Consulting",
    "Consumer Products",
    "Cosmetics",
    "Defense",
    "Department",
    "Education",
    "Electronics",
    "Energy",
    "Entertainment&Leisure",
    "Executive Search",
    "Financial Services",
    "Food,Beverage & Tobacco",
    "Grocery",
    "HealthCare",
    "InternetPublishing",
    "InvestmentBanking",
    "Legal",
    "Manufacturing",
    "MotionPicture & Video",
    "Music",
    "Newspaper Publishers",
    "Online Auctions",
    "Pension Funds",
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
    "Venture Capital",
    ]

def populate(apps, schema_editor):
    Circle = apps.get_model('metas', 'Circle')
    for c in circle_list:
        circle, created = Circle.objects.get_or_create(name=c)

class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0004_auto_parent_is_null_on_circle'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]

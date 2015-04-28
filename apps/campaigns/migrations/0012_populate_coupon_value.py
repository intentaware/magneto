# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def populate_coupon_value_field(apps, schema_editor):
    Coupon = apps.get_model('campaigns', 'Coupon')
    for c in Coupon.objects.all():
        c.value = c.campaign.coupon_value
        c.save


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0011_coupon_value'),
    ]

    operations = [
        migrations.RunPython(populate_coupon_value_field),
    ]

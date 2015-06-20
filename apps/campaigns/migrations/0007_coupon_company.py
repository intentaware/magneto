# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0012_auto_20150414_2027'),
        ('campaigns', '0006_auto_20150414_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='company',
            field=models.ForeignKey(related_name='coupons', blank=True, to='companies.Company', null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0016_company_stripe_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='stripe_customer_id',
        ),
        migrations.RemoveField(
            model_name='companygroup',
            name='permissions',
        ),
    ]

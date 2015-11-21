# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_ip_postalcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipstore',
            name='postal_code',
            field=models.ForeignKey(blank=True, to='cities.PostalCode', null=True),
        ),
    ]

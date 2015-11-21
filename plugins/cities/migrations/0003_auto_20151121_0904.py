# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_added_demographics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postalcode',
            name='income_household',
        ),
        migrations.RemoveField(
            model_name='postalcode',
            name='income_per_capita',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impressions', '0006_auto_20150331_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='impression',
            old_name='pubisher',
            new_name='publisher',
        ),
    ]

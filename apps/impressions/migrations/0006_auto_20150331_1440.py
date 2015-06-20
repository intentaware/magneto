# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impressions', '0005_auto_20150329_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='impression',
            old_name='user',
            new_name='visitor',
        ),
    ]

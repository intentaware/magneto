# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impressions', '0002_impression_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='impression',
            old_name='created_on',
            new_name='added_on',
        ),
    ]

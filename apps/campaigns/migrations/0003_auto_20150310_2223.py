# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20150310_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='created_on',
            new_name='added_on',
        ),
        migrations.RenameField(
            model_name='coupon',
            old_name='created_on',
            new_name='added_on',
        ),
    ]

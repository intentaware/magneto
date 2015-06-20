# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0012_populate_coupon_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='ends_on',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='starts_on',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

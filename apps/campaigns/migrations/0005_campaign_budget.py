# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0004_campaign_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='budget',
            field=models.DecimalField(default=0.0, max_digits=20, decimal_places=4),
            preserve_default=True,
        ),
    ]

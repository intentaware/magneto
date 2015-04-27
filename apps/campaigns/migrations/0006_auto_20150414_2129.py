# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0005_campaign_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='counter',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='ends_on',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='serve_limit',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='starts_on',
        ),
    ]

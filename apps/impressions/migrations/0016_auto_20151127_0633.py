# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impressions', '0015_auto_20151126_1257'),
    ]

    state_operations = [
        migrations.RemoveField(
            model_name='impressionuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='ImpressionUser',
        ),
    ]

    operations = [
        # After this state operation, the Django DB state should match the
        # actual database structure.
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]

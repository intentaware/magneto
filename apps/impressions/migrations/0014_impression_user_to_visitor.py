# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impressions', '0013_auto_20151120_0753'),
    ]

    # Add custom database_operations
    database_operations = [
        migrations.AlterModelTable('ImpressionUser', 'users_visitor'),
    ]

    # Don't modify the Django 'state' yet
    state_operations = [

    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150914_2106'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('key', django_extensions.db.fields.ShortUUIDField(editable=False, blank=True)),
                ('has_opted_out', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

    operations = [
        # By running only state operations, we are making Django think it has
        # applied this migration to the database. In reality, we renamed a
        # "cars_tires" table to "tires_tires" earlier.
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]

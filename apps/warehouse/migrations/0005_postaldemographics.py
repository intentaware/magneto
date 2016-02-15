# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_auto_20151121_0904'),
        ('warehouse', '0004_populate_ip_from_meta'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostalDemographics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('income_per_capita', models.PositiveIntegerField(null=True, blank=True)),
                ('income_household', models.PositiveIntegerField(null=True, blank=True)),
                ('postal_code', models.ForeignKey(to='cities.PostalCode')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

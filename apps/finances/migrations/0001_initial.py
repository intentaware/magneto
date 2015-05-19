# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import apps.finances.mixins
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0015_auto_20150515_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('amount', models.DecimalField(default=0.0, max_digits=20, decimal_places=4)),
                ('attempts', models.IntegerField(default=0)),
                ('attempted_on', models.DateTimeField(null=True, blank=True)),
                ('charged_on', models.DateTimeField(null=True, blank=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('company', models.ForeignKey(related_name='invoices', to='companies.Company')),
            ],
            options={
                'abstract': False,
            },
            bases=(apps.finances.mixins.Stripe, models.Model),
        ),
    ]

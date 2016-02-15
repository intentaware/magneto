# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0004_auto_20150606_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('amount', models.DecimalField(default=0.0, max_digits=20, decimal_places=4)),
                ('name', models.CharField(max_length=128)),
                ('matric_name', models.CharField(max_length=128)),
                ('duration', models.IntegerField(default=0, choices=[(1, b'Monthly'), (2, b'Quarterly'), (3, b'Yearly'), (0, b'Expires on Consumption')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

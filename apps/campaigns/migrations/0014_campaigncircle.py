# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0014_auto_20150414_2301'),
        ('campaigns', '0013_auto_20150428_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignCircle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign')),
                ('circle', models.ForeignKey(to='companies.Circle')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

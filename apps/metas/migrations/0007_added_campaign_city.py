# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0019_campaign_circles'),
        ('cities', '0001_initial'),
        ('metas', '0006_publisher_campaign_active_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignCity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign')),
                ('circle', models.ForeignKey(to='cities.City')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='campaigncity',
            unique_together=set([('campaign', 'circle')]),
        ),
    ]

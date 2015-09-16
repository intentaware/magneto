# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0018_removed_campaign_circle'),
        ('metas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignCircle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('campaign', models.ForeignKey(related_name='circles', to='campaigns.Campaign')),
                ('circle', models.ForeignKey(related_name='circles', to='metas.Circle')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='campaigncircle',
            unique_together=set([('campaign', 'circle')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0019_auto_20150914_2006'),
        ('metas', '0002_campaign_circle'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublisherCircle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('circle', models.ForeignKey(to='metas.Circle')),
                ('publisher', models.ForeignKey(to='companies.Company')),
            ],
        ),
        migrations.AlterField(
            model_name='campaigncircle',
            name='campaign',
            field=models.ForeignKey(to='campaigns.Campaign'),
        ),
        migrations.AlterField(
            model_name='campaigncircle',
            name='circle',
            field=models.ForeignKey(to='metas.Circle'),
        ),
        migrations.AlterUniqueTogether(
            name='publishercircle',
            unique_together=set([('publisher', 'circle')]),
        ),
    ]

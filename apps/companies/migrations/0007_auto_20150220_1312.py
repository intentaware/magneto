# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_compnay_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('name', models.CharField(max_length=256)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from=b'name', editable=False, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='compnay',
            name='users',
        ),
        migrations.AlterField(
            model_name='companygroup',
            name='company',
            field=models.ForeignKey(related_name='groups', to='companies.Company'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='companyuser',
            name='company',
            field=models.ForeignKey(related_name='memberships', to='companies.Company'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Compnay',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='companyuser',
            name='user',
            field=models.ForeignKey(related_name='memberships', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='companyuser',
            unique_together=set([('user', 'group', 'company')]),
        ),
        migrations.AddField(
            model_name='companygroup',
            name='company',
            field=models.ForeignKey(related_name='groups', to='companies.Company'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='companies.CompanyUser'),
            preserve_default=True,
        ),
    ]

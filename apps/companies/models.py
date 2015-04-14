from django.db import models

from django_extensions.db.fields import *
from jsonfield import JSONField

from apps.common.models import *

class Circle(TimeStamped):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Company(TimeStamped, SluggedFromName):
    is_active = models.BooleanField(default=False)

    is_advertiser = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)

    publisher_key = ShortUUIDField(blank=True, null=True)

    # number of impressions xxx amount will buy you
    # e.g campaign.budget * impression_mux = number of impression
    impressions_per_dollar = models.IntegerField(
        default=1000, help_text='No. of impressions generated against each USD')


    users = models.ManyToManyField('users.User', through='companies.CompanyUser')
    circles = models.ManyToManyField(Circle, through='companies.CompanyCircle')

    class Meta:
        verbose_name_plural = "companies"

    def get_target_campaigns(self, request):
        from apps.campaigns.models import Campaign
        return Campaign.objects.all().exclude(image=None).order_by('?')


class CompanyCircle(TimeStamped):
    company = models.ForeignKey(Company)
    circle = models.ForeignKey(Circle)

    class Meta:
        unique_together = ('company', 'circle')


class CompanyGroup(TimeStamped):
    name = models.CharField(max_length=128)
    company = models.ForeignKey('companies.Company', related_name='groups')
    permissions = JSONField(default="[]")


class CompanyUser(TimeStamped):
    user = models.ForeignKey('users.User', related_name='memberships')
    group = models.ForeignKey('companies.CompanyGroup', related_name='memberships')
    company = models.ForeignKey('companies.Company', related_name='memberships')

    # override default group permissions?
    is_owner = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # default membership for the views
    is_default = models.BooleanField(default=False)

    # check whether the membership is active or not
    is_active = models.BooleanField(default=True)

    # phone number
    phone = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        unique_together = ('user', 'group', 'company')

    def __unicode__(self):
        return '%s: %s' %(self.company.name, self.user)

    def set_default(self):
        if not self.is_active:
            self.user.memberships.all().update(is_active=False)
            self.is_active = True
            self.save()





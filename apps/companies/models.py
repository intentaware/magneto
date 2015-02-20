from django.db import models
from django_extensions.db.fields import *

from apps.common.models import *


class Compnay(TimeStamped, SluggedFromName):
    pass


class CompanyGroup(TimeStamped):
    company = models.ForeignKey('companies.Compnay', related_name='groups')


class CompanyUser(TimeStamped):
    user = models.ForeignKey('users.User', related_name='memberships')
    group = models.ForeignKey('companies.CompanyGroup', 
        related_name='memberships')
    company = models.ForeignKey('companies.Compnay', related_name='memberships')

    # override default group permissions?
    
    is_owner = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # default membership for the views
    
    is_default = models.BooleanField(default=False)


    def __unicode__(self):
        return '%s: %s' %(self.company.name, self.user.name)




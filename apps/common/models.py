from django.db import models
from django_extensions.db.fields import *

# Create your models here.


class BaseModel(models.Model):

    def reload(self):
        """
        Reloads the object from the database
        """
        return self.__class__._default_manager.get(pk=self.pk)

    def has_foreign_key(self, name):
        return hasattr(self, name) and getattr(self, name) is not None

    class Meta:
        abstract = True


class TimeStamped(BaseModel):
    """
    Provides created and updated timestamps on models.
    This will be the model inherited site wide because for SAAS
    added_on and updated_on are required to check the action on 
    a particular record
    """

    created_on = CreationDateTimeField()
    updated_on = ModificationDateTimeField()

    class Meta:
        abstract = True


class SluggedFromName(BaseModel):
    """
    Quickly provides a slug field and automate its creation from name
    """
    name = models.CharField(max_length=256)
    slug = AutoSlugField(populate_from='name', db_index=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class SulggedFromTitle(BaseModel):
    """
    quickly provides a slug field and automate its creation from title
    """
    title = models.CharField(max_length=256)
    slug = AutoSlugField(populate_from='title', db_index=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class ToCompany(BaseModel):
    """
    quickly creates a relationship to a company
    """
    company = models.ForeignKey('companies.Company', blank=True, null=True,
        related_name='%(class)ss')

    class Meta:
        abstract = True

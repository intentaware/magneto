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

from __future__ import unicode_literals
from django.db import models
from manager.models.category import Category


# Create your models here.
class Forum(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category)

    class Meta:
            app_label = 'manager'

    def __unicode__(self):
        return self.name

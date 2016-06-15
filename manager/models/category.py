from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
            app_label = 'manager'

    def __unicode__(self):
        return self.title

    def length_forums(self):
        return len(self.forum_set.all())

    def forums(self):
        return self.forum_set.all()

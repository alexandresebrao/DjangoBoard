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

    def length_topics(self):
        return len(self.topic_set.all())

    def last_post_date(self):
        return self.topic_set.last().datetime

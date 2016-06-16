from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from post.models.topic import Topic
from post.models.reply import Reply


# Create your models here.
class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField()

    class Meta:
            app_label = 'users'

    def posts(self):
        topics = Topic.objects.filter(user=self.user).count()
        replys = Reply.objects.filter(user=self.user).count()
        return topics + replys

from manager.models.forum import Forum
from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    user = models.ForeignKey(User)
    forum = models.ForeignKey(Forum)
    datetime = models.DateTimeField(auto_now=True)

    def length_replys(self):
        return len(self.reply_set.all())

    def replys(self):
        return self.reply_set.all().order_by('datetime')

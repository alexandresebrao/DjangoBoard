from django.contrib.auth.models import User
from django.db import models
from post.models.topic import Topic


class Reply(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)
    datetime = models.DateTimeField(auto_now=True)

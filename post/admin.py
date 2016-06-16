from django.contrib import admin
from post.models.topic import Topic
from post.models.reply import Reply

admin.site.register(Topic)
admin.site.register(Reply)
# Register your models here.

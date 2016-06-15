from django.contrib import admin
from manager.models.forum import Forum
from manager.models.category import Category

# Register your models here.
admin.site.register(Forum)
admin.site.register(Category)

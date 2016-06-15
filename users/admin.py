from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from models.userextension import UserExtension


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserExtensionInLine(admin.StackedInline):
    model = UserExtension
    can_delete = False
    verbose_name_plural = 'employee'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserExtensionInLine, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

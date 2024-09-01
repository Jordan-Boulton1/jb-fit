from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile

# Register your models here.


# Define an inline admin descriptor for the UserProfile model.
# This allows the UserProfile model to be edited within the User admin page.
class UserProfileInline(admin.StackedInline):
    # Specifies the model to be used as an inline within the User admin.
    model = UserProfile


# Extend the default UserAdmin to include UserProfileInline.
# This allows the UserProfile information to be displayed and edited
# on the same page as the User model in the admin interface.
class UserAdmin(BaseUserAdmin):
    # Adds the UserProfileInline to the User admin.
    inlines = [UserProfileInline]


# Unregister the default User admin from the Django admin site.
# This is necessary to override the
# default User admin with a customized version.
admin.site.unregister(User)

# Register the customized User admin that includes the UserProfileInline.
admin.site.register(User, UserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your custom User model so it shows up in the admin panel
admin.site.register(User, UserAdmin)

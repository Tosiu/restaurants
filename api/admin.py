from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import User, Restaurant, Visit

admin.site.register(User, UserAdmin)
admin.site.register(Restaurant)
admin.site.register(Visit)


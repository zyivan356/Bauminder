from django.contrib import admin
from .models import CustomUser, Like

admin.site.register(CustomUser)
admin.site.register(Like)

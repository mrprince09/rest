from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Musician

# Register your models here.
admin.site.register(Musician)
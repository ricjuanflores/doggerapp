from django.contrib import admin
from django.contrib.admin import site
from .models import Dog, User, Service
# Register your models here.
site.register(Dog)
site.register(User)
site.register(Service)
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Student, Theme, College_Event, Category, Program, Enroll])

from django.contrib import admin

# Register your models here.
from main.models import Task

# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Task)
from django.contrib import admin

# Register your models here.
from users.models import TaskUser

@admin.register(TaskUser)
class TaskUserAdmin(admin.ModelAdmin):
    pass
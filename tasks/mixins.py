from django.db.models.manager import BaseManager
from django.template.loader import render_to_string
from django.urls import reverse

from main.templatetags.task_tags import get_user_tasks
from tasks.models import Task

class TaskMixin:
    def render_tasks(self, request):
        user_tasks = get_user_tasks(request)
        context: dict[str, BaseManager[Task]] = {"tasks": user_tasks}
        
        return render_to_string(
            "tasks/includes/tasks_template.html", context=context, request=request
        )
from django.http import HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic import DeleteView, UpdateView

from tasks.models import Task
from tasks.mixins import TaskMixin
# Create your views here.

class TaskDeleteView(TaskMixin, View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(id=request.POST.get('task_id'))

        task.delete()

        response_data = {
            "task_items_html": self.render_tasks(request),
        }

        return JsonResponse(response_data)


class TaskUpdateView(TaskMixin, View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(id=request.POST.get('task_id'))

        task.is_done = (request.POST.get('is_done') != 'True')
        task.save()

        response_data = {
            "task_items_html": self.render_tasks(request),
        }

        return JsonResponse(response_data)
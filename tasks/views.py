from django.http import JsonResponse
from django.views import View

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

        # if not request.GET.get('q'):
        #     request.GET.get('q') = request.POST.get('q') if request.POST.get('q') else None

        response_data = {
            "task_items_html": self.render_tasks(request),
        }

        # if not request.POST.get('q'):
        #     # return redirect(request.META.get('HTTP_REFERER'))
        #     return HttpResponseRedirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
        
        return JsonResponse(response_data)
# from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from django.views.generic.base import TemplateView
# Create your views here.

from tasks.utils import get_user_tasks
from tasks.forms import TaskCreateForm

class MainView(TemplateView):
    template_name = "main/index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Главная",
            "tasks": get_user_tasks(self.request),
            "current_date": datetime.now().strftime("%d.%m.%Y"),
        })
        return context
    
    def post(self, request, *args, **kwargs):
        form = TaskCreateForm(data=request.POST)
        context = self.get_context_data(**kwargs)

        if request.user.is_authenticated:
            form.instance.user_id = request.user.id
        else:
            if request.session.session_key:
                form.instance.session_key = request.session.session_key

        if form.is_valid():
            form.save()
        else:
            context["form"] = form

        return self.render_to_response(context)
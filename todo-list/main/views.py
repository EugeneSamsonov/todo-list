# from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

from main.models import Task

class MainView(TemplateView):
    template_name = r"main\index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        return context

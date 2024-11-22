from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from tasks.models import Task
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form = UserLoginForm
    success_url = reverse_lazy('main:index')

    def get_success_url(self, request) -> str:
        redirect_url = request.POST.get('next', None)
        if redirect_url and redirect_url != reverse('users:logout'):
            return request.POST.get('next')
        return reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context
    
    def form_valid(self, form):
        session_key = self.request.session.session_key  
        user = form.get_user()
        
        if user:
            auth.login(self.request, user)

            if session_key:
                Task.objects.filter(session_key=session_key).update(user=user)

            return HttpResponseRedirect(self.get_success_url(self.request))

class UserRegistrationView(CreateView): #CreateView TemplateView
    template_name = "users/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("main:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        return context
    
    def form_valid(self, form):
        form.save()
        session_key = self.request.session.session_key  
        user = form.instance
        
        if user:
            auth.login(self.request, user)

            if session_key:
                Task.objects.filter(session_key=session_key).update(user=user)

            return HttpResponseRedirect(self.success_url)
    

class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = "users/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Профиль"
        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("main:index"))
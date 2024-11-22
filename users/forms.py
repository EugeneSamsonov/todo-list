from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import TaskUser

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = TaskUser
        fields = ["username", "password"]

    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = TaskUser
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(forms.ModelForm):

    class Meta:
        model = TaskUser
        fields = ["username", "first_name", "last_name", "email", "image"]
    
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    image = forms.ImageField(required=False)
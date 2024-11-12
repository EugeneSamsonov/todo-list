from django import forms

from tasks.models import Task

class TaskCreateForm(forms.ModelForm):
    text = forms.CharField()
    date = forms.DateField(required=True)
    session_key = forms.CharField(required=False, max_length=32)
    user_id = forms.IntegerField(required=False)

    class Meta:
        model = Task
        fields = ["text", "date", "user_id", "session_key"]
    
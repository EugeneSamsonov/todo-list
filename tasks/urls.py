from django.urls import path

from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('delete_task/', views.TaskDeleteView.as_view(), name='delete_task'),
    path('update_task/', views.TaskUpdateView.as_view(), name='update_task'),
    # path('add_task/', views.create_task, name='add_task'),
]
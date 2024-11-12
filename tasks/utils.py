from tasks.models import Task


def get_user_tasks(request):
    if request.user.is_authenticated:
        return Task.objects.filter(user_id=request.user.id)#.select_related('task')
    
    if not request.session.session_key:
        request.session.create()
    return Task.objects.filter(session_key=request.session.session_key)#.select_related('task')
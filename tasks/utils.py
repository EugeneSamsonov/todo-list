from main.utils import q_search
from tasks.models import Task


def get_user_tasks(request):
    result_query_set = Task.objects.all()

    if request.POST.get('q'):
        result_query_set = q_search(request.POST.get('q'))
    
    elif request.GET.get('q'):
        result_query_set = q_search(request.GET.get('q'))

    if request.user.is_authenticated:
        return result_query_set.filter(user_id=request.user.id)
    
    if not request.session.session_key:
        request.session.create()
    return result_query_set.filter(session_key=request.session.session_key)
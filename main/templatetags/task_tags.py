from django import template

from tasks.utils import get_user_tasks


register = template.Library()

@register.simple_tag()
def user_tasks(request):
    return get_user_tasks(request)

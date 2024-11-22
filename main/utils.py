from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
)

from tasks.models import Task


def q_search(query):

    if query == "":
        return Task.objects.all()

    vector = SearchVector("text", "date")
    squery = SearchQuery(query)
    result = (
        Task.objects.annotate(rank=SearchRank(vector, squery))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    return result

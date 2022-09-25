from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404

from app import settings
from task_manager.models import Task


def get_tasks(_request):
    page_number = _request.GET.get('page', 1)
    tasks = Task.objects.all()
    paginator = Paginator(tasks, settings.PAGINATION_POSTS_PER_PAGE)
    try:
        tasks = paginator.page(page_number)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    return tasks


def get_task_by_pk(pk):
    task = get_object_or_404(Task, pk=pk)
    return task

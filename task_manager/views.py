from django.shortcuts import render


# Create your views here.


def task_list(request):
    data = {}
    return render(request, 'task_list.html', data)


def task_detail(request):
    data = {}
    return render(request, 'task_detail.html', data)


def task_create(request):
    data = {}
    return render(request, 'task_create.html', data)


def task_update(request):
    data = {}
    return render(request, 'task_update.html', data)


def task_change_status(request):
    pass

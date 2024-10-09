from django.shortcuts import render

from justdoit.models import ToDo


def home(request):
    num_tasks = ToDo.objects.count()
    tasks = ToDo.objects.all()
    return render(
        request,
        'justdoit/home.html',
        {'num_tasks': num_tasks, 'tasks': tasks},
    )


def task_detail(request, task_slug: str):
    task = ToDo.objects.get(slug=task_slug)
    return render(request, 'justdoit/tasks/detail.html', dict(task=task))

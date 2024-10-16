from django.shortcuts import render

from tasks.models import Task

# from .forms import AddTaskForm


def tasklist(request):
    tasks = Task.objects.all()
    done_tasks = [task for task in tasks if task.done]
    pending_tasks = [task for task in tasks if not task.done]
    num_tasks = Task.objects.count()
    return render(
        request,
        'tasks/tasklist.html',
        {
            'num_tasks': num_tasks,
            'tasks': tasks,
            'done_tasks': done_tasks,
            'pending_tasks': pending_tasks,
        },
    )


def done(request, task_slug: str):
    tasks = Task.objects.all()
    slug = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/task_status.html', {'tasks': tasks, 'slug': slug})


def pending(request, task_slug: str):
    tasks = Task.objects.all()
    slug = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/task_status.html', {'tasks': tasks, 'slug': slug})


def add(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/add_task.html', {'tasks': tasks})


def toggle(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks_management.html', {'tasks': tasks})


def edit(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks_management.html', {'tasks': tasks})


def delete(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks_management.html', {'tasks': tasks})

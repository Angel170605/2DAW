from django.shortcuts import redirect, render
from django.utils.text import slugify

from tasks.models import Task

from .forms import AddTaskForm, EditTaskForm


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


def done(request):
    tasks = Task.objects.filter(done=True)
    return render(request, 'tasks/task_status.html', {'tasks': tasks})


def pending(request):
    tasks = Task.objects.filter(done=False)
    return render(request, 'tasks/task_status.html', {'tasks': tasks})


def add(request):
    if request.method == 'GET':
        form = AddTaskForm()
    else:
        if (form := AddTaskForm(data=request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    return render(request, 'tasks/add_task.html', dict(form=form))


def toggle(request, task_slug: str):
    tasks = Task.objects.all()
    slug = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/tasks_management.html', {'tasks': tasks, 'slug': slug})


def edit(request, task_slug: str):
    task = Task.objects.get(slug=task_slug)
    if request.method == 'GET':
        form = EditTaskForm()
    else:
        if (form := EditTaskForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    return render(request, 'tasks/tasks_management.html', {'task': task, 'form': form})


def delete(request, task_slug: str):
    tasks = Task.objects.all()
    slug = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/tasks_management.html', {'tasks': tasks, 'slug': slug})

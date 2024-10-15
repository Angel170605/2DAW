from django.shortcuts import redirect, render
from django.utils.text import slugify

from justdoit.models import ToDo

from .forms import AddTaskForm


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


def task_list(request):
    done_tasks = [task for task in ToDo.objects.all() if task.done]
    pending_tasks = [task for task in ToDo.objects.all() if not task.done]
    return render(
        request,
        'justdoit/tasks/tasklist.html',
        {'done_tasks': done_tasks, 'pending_tasks': pending_tasks},
    )


def add_task(request):
    if request.method == 'POST':
        if (form := AddTaskForm(request.POST)).is_valid():
            task = form.save(commit=False)

            task.slug = slugify(task.title)

            task.save()

            return redirect('justdoit:home')

    else:
        task = AddTaskForm()
    return render(request, 'justdoit/tasks/add_task.html')

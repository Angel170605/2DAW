from django.shortcuts import render

# Create your views here.
from echos.models import Echo


def echos(request):
    echos = Echo.objects.all()
    return render(request, 'echos/echos.html', {'echos': echos})


def detail(request, task_id: int):
    echo = Echo.objects.get(id=task_id)
    return render(request, {'echo': echo})


def edit(request, task_id: int):
    echo = Echo.objects.get(id=task_id)
    return render(request, {'echo': echo})


def delete(request, task_id: int):
    echo = Echo.objects.get(id=task_id)
    echo.delete()
    return render(request)

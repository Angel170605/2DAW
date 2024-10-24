from django.shortcuts import render

from echos.models import Echo


def echos(request):
    echos = Echo.objects.all()
    return render(request, 'echos/echos.html', {'echos': echos})


def detail(request):
    echo = Echo.objects.get(id)
    return render(request, {'echo': echo})


def edit(request):
    echo = Echo.objects.get(id)
    return render(request, {'echo': echo})


def delete(request):
    echo = Echo.objects.get(id)
    echo.delete()
    return render(request)

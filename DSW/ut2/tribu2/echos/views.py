from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from echos.models import Echo
from waves.models import Wave

from .forms import AddEchoForm, EditEchoForm


def echos(request):
    echos = Echo.objects.all()
    waves = Wave.objects.all()
    return render(request, 'echos.html', {'echos': echos, 'waves': waves})


def detail(request, echo_id: int):
    echo = Echo.objects.get(id=echo_id)
    return render(request, {'echo': echo})


@login_required
def add_echo(request):
    if request.method == 'GET':
        form = AddEchoForm()
    else:
        if (form := AddEchoForm(data=request.POST)).is_valid():
            echo = form.save(commit=False)
            echo.user = request.user
            echo.save()
            return redirect('echos:echos')
    return render(request, 'add_echo.html', dict(form=form))


def edit(request, echo_id: int):
    echo = Echo.objects.get(id=echo_id)
    if request.method == 'GET':
        form = EditEchoForm(instance=echo)
    else:
        if (form := EditEchoForm(request.POST, instance=echo)).is_valid():
            echo = form.save()
            echo.save
            return redirect('echos:echos')
    return render(request, 'edit_echo.html', {'echo': echo, 'form': form})


def delete(request, echo_id: int):
    echo = Echo.objects.get(id=echo_id)
    echo.delete()
    return redirect('echos:echos')

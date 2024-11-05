from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from echos.models import Echo
from waves.models import Wave

from .forms import AddEchoForm, EditEchoForm


def echos(request):
    echos = Echo.objects.all()
    return render(request, 'echos.html', {'echos': echos})


def detail(request, echo_id: int):
    echo = Echo.objects.get(id=echo_id)
    waves = Wave.objects.filter(echo=echo)
    n_waves = waves.count()
    return render(request, 'echo_detail.html', {'echo': echo, 'waves': waves, 'n_waves': n_waves})


@login_required
def add_echo(request):
    action = 'Crear echo'
    if request.method == 'GET':
        form = AddEchoForm()
    else:
        if (form := AddEchoForm(data=request.POST)).is_valid():
            echo = form.save(commit=False)
            echo.user = request.user
            echo.save()
            return redirect('echos:echos')
    return render(request, 'echo_form.html', dict(form=form, action=action))


def edit(request, echo_id: int):
    echo = Echo.objects.get(id=echo_id)
    action = 'Modificar echo'
    if request.method == 'GET':
        form = EditEchoForm(instance=echo)
    else:
        if (form := EditEchoForm(request.POST, instance=echo)).is_valid():
            echo = form.save()
            echo.save
            return redirect('echos:echos')
    return render(request, 'echo_form.html', {'echo': echo, 'form': form, 'action': action})


def delete(request, echo_id: int):
    echo = Echo.objects.get(id=echo_id)
    echo.delete()
    return redirect('echos:echos')

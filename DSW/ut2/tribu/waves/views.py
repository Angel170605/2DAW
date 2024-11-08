from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from echos.models import Echo
from waves.models import Wave

from .forms import AddWaveForm, EditWaveForm


def waves(request):
    waves = Wave.objects.all()
    return render(request, 'waves.html', {'waves': waves})


@login_required
def add_wave(request, echo_id: int):
    echo = Echo.objects.get(id=echo_id)
    action = 'Añadir Wave'
    if request.method == 'GET':
        form = AddWaveForm()
    else:
        if (form := AddWaveForm(data=request.POST)).is_valid():
            wave = form.save(commit=False)
            wave.user = request.user
            wave.echo = echo
            wave.save()
            return redirect('echos:detail', echo_id=echo_id)
    return render(request, 'wave_form.html', {'form': form, 'action': action})


def edit(request, echo_id: int, wave_id: int):
    wave = Wave.objects.get(id=wave_id)
    action = 'Modificar wave'
    if request.method == 'GET':
        form = EditWaveForm(instance=wave)
    else:
        if (form := EditWaveForm(request.POST, instance=wave)).is_valid():
            wave = form.save()
            wave.save
            return redirect('echos:detail', echo_id)
    return render(request, 'wave_form.html', {'wave': wave, 'form': form, 'action': action})


def delete(request, echo_id: int, wave_id: int):
    wave = Wave.objects.get(id=wave_id)
    wave.delete()
    return redirect('echos:detail', echo_id)

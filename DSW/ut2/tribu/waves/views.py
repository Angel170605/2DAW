from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from echos.models import Echo
from waves.models import Wave

from .forms import AddWaveForm


def waves(request):
    waves = Wave.objects.all()
    return render(request, 'waves.html', {'waves': waves})


@login_required
def add_wave(request, echo_id: int):
    echo = Echo.objects.get(id=echo_id)
    if request.method == 'GET':
        form = AddWaveForm()
    else:
        if (form := AddWaveForm(data=request.POST)).is_valid():
            wave = form.save(commit=False)
            wave.user = request.user
            wave.echo = echo
            wave.save()
            return redirect('echos:echos')
    return render(request, 'add_wave.html', dict(form=form))

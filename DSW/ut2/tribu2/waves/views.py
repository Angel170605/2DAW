from django.shortcuts import render

from waves.models import Wave


def waves(request):
    waves = Wave.objects.all()
    return render(request, 'waves.html', {'waves': waves})

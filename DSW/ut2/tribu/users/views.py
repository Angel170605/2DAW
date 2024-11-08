from django.shortcuts import render

from echos.models import Echo


def user_echos(request, user_id: int):
    echos = Echo.objects.filter(user=user_id)
    return render(request, 'user_echos.html', {'echos': echos})

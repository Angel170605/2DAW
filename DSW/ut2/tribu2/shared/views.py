from django.shortcuts import redirect, render

from .forms import SignupForm


def signup(request):
    form = SignupForm(request.POST or None)
    if (form := SignupForm(request.POST)).is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        #        login(request, user)
        return redirect('home')
    return render(request, 'signup.html', dict(form=form))

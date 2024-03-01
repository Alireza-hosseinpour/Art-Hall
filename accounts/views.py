from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/products')
        else:
            return redirect('accounts:login')
    return render(request, 'accounts/login.html', {})


@login_required
def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('/products')


def sign_up(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            return redirect('accounts:signup')
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/sign_up.html', context)

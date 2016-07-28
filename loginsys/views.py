from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def login(request):
    args = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            args['login_error'] = 'Invalid login or password!'
            return render(request, 'login.html', args)

    else:
        return render(request, 'login.html', args)


def register(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.method == 'POST':
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            usr = newuser_form.cleaned_data['username']
            pas = newuser_form.cleaned_data['password1']
            newuser = auth.authenticate(username=usr, password=pas)
            auth.login(request, newuser)
            return redirect('home')
        else:
            args['form'] = newuser_form
    return render(request, 'register.html', args)


def logout(request):
    auth.logout(request)
    return redirect('home')

from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def handler(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            if 'register' in request.POST:
                form = RegisterForm(request.POST)
                if form.is_valid():
                    user = form.save()
                else:
                    error = form.errors
            elif 'login' in request.POST:
                form = LoginForm(data=request.POST)
                if form.is_valid():
                    data = form.cleaned_data
                    user = authenticate(username=data['username'], password=data['password'])
                else:
                    error = f'Неверные данные пользователя'

            if 'error' in locals():
                messages.error(request, error)
            else:
                login(request, user)
                messages.success(request, 'Успешно' )
                return redirect('profile:index')
        register_form = RegisterForm()
        login_form = LoginForm()
        return render(request=request, template_name='authentication/register_and_login.html', context={'register_form': register_form, 'login_form': login_form})
    else:
        return redirect('main:index')


@login_required(login_url='authentication:index')
def log_out(request):
    logout(request)

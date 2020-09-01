from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        next = request.GET.get('next')
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect('/')

        context = {
            'form': form,
        }
        return render(request, "login.html", context)

def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        next = request.GET.get('next')
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            if next:
                return redirect(next)
            return redirect('/')

        context = {
            'form': form,
        }
        return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')
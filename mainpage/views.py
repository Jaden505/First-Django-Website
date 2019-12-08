from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from mainpage.models import Addition
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def home_view(request):
    form = AuthenticationForm(data=request.POST)
    user = form.get_user()
    return render(request, "main.html", {'form': user})

@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return render(request, "logout.html")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
             # Log user in
             user = form.get_user()
             login(request, user)
             return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
             # Log user in
            login(request, user)
            return redirect("/")

    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form})

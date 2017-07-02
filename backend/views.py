# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from forms import SignUpForm, LoginForm, IOForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from utlis.utlis import check


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print form
        if form.is_valid():
            form.save()
            print "Hey!"
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'form': form})

def payment(request):
    return render(request, 'payment.html')

def log_in(request):
    print "Hey!"
    if request.method == 'POST':
        print "hey!"
        form = LoginForm(request.POST)
        print form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            print username, " ", password

            user = authenticate(request, username, password)
            print user
            login(request, user)
            return render(request, 'home.html')

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def io(request):
    if request.method == 'POST':
        form = IOForm(request.POST)
        

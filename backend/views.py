# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from forms import SignUpForm, LoginForm, Input
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from utlis.utlis import check


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(request.POST)
        # print("\n\n")
        # print form
        # print(form.cleaned_data.get('username'))
        if form.is_valid():
            form.save()
            print "Hey!"
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(username, raw_password)
            return HttpResponseRedirect("login")

            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            #return redirect()
    else:
        form = SignUpForm()
    return render(request, 'index.html', {'form': form})

def payment(request):
    return render(request, 'payment.html')

def log_in(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect("home")
    print "Hey!"
    if request.method == 'POST':
        print "hey!"
        # form = LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = authenticate(username = username, password = password)
            login(request, user)
            return HttpResponseRedirect(home(request))
        else:
            return render(request, 'registration/login.html')
        # if form.is_valid():
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password1']
        #     print username, " ", password

            # user = authenticate(request, username, password)
            # print user
            # login(request, user)
            # return render(request, 'home.html')

    return render(request, 'registration/login.html')

def log_out(request):
    logout(request)
    return HttpResponseRedirect("login")

def home(request):
    if request.method == "POST":
        form = Input(request.POST)
        if form.is_valid():
            string = form.cleaned_data.get('secret_key')
            x = check(string)
            return render(request, 'output.html', {'key' : x})
    else:
        form = Input()
    return render(request, 'home.html', {'form' : form})

#def io(request):
#    if request.method == 'POST':
#        form = IOForm(request.POST)
        

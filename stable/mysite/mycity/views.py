from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Cities
from .models import UserType
from .models import User
from .forms import *
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.conf import settings



@login_required
def index(request):
    cities_all = Cities.objects.order_by('-title')[:5]
    template = loader.get_template('index.html')
    return render(request, 'index.html')


def register(request):
    template = loader.get_template('register.html')
    user_type_all = UserType.objects.order_by('-type_desc')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/index/')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})


def summary(request):
    template = loader.get_template('summary.html')
    return render(request, 'summary.html')


def model_form_upload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'File Uploaded Successfully')
	else:
		form = DocumentForm()
	return render(request, 'model_form_upload.html', {
		'form': form
		})

def administratorPage(request):
    cities_all = Cities.objects.order_by('-title')[:5]
    template = loader.get_template('administratorPage.html')
    return render(request, 'administratorPage.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

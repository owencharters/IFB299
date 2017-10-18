from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Cities
from .models import UserType
from .models import User
from .forms import *
from django.core.urlresolvers import reverse
from django.contrib import messages


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

def model_form_upload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
#			return HttpResponseRedirect('/index/')
			messages.add_message(request, messages.SUCCESS, 'File Uploaded Successfully')
	else:
		form = DocumentForm()
	return render(request, 'model_form_upload.html', {
		'form': form
		})

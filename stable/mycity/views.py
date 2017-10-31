from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.template import loader
from .models import *
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
        django_user_form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if django_user_form.is_valid() and profile_form.is_valid():
             try:
                 user = User.objects.create_user(request.POST.get(username), django_user_form.email, django_user_form.password)
             #django_user_form.user_id = profile_form.user_id
                 profile_form.save()
                 messages.success(request, ('Your profile was successfully updated!'))
             except IntegrityError as e:
                 return redirect("summary.html", {"Success": e.__cause__})
        else:
             messages.error(request, ('Please correct the error below.'))
    else:
        django_user_form = SignupForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {
        'user_form': django_user_form,
        'profile_form': profile_form,
})


def summary(request, button_id):
    template = loader.get_template('summary.html')
    summaryInfo = Hotels.objects.defer('hotel_id')
    if button_id == "hotels":
        summaryInfo = Hotels.objects.defer('hotel_id')
    elif button_id == "citiyinfo":
        summaryInfo = Libraries.objects.all()
    elif button_id == "Colleges":
        summaryInfo = Colleges.objects.all()
    elif button_id == "libraries":
        summaryInfo = Libraries.objects.all()
    elif button_id == "industries":
        summaryInfo = Industries.objects.all()
    else:
        summaryInfo = Cities.objects.all()
    return render(request, 'summary.html', {'summaryInfo': summaryInfo})


def profile(request):
    template = loader.get_template('profile.html')
    return render(request, 'profile.html')


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

def login(request):
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
    return render(request, 'login.html', {'form': form})
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
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            form.save(commit=True)
            return redirect('signedUpSuccessfully')
    else:
        form = SignupForm()

    return render(request, 'register.html', {'form': form})


def summary(request, button_id):
    template = loader.get_template('summary.html')
    summaryInfo = Hotels.objects.defer('hotel_id')

    # -- Button Management --
    if button_id == "hotels":
        summaryInfo = Hotels.objects.defer('hotel_id')
    elif button_id == "parks":
        summaryInfo = Parks.objects.all()
    elif button_id == "zoos":
        summaryInfo = Zoos.objects.all()
    elif button_id == "museums":
        summaryInfo = Museums.objects.all()
    elif button_id == "malls":
        summaryInfo = Malls.objects.all()
    elif button_id == "restaurants":
        summaryInfo = Restaurants.objects.all()
    elif button_id == "colleges":
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

def signedUpSuccessfully(request):
    template = loader.get_template('signedUpSuccessfully.html')
    return render(request, 'signedUpSuccessfully.html')
    return render(request, 'login.html', {'form': form})

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['title', 'body',])

        found_entries = Entry.objects.filter(entry_query).order_by('-pub_date')

    return render_to_response('search/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))



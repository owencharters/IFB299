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
#Index view
    template = loader.get_template('index.html')
    return render(request, 'index.html')

def register(request):
#Registration view, uses inbuild Django authentication
    template = loader.get_template('register.html')
    user_type_all = UserType.objects.order_by('-type_desc')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():  #checks individual fields vs requirements
            user = form.save() #
            user.set_password(user.password)
            form.save(commit=True)
            return redirect('signedUpSuccessfully')
    else:
        form = SignupForm()

    return render(request, 'register.html', {'form': form})


def summary(request, button_id):
#View for main dashboard. Returns table of results
#and first result firstitem to be used in template
#for map display
    template = loader.get_template('summary.html')
    summaryInfo = Hotels.objects.all()
	
    # -- Button Management --
    if button_id == "hotels":
        summaryInfo = Hotels.objects.all()
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
    firstitem = summaryInfo[:1].get()
    return render(request, 'summary.html', {'summaryInfo': summaryInfo,
	'firstitem': firstitem})


def profile(request):
#View for profile. Incomplete and using dummy data
    template = loader.get_template('profile.html')
    return render(request, 'profile.html')


def model_form_upload(request):
#View for file upload for admin map upload. Stores in media folder.
	if request.method == 'POST': 
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save() #saves data if using POST and form passes validation
			messages.add_message(request, messages.SUCCESS, 'File Uploaded Successfully')
	else:
		form = DocumentForm() #else clear form
	return render(request, 'model_form_upload.html', {
		'form': form
		})

def administratorPage(request):
    template = loader.get_template('administratorPage.html')
    return render(request, 'administratorPage.html')

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			form.save() #saves data if using POST and form passes validation
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1') #retrieves raw password from form
			user = authenticate(username=username, password=raw_password) #automatically hashes password and checks vs records
			login(request, user)

	return render(request, 'login.html')

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



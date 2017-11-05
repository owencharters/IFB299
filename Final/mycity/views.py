from django.shortcuts import render, redirect
from django.template import loader
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as dj_login, authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


@login_required
def index(request):
    cities_all = Cities.objects.order_by('-title')[:5]
    template = loader.get_template('index.html')
    return render(request, 'index.html')


def signup(request):
#Registration view, uses inbuild Django authentication
    if request.method == 'POST':
        form = SignupForm(request.POST)
        types = UserType.objects.all()
        if form.is_valid():
            user = form.save()
            user.refresh_from_db
            user.profile.user_type = form.cleaned_data.get('user_type')
            user.profile.home_city = form.cleaned_data.get('home_city')
            user.save()
            raw_pass = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_pass)
            dj_login(request, user)
            return redirect('signedUpSuccessfully')
    else:
        form = SignupForm()
        types = UserType.objects.all()
    return render(request, 'register.html', {'form': form, 'types': types})


def summary(request, button_id):
#View for main dashboard. Returns table of results
#and first result firstitem to be used in template
#for map display

    template = loader.get_template('summary.html')
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
        # - Report "Incorrect url" if url value matches none of the provided options
        raise ValueError("Incorrect url")
    # - First Item of table used for Google API
    firstitem = summaryInfo[:1].get()
    return render(request, 'summary.html', {'summaryInfo': summaryInfo, 'firstitem': firstitem})


def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        pass_form = PasswordChangeForm(request.user, request.POST)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        types = UserType.objects.all()
        if user_form.is_valid() and profile_form.is_valid() and pass_form.is_valid():
            user = pass_form.save()
            user_form.save()
            profile_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        pass_form = PasswordChangeForm(request.user)
        types = UserType.objects.all()
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'pass_form': pass_form,
        'types': types
    })


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


# Handles search functionality, receiving user query to sort through database
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

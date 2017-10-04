from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Cities
from .models import UserType
from .models import User
from .forms import UserForm
from django.core.urlresolvers import reverse

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

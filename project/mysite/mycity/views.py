from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Cities

def index(request):
    cities_all = Cities.objects.order_by('-title')[:5]
    template = loader.get_template('index.html')
    context = {
        'cities_all': cities_all,
        }
    return HttpResponse(template.render(context, request))


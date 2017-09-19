from django.shortcuts import render
from django.http import HttpResponse
from mycity.models import User

def index(request):
    return HttpResponse("Hello, world. You're at the MyCity index.")


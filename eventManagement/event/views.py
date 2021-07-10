from django.http import request
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import *


# Create your views here.


def home(request):
    events=College_Event.objects.all()
    context={'events':events}
    return render(request, 'event/home.html',context)



def login(request):
    return render(request, 'event/login.html')


def about(request):
    return render(request, 'event/about.html')


def contact(request):
    return render(request, 'event/contact.html')

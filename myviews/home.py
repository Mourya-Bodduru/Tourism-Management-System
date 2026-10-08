from django.shortcuts import render,redirect
from tour.models import *

def home(request):
    
    return render(request,'pages/home.html')


    
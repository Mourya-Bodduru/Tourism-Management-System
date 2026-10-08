from django.shortcuts import render , get_object_or_404 , redirect
from tour.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def details(request, pk):
    packages = get_object_or_404(CreatePackage, pk=pk)
    return render(request, 'pages/details.html', {'packages': packages})



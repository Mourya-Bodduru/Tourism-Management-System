from django.shortcuts import render 
from tour.models import *

def user_tourpackage(request):
    packages = CreatePackage.objects.all()
    context = {
        'packages': packages
    }
    return render(request, 'pages/user_tourpackage.html', context)
from django.shortcuts import render
from tour.models import *


def tour_package(request):
    packages = CreatePackage.objects.all()
    context = {
        'packages': packages
    }
    return render(request, 'pages/tour_package.html', context)


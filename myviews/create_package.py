from django.shortcuts import render,redirect
from tour.models import *
from django.contrib import messages

def packages(request):
    return render(request,'pages/create_package.html')

def create_package(request):
    if request.method == 'POST':
        package_name = request.POST.get('package_name')
        package_type = request.POST.get('package_type')
        package_location = request.POST.get('package_location')
        package_price = request.POST.get('package_price')
        package_features = request.POST.get('package_features')
        package_details = request.POST.get('package_details')
        package_image = request.FILES.get('package_image')  # Use request.FILES to get file data
        
        package = CreatePackage(
            package_name=package_name,
            package_type=package_type,
            package_location=package_location,
            package_price=package_price,
            package_features=package_features,
            package_details=package_details,
            package_image=package_image,
        )
        package.save()
        messages.info(request, "Package created..")
        
    
    return redirect('admin_dashboard')
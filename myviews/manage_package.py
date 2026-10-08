from django.shortcuts import render ,redirect
from tour.models import *
from django.contrib import messages

def manage_package(request):
    packages = CreatePackage.objects.all()
    return render(request, 'pages/manage_package.html', {'packages': packages})

def update_package(request,pk):
    package = CreatePackage.objects.get(id=pk)
    
    if request.method == 'POST':
        package.package_name = request.POST.get('package_name')
        package.package_type = request.POST.get('package_type')
        package.package_location = request.POST.get('package_location')
        package.package_price = request.POST.get('package_price')
        package.package_features = request.POST.get('package_features')
        package.package_details = request.POST.get('package_details')
        package.package_image = request.FILES.get('package_image') 
        package.save()
        messages.info(request, "Package is Updated...")
        return redirect('admin_dashboard')
    
    context = {
        'package': package
    }
    
    return render(request, 'pages/update_package.html', context)

def delete_package(request, id):
    entry = CreatePackage.objects.get(id=id)
    entry.delete()
    return redirect('admin_dashboard')
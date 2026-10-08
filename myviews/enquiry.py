from django.shortcuts import render,redirect
from tour.models import *
from django.contrib import messages

def enquiry(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        
        
        contact_form = Enquiry(
            username=username,
            email=email,
            mobile_no=mobile_no,
            subject=subject,
            description=description,
        )
        contact_form.save()
        messages.info(request, "Your enquiry will be seen by Admin and he may send reply to it..")
          

    return render(request, 'pages/enquiry.html')
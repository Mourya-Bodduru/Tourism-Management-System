from django.shortcuts import render,redirect  
from tour.models import *
from django.contrib import messages

def raised_ticket(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        email= request.POST.get('email')
        tour_name = request.POST.get('tour_name')
        location = request.POST.get('location')
        details = request.POST.get('details')
        new_instance = TicketRaised(
            username=username,
            email=email,
            tour_name=tour_name,
            location=location,
            details=details
        )
        new_instance.save()
        messages.info(request, "Your Raised ticket will be seen by Admin and he may send reply to it..")
        return redirect('user_dashboard')
    else:
        return render(request,'pages/raised_ticket.html')

    
def ticket_raised(request):
    return render(request,'pages/raised_ticket.html')
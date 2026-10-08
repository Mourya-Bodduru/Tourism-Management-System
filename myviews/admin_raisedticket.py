from django.shortcuts import render,redirect ,get_object_or_404 
from tour.models import *
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.contrib import messages 

def admin_raisedticket(request):
    ticket=TicketRaised.objects.all()
    return render(request,'pages/admin_raisedticket.html',{'ticket':ticket})

def send_reply_email_ticket(request,pk):
    if request.method == 'POST':
        reply_message = request.POST.get('reply_message')
        ticket = get_object_or_404(TicketRaised, pk=pk)
        recipient_email = ticket.email
        
        subject = 'Raised Ticket Reply'
        message = reply_message
        from_email = 'boddurumourya@example.com'  
        recipient_list = [recipient_email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.info(request, "Mail sent..")
            ticket.delete()
            return redirect('admin_dashboard')
        except Exception as e:
            return redirect('some_error_page')
    else:
        return redirect('some_error_page')
    

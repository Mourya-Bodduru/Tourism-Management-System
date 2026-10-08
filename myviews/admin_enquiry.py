from django.shortcuts import render ,redirect ,get_object_or_404
from tour.models import *
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.contrib import messages  

def admin_enquiry(request):
    enquiries = Enquiry.objects.all()
    return render(request, 'pages/admin_enquiry.html', {'enquiries': enquiries})


def send_reply_email(request,pk):
    if request.method == 'POST':
        reply_message = request.POST.get('reply_message')
        enquiry = get_object_or_404(Enquiry, pk=pk)
        recipient_email = enquiry.email
        subject = 'Enquiry Reply'
        message = reply_message
        from_email = 'boddurumourya@example.com'  
        recipient_list = [recipient_email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.info(request, "Mail sent..")
            
            enquiry.delete()
            return redirect('admin_dashboard')
        except Exception as e:
            return redirect('some_error_page')
    else:
        return redirect('some_error_page')
    

from django.shortcuts import render,redirect,get_object_or_404
from tour.models import UserRegister
from django.core.mail import send_mail

def manage_users(request):
    return render(request,'pages/manage_users.html')

def approve_todo(request):
    tasks = UserRegister.objects.all()
    context = {
        'tasks':tasks,
    }
    return render(request, 'pages/manage_users.html',context)

def approve(request, registration_id):
    registration = get_object_or_404(UserRegister, id=registration_id)
    registration.status = 1
    registration.save()
    
    subject = 'Registration has been approved..'
    message = 'Your registration has been approved. You may now proceed.'
    from_email = 'your_email@example.com'  
    to_email = registration.email  
    send_mail(subject, message, from_email, [to_email])
    
    return redirect('admin_dashboard')

def delete(request, registration_id):
    registration = get_object_or_404(UserRegister, id=registration_id)
    email = registration.email
    
    subject = 'OOPS..Registration rejected..'
    message = 'Sorry Buddy...Your registration has been rejected.'
    from_email = 'your_email@example.com'  
    to_email = email
    send_mail(subject, message, from_email, [to_email])
    
    registration.delete()
    
    return redirect('admin_dashboard')
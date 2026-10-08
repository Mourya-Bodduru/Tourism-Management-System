from django.shortcuts import render,redirect,get_object_or_404 
from tour.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if UserRegister.objects.filter(username=username).exists():
            member = UserRegister.objects.filter(username=username).first()
            request.session['email'] = member.email
            if member.password == password:
                if member.status == 1:
                    request.session['username'] = username
                    messages.info(request,"Successfully Logged in..")
                    return redirect('user_dashboard')
                    
                else:
                    messages.error(request, "Oops! Your account is not approved.")
            else:
                messages.error(request, "Password does not match.")
        else:
            messages.error(request, "Username does not exist.")
        
        return redirect('sign_in')  
    else:
        return render(request, 'pages/sign_in.html')


def book_now(request,package_id):
    if request.method == 'POST':
        package = CreatePackage.objects.get(id=package_id)
        package_name = package.package_name
        user_register = get_object_or_404(UserRegister, username=request.session.get("username"),email=request.session.get("email"))
        created = Bookings.objects.get_or_create(username=user_register,email=user_register,package_name=package)
        package=Bookings.objects.filter(package_name=package).values()
        email=user_register.email
        if created:
            subject = 'Booking Confirmation'
            message = f'Your tour was booked. Your booked tour is {package_name}'
            from_email = 'your@example.com'  
            recipient_list = [email]
            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=True)  
            except Exception as e:
                print(f"Failed to send email: {e}")
        else:
            messages.error(request, 'Booking already exists.') 
        messages.info(request, 'Booking successful. Confirmation email sent.')
        return redirect('thank_you')
    else:
        return redirect('error') 


def cancel(request, pk):
    if request.method == 'POST':
        booking = Bookings.objects.get(pk=pk)  
        print(booking)  
        print(booking.email)
        recipient_email = booking.username.email
        
        subject = 'Booking Cancellation'
        message = 'Your booking has been canceled.' 
        from_email = 'boddurumourya@gmail.com'  
        recipient_list = [recipient_email]
        
        try:
            send_mail(subject, message, from_email, recipient_list)
            
            booking.delete()  
            messages.info(request, "Cancellation email sent.")       
            return redirect('admin_dashboard')
            
        except Exception as e:

            return redirect('some_error_page')
    else:
        return redirect('some_error_page')
    
def user_dashboard(request):
    username=request.session['username']
    mem= UserRegister.objects.filter(username=username).values()[:1]
    return render(request,'pages/user_dashboard.html',{'mem':mem})

def bookings(request):
    all_bookings = Bookings.objects.all()
    
    context = {
        'cart_items': all_bookings
    }
    return render(request, 'pages/bookings.html', context)
    
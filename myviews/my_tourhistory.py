from django.shortcuts import render ,get_object_or_404, redirect
from tour.models import *
from django.contrib import messages

def history(request):
    email = request.session.get('email')
    user = get_object_or_404(UserRegister, email=email)
    tour = Bookings.objects.filter(email=user)
    context = {
        'cart_items': tour
    }
    return render(request, 'pages/my_tourhistory.html', context)

def cancel_booking(request,booking_id):
    booking = get_object_or_404(Bookings, id=booking_id)
    
    booking.delete()
    
    messages.success(request, 'Booking canceled successfully.')
    return redirect('user_dashboard')
    
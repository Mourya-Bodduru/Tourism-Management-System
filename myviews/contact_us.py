from django.shortcuts import render 
def contact_us(request):
    return render(request,'pages/contact_us.html')
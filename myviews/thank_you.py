from django.shortcuts import render 

def thank_you(request):
    return render(request,'pages/thank_you.html') 
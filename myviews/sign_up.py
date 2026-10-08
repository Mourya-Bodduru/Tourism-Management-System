from django.shortcuts import render,redirect
from tour.models import UserRegister
from django.contrib import messages

def sign_up(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile_no= request.POST.get('mobile_no')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.info(request, "Password does not match...")
            return redirect('sign_up')
        
        if UserRegister.objects.filter(email=email).exists():
            messages.info(request, "Email already exists...")
            return redirect('sign_up')
        else:
            user = UserRegister(username=username,email=email, mobile_no=mobile_no ,password=password)
            user.save()
            messages.info(request, "ヾ(＠⌒ー⌒＠)ノ...Registered Successfully...ヾ(＠⌒ー⌒＠)ノ")
            return redirect('sign_in') 
            
    else:
        return render(request, 'pages/sign_up.html')
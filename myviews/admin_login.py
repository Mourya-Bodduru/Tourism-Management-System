from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['superuser_email'] = user.email
            print(user.email)
            return redirect('admin_dashboard')
        else:
           
            messages.info(request, "User is not existed..")
            return render(request, 'pages/admin_login.html')
    else:
       
        return render(request, 'pages/admin_login.html')
    
def admin_logout(request):
    logout(request)
    if 'superuser_email' in request.session:
        del request.session['superuser_email']
    return redirect('admin_login')

@login_required
def admin_dashboard(request):
    superuser_email = request.session.get('superuser_email', None)
    return render(request,'pages/admin_dashboard.html')
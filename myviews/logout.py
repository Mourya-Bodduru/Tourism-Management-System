from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout

def logout_user(request):
    django_logout(request)
    return redirect('sign_in') 
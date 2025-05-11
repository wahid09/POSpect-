from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def get_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = auth.authenticate(username=email, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                # messages.success(request, 'You are now logged in.')
                return redirect('dashboard:dashboard')
            else:
                messages.error(request, 'Invalid Login credentials')
                return redirect('user:login')
    return render(request, 'user/login.html')


@login_required
def get_logout(request):
    logout(request)
    messages.info(request, 'You are now loggout.')
    return HttpResponseRedirect(reverse('user:login'))

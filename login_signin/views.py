from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def indexPage(request):
    return render(request, 'index.html')

def registerPage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            form = CustomUserCreationForm()
        return render(request, 'register.html',{'form': form})

def loginPage(request):
    return render(request, 'login.html')

def profilePage(request):
    return render(request, 'profile.html')

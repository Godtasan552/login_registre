from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import logout


def indexPage(request):
    return render(request, 'index.html')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, "Please enter both username and password")
            return render(request, 'login.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if not all([username, email, password, confirm_password]):
            messages.error(request, 'Please fill out all fields.')
            return render(request, 'register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'register.html')
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')
        user = User.objects.create_user(
            username=username, email=email, password=password)
        UserProfile.objects.create(user=user)
        messages.success(request, 'User created successfully')
        return redirect('login')
    return render(request, 'register.html')


def profilePage(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Create a new UserProfile instance for the user
        user_profile = UserProfile.objects.create(user=request.user)

    form = UserProfileForm(instance=user_profile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')

    return render(request, 'profile.html', {'profile': user_profile, 'form': form})


def logoutPage(request):
    logout(request)
    return redirect('login')

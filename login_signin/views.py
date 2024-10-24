from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _
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
            messages.success(request, _('สมัครสมาชิกสำเร็จ! ยินดีต้อนรับเข้าสู้ระบบ'))
            return redirect('profile')
        else:
            messages.error(request, _('กรุณาแก้ไขข้อผิดพลาด'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html',{'form': form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method. == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not

def profilePage(request):
    return render(request, 'profile.html')

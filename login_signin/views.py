from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import CustomUserCreationForm
from django.contrib.auth import logout  # เพิ่มการนำเข้าตรงนี้
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
    
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, _(f'ยินดีต้อนรับกลับ {username}!'))
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('profile')
            else:
                messages.error(request, _('ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง'))
        else:
            messages.error(request, _('กรุณากรอกข้อมูลให้ถูกต้อง'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, _('คุณได้ออกจากระบบเรียบร้อยแล้ว'))
    return redirect('login')

@login_required
def profilePage(request):
    if request.method == 'POST':
        messages.success(request, _('อัพเดทโปรไฟล์สำเร็จ'))
    return render(request, 'profile.html')
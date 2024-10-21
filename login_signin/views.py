from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import login, authenticate


def indexPage(request):
    return render(request, 'index.html')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            return HttpResponse("Please enter both username and password")
        
        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
                return HttpResponse("Login failed. Please try again.")  # เพิ่มกรณีผู้ใช้ไม่ถูกต้อง
    return render(request, 'login.html')



def registerPage(request):
    return render(request, 'register.html')


def profilePage(request):
    return render(request, 'profile.html')

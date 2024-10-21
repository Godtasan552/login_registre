from django.shortcuts import render,HttpResponse

def indexPage(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):
    return render(request, 'register.html')

def profilePage(request):
    return render(request, 'profile.html')

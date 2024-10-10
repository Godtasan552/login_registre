from django.shortcuts import render,HttpResponse

def indexPage(request):
    return render(request, 'index.html'),

# Create your views here.

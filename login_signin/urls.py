from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='index'),
    path('login/',views.loginPage, name='login'),
    path('profile/',views.profilePage, name='profile'),
    path('register/',views.registerPage, name='register'),
]

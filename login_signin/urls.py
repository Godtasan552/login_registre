from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.indexPage, name='index'),
    path('login/',views.loginPage, name='login'),
    path('register/',views.registerPage, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profilePage, name='profile'),
    
]

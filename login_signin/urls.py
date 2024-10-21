from django.urls import path
from .views import indexPage, loginPage, registerPage, profilePage, logoutPage

urlpatterns = [
    path('', indexPage, name='index'),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('profile/', profilePage, name='profile'),
    path('logout/', logoutPage, name='logout'),
]
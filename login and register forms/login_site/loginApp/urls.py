from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('registerpage', views.registerpage, name='registerpage'),
    path('register', views.handlesignup, name='handlesignup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
]

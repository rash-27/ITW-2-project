from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('login/',views.loginpage,name='loginpage'),
    path('register/',views.registerpage,name='registerpage'),
]

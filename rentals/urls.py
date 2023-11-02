from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('login/',views.loginpage,name='loginpage'),
    path('logout/',views.logout_,name='logout'),
    path('register/',views.registerpage,name='registerpage'),
    path('register/<user>',views.completeregister,name='complete-registration'),
    path('<user>/',views.userhome,name='userHomePage'),

]

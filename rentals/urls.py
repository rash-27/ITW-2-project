from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('login/',views.loginpage,name='loginpage'),
    path('logout/',views.logout_,name='logout'),
    path('register/',views.registerpage,name='registerpage'),
    path('register/<user>/',views.completeregister,name='complete-registration'),
    path('<user>/',views.userhome,name='userHomePage'),
    path('<user>/Rent-a-ride/',views.rentaride,name='rent a ride'),
    path('<user>/Update/',views.update,name='Update'),
    path('<user>/Transactions/',views.seeTransactions,name='See Transactions'),
    path('<user>/Book-a-ride/',views.bookaride,name='book a ride'),
    path('<user>/Book-a-ride/status',views.bookingstatustake,name='booking Status Take'),
    path('<user>/Rent-a-ride/status',views.bookingstatusgive,name='renting Status Take'),
    path('<user>/Book-a-ride/accept/<username>/',views.bookingaccept,name='Accepting Status'),
    path('<user>/Book-a-ride/accept/<username>/review',views.review,name='Review'),
    path('<user>/Book-a-ride/accept/<username>/confirm',views.confirm,name='Confirm')
]


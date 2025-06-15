from .views import Register,Login,Home,Logout,Dashboard,Donor,DonorDetails,reset_donor_form,reset_password_view
from django.urls import path

urlpatterns=[
       path("",Home,name='Home'),
       path("Login/",Login,name='Login'),
       path("Logout/",Logout,name='Logout'),
       path("Register/",Register,name='Register'),
       path("Dashboard/",Dashboard,name='Dashboard'),
       path("Donor/",Donor,name='Donor'),
       path("DonorDetails/",DonorDetails,name='DonorDetails'),
       path("reset_donor_form/",reset_donor_form,name='reset_donor_form'),
       path("reset_password_view/",reset_password_view,name='reset_password_view'),
]
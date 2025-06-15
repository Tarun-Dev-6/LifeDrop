from .views import Home1,Logout,Register,Login,Dashboard
from django.urls import path

urlpatterns=[
       path("Home/",Home1,name='Home'),
       path("Login/",Login,name='Login'),
       path("Logout/",Logout,name='Logout'),
       path("Register/",Register,name='Register'),
       path("Dashboard/",Dashboard,name='Dashboard'),
]
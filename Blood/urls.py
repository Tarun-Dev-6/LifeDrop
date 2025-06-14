from .views import Home,Logout,Register,Login,Dashboard
from django.urls import path

urlpatterns=[
       path("Home/",Home,name='Home'),
       path("Login/",Login,name='Login'),
       path("Logout/",Logout,name='Logout'),
       path("Register/",Register,name='Register'),
       path("Dashboard/",Dashboard,name='Dashboard'),
]
from django.urls import path
from .views import  home,register


urlpatterns=[
# path("home/",home,name="home"),
path("register/",register,name='register'),
path('',home, name='home'), 
]


 

# from django.urls import path
# from myapp2 import views

# urlpatterns = [
#     path('registers/', views.registers, name='registers'), ]

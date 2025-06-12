from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
# def home(request):
# 	return render(request,'myapp2/home.html')
def register(request):
	if request.method=="POST":
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		user=User.objects.create_user(username=username,email=email,password=password)
		user.save()
		return redirect('home')
	return render(request,'myapp2/register.html')



def login_user(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect("home")
		else:
			return render(request,'myapp2/login.html')
	return render(request,'myapp2/login.html')

def logout_user(request):
	logout(request)
	return redirect('home')

from django.shortcuts import render 
from .models import CarouselImage 
 
def home(request): 
    images = CarouselImage.objects.all() 
    return render(request, 'myapp2/home.html', {'images': images})


# from django.shortcuts import render, redirect
# from .forms import RegistrationForm

# def registers(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the user data
#     else:
#         form = RegistrationForm()

#     return render(request, 'myapp2/register.html', {'form': form})

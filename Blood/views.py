from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from base.models import DonorDetails
from django.contrib import messages
# Create your views here.


def Home(request):
    return render(request,'Blood/home.html')

def Login(request):
    if request.method == "POST":
        identifier = request.POST.get("identifier")
        password = request.POST.get("password")

        # Try to get user by email, else fallback to username
        try:
            user_obj = User.objects.get(email=identifier)
            username = user_obj.username
        except User.DoesNotExist:
            username = identifier  # Assume it's a username

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Dashboard")  # Redirect to your dashboard or homepage
        else:
            return render(request, "Blood/login.html", {"error": "Invalid username/email or password."})

    return render(request, "Blood/login.html")

def Logout(request):
    logout(request)  # This logs out the user
    return redirect('Home')  # Redirect to login page (or home page)


def Register(request):
    if request.method == "POST":
        username = request.POST.get('username')  # New field
        name = request.POST.get('fullName')
        blood_group = request.POST.get('bloodGroup')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        mobile = request.POST.get('mobile')
        state = request.POST.get('state')
        city = request.POST.get('city')

        # Password match check
        if password != confirm_password:
            return render(request, 'Blood/register.html', {
                'error': 'Passwords do not match.'
            })

        # Username and email uniqueness check
        if User.objects.filter(username=username).exists():
            return render(request, 'Blood/register.html', {
                'error': 'Username already taken.'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'Blood/register.html', {
                'error': 'Email already registered.'
            })

        # Create user with actual username
        user = User.objects.create_user(username=username,email=email,password=password
        )

        # Create donor record linked to the user
        donor = DonorDetails.objects.create(
            user=user,
            full_name=name,
            blood_group=blood_group,
            mobile=mobile,
            state=state,
            city=city
        )

        messages.success(request, "Registration successful! Please log in.")
        return redirect('Login')

    return render(request, 'Blood/register.html')


def Dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, "Incorrect Username or Password.")
        return redirect('Login')

    if not DonorDetails.objects.filter(user=request.user).exists():
        # User is not linked to DonorDetails
        messages.error(request, "Access denied. You are not registered as a donor.")
        return redirect('Login')  # Redirect to login or a custom error page

    # If donor exists, load the dashboard
    return render(request, 'Blood/dashboard.html')


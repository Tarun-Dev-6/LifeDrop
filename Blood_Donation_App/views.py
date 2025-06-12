from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import  DonorDetails1
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password

def Register(request):
    if request.method == "POST":
        username = request.POST.get('email')  # Using email as username
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        blood_group = request.POST.get('bloodGroup')
        age = request.POST.get('age')
        state = request.POST.get('state')
        city = request.POST.get('city')

        # Validation: Check for required fields
        if not all([name, email, password, phone, blood_group, age, state, city]):
            return render(request, 'Blood_Donation_App/register.html', {
                'error': 'All fields are required.'
            })

        # Password and email uniqueness checks
        if User.objects.filter(username=username).exists():
            return render(request, 'Blood_Donation_App/register.html', {
                'error': 'An account with this email already exists.'
            })

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = name
        user.save()

        # Create donor profile
        donor = DonorDetails1.objects.create(
            user=user,
            phone=phone,
            blood_group=blood_group,
            age=age,
            state=state,
            city=city
        )
        messages.success(request, "Registration successful! Please log in.")
        return redirect('Login')  # Make sure 'login' is the name of your login URL pattern

    return render(request, 'Blood_Donation_App/register.html')





def Login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("Home")  # Redirect to your dashboard or homepage
        else:
            messages.error(request, "Invalid email or password.")
            return redirect("Login")  # or just re-render the same template

    return render(request, "Blood_Donation_App/login.html")

def Logout(request):
    logout(request)  # This logs out the user
    return redirect('Home')  # Redirect to login page (or home page)


def Home(request):
    return render(request, "Blood_Donation_App/index.html")


def Donor(request):
    return render(request, "Blood_Donation_App/donor.html")

def DonorDetails(request):
    if request.method == "POST":
        user = request.user

        # Detect if password fields are in the form submission
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')

        if current_password or new_password or confirm_password:
            # Handle password change logic only if these fields are submitted
            if not user.check_password(current_password):             
                messages.error(request, "Current password is incorrect.", extra_tags='password')
                return redirect("DonorDetails")

            if new_password != confirm_password:
                messages.error(request, "New passwords do not match.", extra_tags='password')
                return redirect("DonorDetails")

            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully.", extra_tags='password')
            return redirect("DonorDetails")

        # Handle profile update only if password fields are not submitted
        user.first_name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.profile.phone = request.POST.get("phone")
        user.profile.age = request.POST.get("age")
        user.profile.blood_group = request.POST.get("bloodGroup")
        user.profile.state = request.POST.get("state")
        user.profile.city = request.POST.get("city")

        emergency_status = request.POST.get("availableForEmergency")
        user.profile.available_for_emergency = emergency_status == "on"

        user.save()
        user.profile.save()

        messages.success(request, "Profile updated successfully.", extra_tags='profile')
        return redirect("DonorDetails")

    return render(request, "Blood_Donation_App/donor-details.html")


def reset_donor_form(request):
    messages.error(request, "Changes Not Saved", extra_tags='profile')
    return redirect('DonorDetails')

def Dashboard(request):
    blood_group = request.GET.get('blood_group')
    state = request.GET.get('state')
    city = request.GET.get('city')

    donors = DonorDetails1.objects.none()  # Default to empty

    if blood_group or state or city:
        donors = DonorDetails1.objects.all()

        if blood_group:
            donors = donors.filter(blood_group=blood_group)
        if state:
            donors = donors.filter(state=state)
        if city:
            donors = donors.filter(city=city)

        if request.user.is_authenticated:
            donors = donors.exclude(user=request.user)


    context = {
        'donors': donors,
        'search_params': {
            'blood_group': blood_group,
            'state': state,
            'city': city,
        }
    }
    return render(request, 'Blood_Donation_App/dashboard.html', context)



def reset_password_view(request):
    if request.method == "POST":
        email = request.POST.get('resetEmail')
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "No user found with this email.")
            return redirect("Login")

        if not check_password(current_password, user.password):
            messages.error(request, "Current password is incorrect.")
            return redirect("Login")

        if new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
            return redirect("Login")

        user.set_password(new_password)
        user.save()
        messages.success(request, "Password changed successfully. You can now log in.")
        return redirect("Login")

    return render(request, "Blood_Donation_App/login.html")

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import studentdetails,DonorDetails
from .forms import DonorForm,EmailForm,studentdetailsForm
from django.contrib import messages
# Create your views here.
def demo(request):
    return HttpResponse('HELLO')

def std(request):
    stddetails=studentdetails.objects.all()
    details={'stddetails' : stddetails}
    return render(request,'base/stddetails.html',details)

def Donor(request):
    Donordetails=DonorDetails.objects.all()
    context={'Donordetails' : Donordetails}
    return render(request,'base/Donordetails.html',context)




def donor_registration(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the data to the DonorDetails model
            return redirect('Donor')  # Redirect to a success page (you need to define it)
        else:
            # If the form is not valid, it will render again with error messages
            return render(request, 'base/register.html', {'form': form})
    
    else:
        form = DonorForm()
        return render(request, 'base/register.html',{'form': form})
    
def email(request):
    form = EmailForm()
    return render(request,'base/email.html',{'form': form})

def form(request):
    form = studentdetailsForm()
    return render(request,'base/stddetailsform.html',{'form': form})

def edit_student(request, id):
    student = get_object_or_404(studentdetails, pk=id)
    if request.method == 'POST':
        form = studentdetailsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('std')  # Replace with your actual view name
    else:
        form = studentdetailsForm(instance=student)
    return render(request, 'base/stddetailsform.html', {'form': form})


def delete_student(request, id):
    student = get_object_or_404(studentdetails, pk=id)
    student.delete()
    return redirect('std')  # Replace with your actual view name
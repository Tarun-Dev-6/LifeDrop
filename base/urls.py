from django.urls import path
from .views import demo,std,Donor,donor_registration,email,form,edit_student,delete_student

urlpatterns=[
    path('demo-function/',demo),
    path('student-details/',std,name='std'),
    path('Donor-Details/',Donor,name='Donor'),
    path('Donor-Registration/',donor_registration,name='donor_registration'),
    path('Email/',email,name='email'),
    path('form/',form),
    path('edit/<int:id>/', edit_student, name='edit_student'),
    path('delete/<int:id>/', delete_student, name='delete_student'),
]
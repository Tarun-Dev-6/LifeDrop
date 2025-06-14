from django.contrib import admin

# Register your models here.
from .models import studentdetails
from .models import DonorDetails

admin.site.register(studentdetails)
admin.site.register(DonorDetails)
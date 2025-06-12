from django.db import models
from django.contrib.auth.models import User

class DonorDetails1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=3, choices=[
        ("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"),
        ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-"),
    ])
    age = models.PositiveIntegerField()
    state = models.CharField(max_length=50, choices=[
        ("Andhra Pradesh", "Andhra Pradesh"), ("Bihar", "Bihar"),
        ("Delhi", "Delhi"), ("Gujarat", "Gujarat"), ("Karnataka", "Karnataka"),
        ("Kerala", "Kerala"), ("Maharashtra", "Maharashtra"),
        ("Punjab", "Punjab"), ("Tamil Nadu", "Tamil Nadu"),
        ("Uttar Pradesh", "Uttar Pradesh"),
    ])
    city = models.CharField(max_length=50)
    registered_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.blood_group})"
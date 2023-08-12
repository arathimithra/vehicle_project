from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_superadmin = models.BooleanField('Is superadmin',default=False)
    is_customer = models.BooleanField('Is customer',default=False)
    is_admin = models.BooleanField('Is admin',default=False)


class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=200, null=True, blank=True)
    vehicle_type = models.CharField(max_length=200, null=True, blank=True)
    vehicle_model = models.CharField(max_length=500, null=True, blank=True)
    vehicle_description = models.TextField()

    def __str__(self):
        return self.vehicle_number

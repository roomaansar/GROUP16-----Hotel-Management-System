from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    contact = models.IntegerField(default = 1234567890)
    birth_date = models.DateField(default = timezone.now)
    is_manager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

class Manager(models.Model):
    """Model definition for Manager."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hotel = models.ForeignKey('hotels.Hotel', on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of Manager."""
        return self.user.username

class Customer(models.Model):
    """Model definition for Customer."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    wallet = models.IntegerField(default = 10000)

    def __str__(self):
        """Unicode representation of Customer."""
        return self.user.username



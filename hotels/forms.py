from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Booking
from .models import Hotel,Room
from django.utils import timezone

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'begin_time', 'end_time', 'num_rooms']
        

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    location = forms.CharField(required=True)
    hotel_name = forms.CharField(required=True)
    hotel_email = forms.EmailField(required=True)
    email = forms.EmailField(required=True)
    contact = forms.CharField(required=True)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from hotels.models import Hotel
from .models import User, Manager, Customer

class ManagerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    contact = forms.IntegerField()
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    hotel = forms.ModelChoiceField(
        queryset=Hotel.objects.all(),
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.contact = self.cleaned_data.get('contact')
        user.birth_date = self.cleaned_data.get('birth_date')
        user.save()
        student = Manager.objects.create(user=user, hotel=self.cleaned_data.get('hotel'))
        return user

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    contact = forms.IntegerField()
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.contact = self.cleaned_data.get('contact')
        user.birth_date = self.cleaned_data.get('birth_date')
        if commit:
            user.save()
            student = Customer.objects.create(user=user)
        return user

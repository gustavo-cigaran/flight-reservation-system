from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Reservation, Airplane, Flight, Customer

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'flight', 'seat_number']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-select'}),
            'flight': forms.Select(attrs={'class': 'form-select'}),
            'seat_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 12',
                'min': '1'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        flight = cleaned_data.get('flight')

        if flight:
            reservations = Reservation.objects.filter(flight=flight)
            if self.instance.pk:
                reservations = reservations.exclude(pk=self.instance.pk)
            if reservations.count() >= flight.airplane.capacity:
                raise ValidationError("O voo já atingiu a capacidade máxima de reservas.")
            
            return cleaned_data

class AirplaneForm(forms.ModelForm):
    class Meta:
        model = Airplane
        fields = ['identifier', 'capacity']
        widgets = {
            'identifier': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: PR-GUQ'
            }),
            'capacity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 150',
                'min': '1'
            }),
        }

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['airplane', 'origin', 'destination', 'departure_time']
        widgets = {
            'airplane': forms.Select(attrs={'class': 'form-select'}),
            'origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: São Paulo'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Rio de Janeiro'}),
            'departure_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: João Silva'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex: joao@example.com'}),
        }
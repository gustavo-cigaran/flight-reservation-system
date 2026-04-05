from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Reservation, Airplane

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
from django import forms
from .models import Reservation, Airplane

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'flight', 'seat_number']

class AirplaneForm(forms.ModelForm):
    class Meta:
        model = Airplane
        fields = ['identifier', 'capacity']
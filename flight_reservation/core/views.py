from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from .models import Flight, Customer, Reservation

def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flight_list.html', {'flights': flights})

@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/flights/')
    else:
        form = ReservationForm()

    return render(request, 'create_reservation.html', {'form': form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers' : customers})

def show_flight_reservation(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    reservations = Reservation.objects.filter(flight=flight).select_related('customer')
    occupied_seats = reservations.values_list('seat_number', flat=True).order_by('seat_number')
    return render(request, 'flight_details.html', {
        'reservations': reservations,
        'flight': flight,
        'occupied_seats': occupied_seats
        })
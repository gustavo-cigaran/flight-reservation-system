from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm, AirplaneForm
from .models import Flight, Customer, Reservation, Airplane

@login_required
def airplane_registration(request):
    if request.method == 'POST':
        form = AirplaneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/flights/')
    else:
        form = AirplaneForm()

    return render(request, 'airplane_registration.html', {'form': form})

def airplane_list(request):
    airplanes = Airplane.objects.all()
    return render(request, 'airplane_list.html', {'airplanes': airplanes})

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

@login_required
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect(f'/flights/{reservation.flight.id}/')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'edit_reservation.html', {'form': form})

@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('/flights/')

    return render(request, 'delete_reservation.html', {'reservation': reservation})

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
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm, AirplaneForm, FlightForm
from .models import Flight, Customer, Reservation, Airplane

@login_required
def create_airplane(request):
    if request.method == 'POST':
        form = AirplaneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/flights/')
    else:
        form = AirplaneForm()

    return render(request, 'airplane_registration.html', {'form': form})

@login_required
def list_airplanes(request):
    airplanes = Airplane.objects.all()
    return render(request, 'airplane_list.html', {'airplanes': airplanes})

@login_required
def update_airplane(request, airplane_id):
    airplane = get_object_or_404(Airplane, id=airplane_id)
    if request.method == 'POST':
        form = AirplaneForm(request.POST, instance=airplane)
        if form.is_valid():
            form.save()
            return redirect('/airplanes/')
    else:
        form = AirplaneForm(instance=airplane)

    return render(request, 'edit_airplane.html', {'form': form})

@login_required
def delete_airplane(request, airplane_id):
    airplane = get_object_or_404(Airplane, id=airplane_id)
    if request.method == 'POST':
        airplane.delete()
        return redirect('/airplanes/')

    return render(request, 'delete_airplane.html', {'airplane': airplane})

@login_required
def list_flights(request):
    flights = Flight.objects.all()
    return render(request, 'flight_list.html', {'flights': flights})

@login_required
def create_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/flights/')
    else:
        form = FlightForm()

    return render(request, 'flight_registration.html', {'form': form})

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
def update_reservation(request, reservation_id):
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


@login_required
def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers' : customers})

@login_required
def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    reservations = Reservation.objects.filter(flight=flight).select_related('customer')
    occupied_seats = reservations.values_list('seat_number', flat=True).order_by('seat_number')
    return render(request, 'flight_detail.html', {
        'reservations': reservations,
        'flight': flight,
        'occupied_seats': occupied_seats
        })
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Airplane, Customer, Flight, Reservation
from django.utils import timezone
import datetime

class AirplaneModelTest(TestCase):
    def test_airplane_creation(self):
        """Testa a criação de um avião"""
        airplane = Airplane.objects.create(identifier="ABC123", capacity=100)
        self.assertEqual(airplane.identifier, "ABC123")
        self.assertEqual(airplane.capacity, 100)
        self.assertEqual(str(airplane), "ABC123")

    def test_airplane_unique_identifier(self):
        """Testa que identificadores de avião devem ser únicos"""
        Airplane.objects.create(identifier="ABC123", capacity=100)
        with self.assertRaises(Exception):
            Airplane.objects.create(identifier="ABC123", capacity=150)

class CustomerModelTest(TestCase):
    def test_customer_creation(self):
        """Testa a criação de um cliente"""
        customer = Customer.objects.create(name="João Silva", email="joao@email.com")
        self.assertEqual(customer.name, "João Silva")
        self.assertEqual(customer.email, "joao@email.com")
        self.assertEqual(str(customer), "João Silva")

class FlightModelTest(TestCase):
    def setUp(self):
        self.airplane = Airplane.objects.create(identifier="ABC123", capacity=100)

    def test_flight_creation(self):
        """Testa a criação de um voo"""
        departure_time = timezone.now() + datetime.timedelta(days=1)
        flight = Flight.objects.create(
            airplane=self.airplane,
            origin="São Paulo",
            destination="Rio de Janeiro",
            departure_time=departure_time
        )
        self.assertEqual(flight.origin, "São Paulo")
        self.assertEqual(flight.destination, "Rio de Janeiro")
        self.assertEqual(flight.airplane, self.airplane)
        expected_str = "São Paulo -> Rio de Janeiro (ABC123)"
        self.assertEqual(str(flight), expected_str)

class ReservationModelTest(TestCase):
    def setUp(self):
        self.airplane = Airplane.objects.create(identifier="ABC123", capacity=100)
        self.customer = Customer.objects.create(name="João Silva", email="joao@email.com")
        departure_time = timezone.now() + datetime.timedelta(days=1)
        self.flight = Flight.objects.create(
            airplane=self.airplane,
            origin="São Paulo",
            destination="Rio de Janeiro",
            departure_time=departure_time
        )

    def test_reservation_creation(self):
        """Testa a criação de uma reserva"""
        reservation = Reservation.objects.create(
            customer=self.customer,
            flight=self.flight,
            seat_number=1
        )
        self.assertTrue(len(reservation.record_locator) == 6)
        self.assertEqual(reservation.customer, self.customer)
        self.assertEqual(reservation.flight, self.flight)
        self.assertEqual(reservation.seat_number, 1)
        expected_str = f"{reservation.record_locator} | João Silva | São Paulo -> Rio de Janeiro (ABC123) | 1"
        self.assertEqual(str(reservation), expected_str)

    def test_unique_seat_per_flight(self):
        """Testa que assentos devem ser únicos por voo"""
        Reservation.objects.create(
            customer=self.customer,
            flight=self.flight,
            seat_number=1
        )
        customer2 = Customer.objects.create(name="Maria Santos", email="maria@email.com")
        with self.assertRaises(Exception):
            Reservation.objects.create(
                customer=customer2,
                flight=self.flight,
                seat_number=1
            )

    def test_record_locator_generation(self):
        """Testa que localizadores são gerados automaticamente e são únicos"""
        reservation1 = Reservation.objects.create(
            customer=self.customer,
            flight=self.flight,
            seat_number=1
        )
        customer2 = Customer.objects.create(name="Maria Santos", email="maria@email.com")
        reservation2 = Reservation.objects.create(
            customer=customer2,
            flight=self.flight,
            seat_number=2
        )
        self.assertNotEqual(reservation1.record_locator, reservation2.record_locator)
        self.assertTrue(len(reservation1.record_locator) == 6)
        self.assertTrue(len(reservation2.record_locator) == 6)

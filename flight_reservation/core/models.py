from django.db import models

class Airplane(models.Model):
    identifier = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.identifier
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Flight(models.Model):
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()

    def __str__(self):
        return f"{self.origin} -> {self.destination} ({self.airplane})"
    
class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.IntegerField()

    class Meta:
        unique_together = ('flight', 'seat_number')

    def __str__(self):
        return f"{self.customer} | {self.flight} | {self.seat_number}"
    

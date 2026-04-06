from django.db import models
import random
import string

def generate_record_locator():
    characters = string.ascii_uppercase + string.digits
    characters = characters.replace('0', '').replace('O', '').replace('I', '').replace('1', '')
    
    return ''.join(random.choice(characters) for _ in range(6))

class Airplane(models.Model):
    identifier = models.CharField(
        max_length=100, 
        unique=True,
        error_messages={
            'unique': 'Já existe um avião com este identificador. Por favor, escolha outro.'
        })
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.identifier
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

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
    record_locator = models.CharField(max_length=6, unique=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.IntegerField()

    class Meta:
        unique_together = ('flight', 'seat_number')

    def save(self, *args, **kwargs):
        if not self.record_locator:
            while True:
                new_record_locator = generate_record_locator()
                if not Reservation.objects.filter(record_locator=new_record_locator).exists():
                    self.record_locator = new_record_locator
                    break

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.record_locator} | {self.customer} | {self.flight} | {self.seat_number}"
    

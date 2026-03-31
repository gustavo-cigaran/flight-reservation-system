from django.contrib import admin
from .models import Airplane, Customer, Flight, Reservation

admin.site.register(Airplane)
admin.site.register(Customer)
admin.site.register(Flight)
admin.site.register(Reservation)

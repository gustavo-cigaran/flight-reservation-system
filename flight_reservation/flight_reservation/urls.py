from django.contrib import admin
from django.urls import path
from core.views import flight_list, create_reservation, customer_list, show_flight_reservation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', flight_list),
    path('reserve/', create_reservation),
    path('customers/', customer_list),
    path('flights/<int:flight_id>/',show_flight_reservation),
]

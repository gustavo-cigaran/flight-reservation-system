from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from core.forms import LoginForm
from core.views import *

urlpatterns = [
    path('', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('admin/', admin.site.urls),
    path('airplanes/', list_airplanes),
    path('airplanes/register/', create_airplane),
    path('airplanes/edit/<int:airplane_id>/', update_airplane),
    path('airplanes/delete/<int:airplane_id>/', delete_airplane),
    path('flights/', list_flights, name='flight_list'),
    path('flights/register/', create_flight),
    path('flights/edit/<int:flight_id>/', update_flight),
    path('reserve/', create_reservation),
    path('flights/edit/<int:reservation_id>/', update_reservation),
    path('flights/delete/<int:reservation_id>/', delete_reservation),
    path('customers/', list_customers),
    path('flights/<int:flight_id>/', flight_detail, name='flight_detail'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]

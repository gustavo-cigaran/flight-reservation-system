from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from core.forms import LoginForm
from core.views import *

urlpatterns = [
    path('', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('admin/', admin.site.urls),
    path('airplanes/', airplane_list),
    path('airplanes/register/', airplane_registration),
    path('flights/', flight_list, name='flight_list'),
    path('reserve/', create_reservation),
    path('flights/edit/<int:reservation_id>/', edit_reservation),
    path('flights/delete/<int:reservation_id>/', delete_reservation),
    path('customers/', customer_list),
    path('flights/<int:flight_id>/',show_flight_reservation),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]

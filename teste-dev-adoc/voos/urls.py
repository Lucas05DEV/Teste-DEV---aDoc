from django.urls import path
from . import views

urlpatterns = [

    ## Auth
    path('login/',views.CustomLoginView.as_view(), name='login'),
    path('logout/',views.CustomLogoutView.as_view(), name='logout'),
    path('register/',views.RegisterView.as_view(), name='register'),

    ## Airplane URLs
    path('airplanes/', views.AirplaneListView.as_view(), name='airplane-list'),
    path('airplanes/new/', views.AirplaneCreateView.as_view(), name='airplane-create'),
    path('airplanes/<int:pk>/edit/', views.AirplaneUpdateView.as_view(), name='airplane-update'),
    path('airplanes/<int:pk>/delete/', views.AirplaneDeleteView.as_view(), name='airplane-delete'),

    ## Flight URLs
    path('flights/', views.FlightListView.as_view(), name='flight-list'),
    path('flights/new/', views.FlightCreateView.as_view(), name='flight-create'),
    path('flights/<int:pk>/', views.FlightDetailView.as_view(), name='flight-detail'),
    path('flights/<int:pk>/edit/', views.FlightUpdateView.as_view(), name='flight-update'),
    path('flights/<int:pk>/delete/', views.FlightDeleteView.as_view(), name='flight-delete'),
    path('flights/<int:pk>/reserve/', views.ClientReserveView.as_view(), name='flight-reserve'),


    ## Client URLs
    path('clients/', views.ClientListView.as_view(), name='client-list'),
    path('clients/new/', views.ClientCreateView.as_view(), name='client-create'),
    path('clients/<int:pk>/edit/', views.ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client-delete'),

    ## Reservation URLs
    path('reservations/', views.ReservationListView.as_view(), name='reservation-list'),
    path('reservations/new/', views.ReservationCreateView.as_view(), name='reservation-create'),
    path('reservations/<int:pk>/', views.ReservationDetailView.as_view(), name='reservation-detail'),
    path('reservations/<int:pk>/edit/', views.ReservationUpdateView.as_view(), name='reservation-update'),
    path('reservations/<int:pk>/delete/', views.ReservationDeleteView.as_view(), name='reservation-delete'),
]   

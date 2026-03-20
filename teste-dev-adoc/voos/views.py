from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Airplane, Flight, Client, Reservation

## Airplane

class AirplaneListView(ListView):
    model = Airplane
    template_name = 'airplanes/airplane_list.html'
    context_object_name = 'airplanes'

class AirplaneCreateView(CreateView):
    model = Airplane
    template_name = 'airplanes/airplane_form.html'
    fields = ['identification', 'max_capacity']
    success_url = reverse_lazy('airplane-list')

    def form_valid(self, form):
        messages.success(self.request, 'Avião cadastrado com sucesso!')
        return super().form_valid(form)
    
class AirplaneUpdateView(UpdateView):
    model = Airplane
    template_name = 'airplanes/airplane_form.html'
    fields = ['identification', 'max_capacity']
    success_url = reverse_lazy('airplane-list')

    def form_valid(self, form):
        messages.success(self.request, 'Avião atualizado com sucesso!')
        return super().form_valid(form)
    
class AirplaneDeleteView(DeleteView):
    model = Airplane
    template_name = 'airplanes/airplane_confirm_delete.html'
    success_url = reverse_lazy('airplane-list')

    def form_valid(self, form):
        messages.success(self.request, 'Avião removido com sucesso!')
        return super().form_valid(form)
    
## Flight

class FlightListView(ListView):
    model = Flight
    template_name = 'flights/flight_list.html'
    context_object_name = 'flights'

class FlightDetailView(DetailView):
    model = Flight
    template_name = 'flights/flight_detail.html'
    context_object_name = 'flight'

class FlightCreateView(CreateView):
    model = Flight
    template_name = 'flights/flight_form.html'
    fields = ['airplane', 'origin', 'destination', 'date', 'time']
    success_url = reverse_lazy('flight-list')

    def form_valid(self, form):
        messages.success(self.request, 'Voo cadastrado com sucesso!')
        return super().form_valid(form)

class FlightUpdateView(UpdateView):
    model = Flight
    template_name = 'flights/flight_form.html'
    fields = ['airplane', 'origin', 'destination', 'date', 'time']
    success_url = reverse_lazy('flight-list')

    def form_valid(self, form):
        messages.success(self.request, 'Voo atualizado com sucesso!')
        return super().form_valid(form)

class FlightDeleteView(DeleteView):
    model = Flight
    template_name = 'flights/flight_confirm_delete.html'
    success_url = reverse_lazy('flight-list')

    def form_valid(self, form):
        messages.success(self.request, 'Voo removido com sucesso!')
        return super().form_valid(form)
    
## Client

class ClientListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

class ClientCreateView(CreateView):
    model = Client
    template_name = 'clients/client_form.html'
    fields = ['name', 'email', 'telephone']
    success_url = reverse_lazy('client-list')

    def form_valid(self, form):
        messages.success(self.request, 'Cliente cadastrado com sucesso!')
        return super().form_valid(form)
    
class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'clients/client_form.html'
    fields = ['name', 'email', 'telephone']
    success_url = reverse_lazy('client-list')

    def form_valid(self, form):
        messages.success(self.request, 'Cliente atualizado com sucesso!')
        return super().form_valid(form)
    
class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('client-list')

    def form_valid(self, form):
        messages.success(self.request, 'Cliente removido com sucesso!')
        return super().form_valid(form)

## Reservation

class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservations/reservation_list.html'
    context_object_name = 'reservations'

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'reservations/reservation_detail.html'
    context_object_name = 'reservation'
    
class ReservationCreateView(CreateView):
    model = Reservation
    template_name = 'reservations/reservation_form.html'
    fields = ['flight', 'client', 'seat_number']
    success_url = reverse_lazy('reservation-list')

    def form_valid(self, form):
        messages.success(self.request, 'Reserva cadastrada com sucesso!')
        return super().form_valid(form)
    
class ReservationUpdateView(UpdateView):
    model = Reservation
    template_name = 'reservations/reservation_form.html'
    fields = ['flight', 'client', 'seat_number', 'status']
    success_url = reverse_lazy('reservation-list')

    def form_valid(self, form):
        messages.success(self.request, 'Reserva atualizada com sucesso!')
        return super().form_valid(form)

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'reservations/reservation_confirm_delete.html'
    success_url = reverse_lazy('reservation-list')

    def form_valid(self, form):
        messages.success(self.request, 'Reserva removida com sucesso!')
        return super().form_valid(form)
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Airplane, Flight, Client, Reservation

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
    
## Auth

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('airplane-list')
        return reverse_lazy('flight-list')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'telephone', 'password1', 'password2']

class RegisterView(CreateView):
    template_name = 'auth/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        Client.objects.create(
            user=user,
            name=user.username,
            email=form.cleaned_data['email'],
            telephone=form.cleaned_data.get('telephone', '')
        )
        messages.success(self.request, 'Account created! Please sign in.')
        return redirect(self.success_url)

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
    
## Self Reservation

class ClientReserveView(LoginRequiredMixin, View):
    template_name = 'flights/flight_reserve.html'

    def get_client(self):
        return get_object_or_404(Client, user=self.request.user)
    
    def get(self, request, pk):
        flight = get_object_or_404(Flight, pk=pk)
        client = self.get_client()
        already_reserved = Reservation.objects.filter(
            flight=flight, client=client, status='active'
        ).exists()
        return render(request, self.template_name, {
            'flight': flight,
            'already_reserved': already_reserved,
        })
            
    def post(self, request, pk):
        from django.shortcuts import render
        flight = get_object_or_404(Flight, pk=pk)
        client = self.get_client()
        seat_number = request.POST.get('seat_number')

        if not seat_number:
            messages.error(request, 'Please choose a seat number.')
            return redirect('flight-reserve', pk=pk)

        try:
            reservation = Reservation(
                flight=flight,
                client=client,
                seat_number=int(seat_number)
            )
            reservation.full_clean()
            reservation.save()
            messages.success(request, f'Seat {seat_number} reserved successfully!')
            return redirect('flight-list')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('flight-reserve', pk=pk)
        
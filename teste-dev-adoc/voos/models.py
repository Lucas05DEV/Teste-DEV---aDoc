from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError

## Class Airplane
class Airplane(models.Model):
    identification = models.CharField(max_length=30, unique=True)
    max_capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.identification} ({self.max_capacity} pax)"
    
    class Meta:
        verbose_name = "Airplane"
        verbose_name_plural = "Airplanes"
        ordering = ['identification']

## Class Flight
class Flight(models.Model):
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='flights')
    origin = models.CharField(max_length=100)
    destination =  models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.origin} → {self.destination} ({self.date})"
    
    def available_seats(self):
        active_reservations = self.reservations.filter(status='active').count()
        return self.airplane.max_capacity - active_reservations

    def clean(self):
        if self.origin and self.destination and self.origin == self.destination:
            raise ValidationError("O local de origem e destino não podem ser iguais.")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Flight"
        verbose_name_plural = "Flights"
        ordering = ['date', 'time']

## Class Client
class Client(models.Model):
    telephone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Informe um número de telefone válido (9 a 15 dígitos)")
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, validators=[telephone_validator], blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['name']
    
## Class Reservation  
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reservations')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reservations')
    seat_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    reservation_date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.flight and self.seat_number:
            capacity = self.flight.airplane.max_capacity
            if self.seat_number > capacity:
                raise ValidationError(f"O número do assento deve ser entre 1 e {capacity}.")

        if self.flight and self.client:
            existing_resevation = Reservation.objects.filter(flight=self.flight, client=self.client, status='active').exclude(pk=self.pk)

            if existing_resevation.exists():
                raise ValidationError("O cliente já possui uma reserva ativa para este voo.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation for {self.client.name} on flight {self.flight} (Seat {self.seat_number})"

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
        ordering = ['reservation_date']
        constraints = [
            models.UniqueConstraint(fields=['flight', 'seat_number'], name='unique_seat_per_flight'),
            models.UniqueConstraint(fields=['flight', 'client'], condition=models.Q(status='active'), name='unique_active_reservation_per_client_flight'),
        ]


from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.PositiveBigIntegerField()
    password = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Staf(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AdminReg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.PositiveBigIntegerField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Deliveryboy(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name





class FuelStation(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    fuel_price = models.DecimalField(max_digits=5, decimal_places=2)
    available_fuels = models.TextField()  # Example: "Petrol, Diesel, CNG"
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    fuel_station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.fuel_type} - {self.amount}"

class FuelConsumption(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    distance_covered = models.DecimalField(max_digits=6, decimal_places=2)
    fuel_used = models.DecimalField(max_digits=5, decimal_places=2)
    trip_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.distance_covered} km"

class Notification(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}"



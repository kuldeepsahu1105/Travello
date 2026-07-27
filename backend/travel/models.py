from django.db import models


class Trip(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    cover_image = models.URLField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} - {self.destination}"


class Booking(models.Model):
    TYPE_CHOICES = [
        ('flight', 'Flight'),
        ('hotel', 'Hotel'),
        ('car', 'Car Rental'),
        ('activity', 'Activity'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='bookings')
    title = models.CharField(max_length=200)
    booking_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    provider = models.CharField(max_length=200, blank=True)
    confirmation_number = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    booking_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['booking_date']

    def __str__(self):
        return f"{self.title} ({self.booking_type})"


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('transport', 'Transport'),
        ('accommodation', 'Accommodation'),
        ('food', 'Food & Dining'),
        ('entertainment', 'Entertainment'),
        ('shopping', 'Shopping'),
        ('other', 'Other'),
    ]

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} - ${self.amount}"


class ItineraryItem(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='itinerary')
    day = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['day', 'time']
        verbose_name_plural = 'itinerary items'

    def __str__(self):
        return f"Day {self.day}: {self.title}"

from django.contrib import admin
from .models import Trip, Booking, Expense, ItineraryItem


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['title', 'destination', 'start_date', 'end_date', 'status', 'budget']
    list_filter = ['status']
    search_fields = ['title', 'destination']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['title', 'trip', 'booking_type', 'amount', 'status', 'booking_date']
    list_filter = ['booking_type', 'status']


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['title', 'trip', 'category', 'amount', 'date']
    list_filter = ['category']


@admin.register(ItineraryItem)
class ItineraryItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'trip', 'day', 'time', 'location']

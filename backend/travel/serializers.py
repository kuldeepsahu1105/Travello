from rest_framework import serializers
from .models import Trip, Booking, Expense, ItineraryItem


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class ItineraryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryItem
        fields = '__all__'


class TripListSerializer(serializers.ModelSerializer):
    total_expenses = serializers.SerializerMethodField()
    booking_count = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = [
            'id', 'title', 'destination', 'description', 'start_date', 'end_date',
            'budget', 'status', 'cover_image', 'total_expenses', 'booking_count',
            'created_at', 'updated_at',
        ]

    def get_total_expenses(self, obj):
        return sum(e.amount for e in obj.expenses.all())

    def get_booking_count(self, obj):
        return obj.bookings.count()


class TripDetailSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)
    expenses = ExpenseSerializer(many=True, read_only=True)
    itinerary = ItineraryItemSerializer(many=True, read_only=True)
    total_expenses = serializers.SerializerMethodField()
    remaining_budget = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = [
            'id', 'title', 'destination', 'description', 'start_date', 'end_date',
            'budget', 'status', 'cover_image', 'bookings', 'expenses', 'itinerary',
            'total_expenses', 'remaining_budget', 'created_at', 'updated_at',
        ]

    def get_total_expenses(self, obj):
        return sum(e.amount for e in obj.expenses.all())

    def get_remaining_budget(self, obj):
        total = sum(e.amount for e in obj.expenses.all())
        return obj.budget - total

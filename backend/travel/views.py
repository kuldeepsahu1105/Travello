from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count
from .models import Trip, Booking, Expense, ItineraryItem
from .serializers import (
    TripListSerializer, TripDetailSerializer,
    BookingSerializer, ExpenseSerializer, ItineraryItemSerializer,
)


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TripDetailSerializer
        return TripListSerializer

    @action(detail=False, methods=['get'])
    def stats(self, request):
        trips = Trip.objects.all()
        return Response({
            'total_trips': trips.count(),
            'active_trips': trips.filter(status='active').count(),
            'planned_trips': trips.filter(status='planned').count(),
            'completed_trips': trips.filter(status='completed').count(),
            'total_budget': trips.aggregate(total=Sum('budget'))['total'] or 0,
            'total_expenses': Expense.objects.aggregate(total=Sum('amount'))['total'] or 0,
            'total_bookings': Booking.objects.count(),
            'destinations': trips.values('destination').annotate(
                count=Count('id')
            ).order_by('-count')[:5],
        })


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        trip_id = self.request.query_params.get('trip')
        if trip_id:
            qs = qs.filter(trip_id=trip_id)
        return qs


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        trip_id = self.request.query_params.get('trip')
        if trip_id:
            qs = qs.filter(trip_id=trip_id)
        return qs


class ItineraryItemViewSet(viewsets.ModelViewSet):
    queryset = ItineraryItem.objects.all()
    serializer_class = ItineraryItemSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        trip_id = self.request.query_params.get('trip')
        if trip_id:
            qs = qs.filter(trip_id=trip_id)
        return qs

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet, BookingViewSet, ExpenseViewSet, ItineraryItemViewSet

router = DefaultRouter()
router.register('trips', TripViewSet)
router.register('bookings', BookingViewSet)
router.register('expenses', ExpenseViewSet)
router.register('itinerary', ItineraryItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

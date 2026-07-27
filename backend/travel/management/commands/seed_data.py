from django.core.management.base import BaseCommand
from datetime import date, time, timedelta
from decimal import Decimal
from travel.models import Trip, Booking, Expense, ItineraryItem


class Command(BaseCommand):
    help = 'Seed the database with sample travel data'

    def handle(self, *args, **options):
        Trip.objects.all().delete()

        trips_data = [
            {
                'title': 'Tokyo Adventure',
                'destination': 'Tokyo, Japan',
                'description': 'Explore the vibrant streets of Shibuya, visit ancient temples, and enjoy world-class sushi.',
                'start_date': date(2026, 4, 10),
                'end_date': date(2026, 4, 18),
                'budget': Decimal('4500.00'),
                'status': 'planned',
                'cover_image': 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800',
            },
            {
                'title': 'European Grand Tour',
                'destination': 'Paris, France',
                'description': 'A multi-city tour through Paris, Rome, and Barcelona with art, culture, and cuisine.',
                'start_date': date(2026, 6, 1),
                'end_date': date(2026, 6, 15),
                'budget': Decimal('8000.00'),
                'status': 'planned',
                'cover_image': 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800',
            },
            {
                'title': 'Bali Retreat',
                'destination': 'Bali, Indonesia',
                'description': 'Relax on pristine beaches, explore rice terraces, and experience Balinese culture.',
                'start_date': date(2025, 12, 1),
                'end_date': date(2025, 12, 10),
                'budget': Decimal('3000.00'),
                'status': 'completed',
                'cover_image': 'https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=800',
            },
            {
                'title': 'New York City Weekend',
                'destination': 'New York, USA',
                'description': 'Broadway shows, Central Park, museums, and the best pizza in the world.',
                'start_date': date(2026, 3, 14),
                'end_date': date(2026, 3, 17),
                'budget': Decimal('2500.00'),
                'status': 'active',
                'cover_image': 'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=800',
            },
        ]

        for data in trips_data:
            trip = Trip.objects.create(**data)

            if trip.destination == 'Tokyo, Japan':
                Booking.objects.create(
                    trip=trip, title='ANA Flight to Tokyo', booking_type='flight',
                    provider='All Nippon Airways', confirmation_number='ANA-78234',
                    amount=Decimal('1200.00'), booking_date=date(2026, 2, 1), status='confirmed',
                )
                Booking.objects.create(
                    trip=trip, title='Shibuya Hotel', booking_type='hotel',
                    provider='Hotel Gracery Shinjuku', confirmation_number='HGS-44521',
                    amount=Decimal('1800.00'), booking_date=date(2026, 2, 5), status='confirmed',
                )
                Expense.objects.create(
                    trip=trip, title='JR Rail Pass', category='transport',
                    amount=Decimal('280.00'), date=date(2026, 4, 10),
                )
                ItineraryItem.objects.create(
                    trip=trip, day=1, title='Arrive at Narita Airport',
                    time=time(14, 0), location='Narita International Airport',
                    description='Check in to hotel and explore Shibuya crossing.',
                )
                ItineraryItem.objects.create(
                    trip=trip, day=2, title='Visit Senso-ji Temple',
                    time=time(9, 0), location='Asakusa, Tokyo',
                    description='Morning temple visit followed by Nakamise shopping street.',
                )

            elif trip.destination == 'New York, USA':
                Booking.objects.create(
                    trip=trip, title='Delta Flight NYC', booking_type='flight',
                    provider='Delta Airlines', confirmation_number='DL-99201',
                    amount=Decimal('450.00'), booking_date=date(2026, 1, 15), status='confirmed',
                )
                Expense.objects.create(
                    trip=trip, title='Broadway Tickets', category='entertainment',
                    amount=Decimal('320.00'), date=date(2026, 3, 15),
                )
                Expense.objects.create(
                    trip=trip, title='Dinner at Katz Deli', category='food',
                    amount=Decimal('65.00'), date=date(2026, 3, 14),
                )

            elif trip.destination == 'Bali, Indonesia':
                Expense.objects.create(
                    trip=trip, title='Villa Rental', category='accommodation',
                    amount=Decimal('1200.00'), date=date(2025, 12, 1),
                )
                Expense.objects.create(
                    trip=trip, title='Scuba Diving', category='entertainment',
                    amount=Decimal('180.00'), date=date(2025, 12, 5),
                )

        self.stdout.write(self.style.SUCCESS(f'Seeded {Trip.objects.count()} trips with related data.'))

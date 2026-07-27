import { Component, OnInit } from '@angular/core';
import { CommonModule, CurrencyPipe, DatePipe } from '@angular/common';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { TravelService } from '../../services/travel.service';
import { Trip, Booking, Expense, ItineraryItem } from '../../models/travel.models';

@Component({
  selector: 'app-trip-detail',
  standalone: true,
  imports: [CommonModule, CurrencyPipe, DatePipe, RouterLink, FormsModule],
  templateUrl: './trip-detail.component.html',
  styleUrl: './trip-detail.component.scss',
})
export class TripDetailComponent implements OnInit {
  trip: Trip | null = null;
  loading = true;
  activeTab: 'overview' | 'bookings' | 'expenses' | 'itinerary' = 'overview';

  showBookingForm = false;
  showExpenseForm = false;
  showItineraryForm = false;

  newBooking: Partial<Booking> = {};
  newExpense: Partial<Expense> = {};
  newItinerary: Partial<ItineraryItem> = {};

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private travelService: TravelService,
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.loadTrip(id);
  }

  loadTrip(id: number): void {
    this.loading = true;
    this.travelService.getTrip(id).subscribe({
      next: (trip) => {
        this.trip = trip;
        this.loading = false;
      },
      error: () => this.router.navigate(['/trips']),
    });
  }

  deleteTrip(): void {
    if (this.trip && confirm('Delete this trip and all related data?')) {
      this.travelService.deleteTrip(this.trip.id!).subscribe(() => {
        this.router.navigate(['/trips']);
      });
    }
  }

  addBooking(): void {
    if (!this.trip) return;
    this.newBooking.trip = this.trip.id;
    this.travelService.createBooking(this.newBooking).subscribe(() => {
      this.showBookingForm = false;
      this.newBooking = {};
      this.loadTrip(this.trip!.id!);
    });
  }

  addExpense(): void {
    if (!this.trip) return;
    this.newExpense.trip = this.trip.id;
    this.travelService.createExpense(this.newExpense).subscribe(() => {
      this.showExpenseForm = false;
      this.newExpense = {};
      this.loadTrip(this.trip!.id!);
    });
  }

  addItineraryItem(): void {
    if (!this.trip) return;
    this.newItinerary.trip = this.trip.id;
    this.travelService.createItineraryItem(this.newItinerary).subscribe(() => {
      this.showItineraryForm = false;
      this.newItinerary = {};
      this.loadTrip(this.trip!.id!);
    });
  }

  getStatusClass(status: string): string {
    return `status-${status}`;
  }

  getBudgetPercent(): number {
    if (!this.trip || !this.trip.budget) return 0;
    const spent = this.trip.total_expenses || 0;
    return Math.min(100, (spent / this.trip.budget) * 100);
  }
}

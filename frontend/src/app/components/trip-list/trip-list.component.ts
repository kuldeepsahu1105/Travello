import { Component, OnInit } from '@angular/core';
import { CommonModule, CurrencyPipe, DatePipe } from '@angular/common';
import { RouterLink } from '@angular/router';
import { TravelService } from '../../services/travel.service';
import { Trip } from '../../models/travel.models';

@Component({
  selector: 'app-trip-list',
  standalone: true,
  imports: [CommonModule, CurrencyPipe, DatePipe, RouterLink],
  templateUrl: './trip-list.component.html',
  styleUrl: './trip-list.component.scss',
})
export class TripListComponent implements OnInit {
  trips: Trip[] = [];
  loading = true;
  filterStatus = 'all';

  constructor(private travelService: TravelService) {}

  ngOnInit(): void {
    this.loadTrips();
  }

  loadTrips(): void {
    this.loading = true;
    this.travelService.getTrips().subscribe({
      next: (data: any) => {
        this.trips = data.results || data;
        this.loading = false;
      },
      error: () => (this.loading = false),
    });
  }

  get filteredTrips(): Trip[] {
    if (this.filterStatus === 'all') return this.trips;
    return this.trips.filter((t) => t.status === this.filterStatus);
  }

  deleteTrip(id: number, event: Event): void {
    event.preventDefault();
    event.stopPropagation();
    if (confirm('Are you sure you want to delete this trip?')) {
      this.travelService.deleteTrip(id).subscribe(() => this.loadTrips());
    }
  }

  getStatusClass(status: string): string {
    return `status-${status}`;
  }
}

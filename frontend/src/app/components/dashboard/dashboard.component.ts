import { Component, OnInit } from '@angular/core';
import { CommonModule, CurrencyPipe } from '@angular/common';
import { RouterLink } from '@angular/router';
import { TravelService } from '../../services/travel.service';
import { DashboardStats, Trip } from '../../models/travel.models';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, CurrencyPipe, RouterLink],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss',
})
export class DashboardComponent implements OnInit {
  stats: DashboardStats | null = null;
  recentTrips: Trip[] = [];
  loading = true;

  constructor(private travelService: TravelService) {}

  ngOnInit(): void {
    this.travelService.getStats().subscribe({
      next: (stats) => {
        this.stats = stats;
        this.loading = false;
      },
      error: () => (this.loading = false),
    });

    this.travelService.getTrips().subscribe({
      next: (data: any) => {
        const trips = data.results || data;
        this.recentTrips = trips.slice(0, 3);
      },
    });
  }

  getStatusClass(status: string): string {
    return `status-${status}`;
  }
}

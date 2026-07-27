import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { TravelService } from '../../services/travel.service';
import { Trip } from '../../models/travel.models';

@Component({
  selector: 'app-trip-form',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './trip-form.component.html',
  styleUrl: './trip-form.component.scss',
})
export class TripFormComponent implements OnInit {
  trip: Partial<Trip> = {
    title: '',
    destination: '',
    description: '',
    start_date: '',
    end_date: '',
    budget: 0,
    status: 'planned',
    cover_image: '',
  };
  isEdit = false;
  tripId: number | null = null;
  saving = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private travelService: TravelService,
  ) {}

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id && id !== 'new') {
      this.isEdit = true;
      this.tripId = Number(id);
      this.travelService.getTrip(this.tripId).subscribe({
        next: (trip) => (this.trip = trip),
        error: () => this.router.navigate(['/trips']),
      });
    }
  }

  onSubmit(): void {
    this.saving = true;
    const request = this.isEdit
      ? this.travelService.updateTrip(this.tripId!, this.trip)
      : this.travelService.createTrip(this.trip);

    request.subscribe({
      next: (trip) => {
        this.saving = false;
        this.router.navigate(['/trips', trip.id]);
      },
      error: () => (this.saving = false),
    });
  }
}

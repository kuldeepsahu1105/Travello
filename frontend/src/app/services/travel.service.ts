import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Trip, Booking, Expense, ItineraryItem, DashboardStats } from '../models/travel.models';

const API_URL = 'http://localhost:8000/api';

@Injectable({ providedIn: 'root' })
export class TravelService {
  constructor(private http: HttpClient) {}

  getStats(): Observable<DashboardStats> {
    return this.http.get<DashboardStats>(`${API_URL}/trips/stats/`);
  }

  getTrips(): Observable<Trip[]> {
    return this.http.get<{ results: Trip[] } | Trip[]>(`${API_URL}/trips/`).pipe(
      // Handle both paginated and non-paginated responses
    ) as Observable<Trip[]>;
  }

  getTrip(id: number): Observable<Trip> {
    return this.http.get<Trip>(`${API_URL}/trips/${id}/`);
  }

  createTrip(trip: Partial<Trip>): Observable<Trip> {
    return this.http.post<Trip>(`${API_URL}/trips/`, trip);
  }

  updateTrip(id: number, trip: Partial<Trip>): Observable<Trip> {
    return this.http.put<Trip>(`${API_URL}/trips/${id}/`, trip);
  }

  deleteTrip(id: number): Observable<void> {
    return this.http.delete<void>(`${API_URL}/trips/${id}/`);
  }

  getBookings(tripId?: number): Observable<Booking[]> {
    const url = tripId ? `${API_URL}/bookings/?trip=${tripId}` : `${API_URL}/bookings/`;
    return this.http.get<Booking[]>(url);
  }

  createBooking(booking: Partial<Booking>): Observable<Booking> {
    return this.http.post<Booking>(`${API_URL}/bookings/`, booking);
  }

  deleteBooking(id: number): Observable<void> {
    return this.http.delete<void>(`${API_URL}/bookings/${id}/`);
  }

  getExpenses(tripId?: number): Observable<Expense[]> {
    const url = tripId ? `${API_URL}/expenses/?trip=${tripId}` : `${API_URL}/expenses/`;
    return this.http.get<Expense[]>(url);
  }

  createExpense(expense: Partial<Expense>): Observable<Expense> {
    return this.http.post<Expense>(`${API_URL}/expenses/`, expense);
  }

  deleteExpense(id: number): Observable<void> {
    return this.http.delete<void>(`${API_URL}/expenses/${id}/`);
  }

  getItinerary(tripId: number): Observable<ItineraryItem[]> {
    return this.http.get<ItineraryItem[]>(`${API_URL}/itinerary/?trip=${tripId}`);
  }

  createItineraryItem(item: Partial<ItineraryItem>): Observable<ItineraryItem> {
    return this.http.post<ItineraryItem>(`${API_URL}/itinerary/`, item);
  }

  deleteItineraryItem(id: number): Observable<void> {
    return this.http.delete<void>(`${API_URL}/itinerary/${id}/`);
  }
}
